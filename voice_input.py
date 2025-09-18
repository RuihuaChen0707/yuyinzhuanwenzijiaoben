# === 最终正式版代码 ===
import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os
import tempfile
from pynput import keyboard
import sys
import time

# --- 配置区 ---
MODEL_SIZE = "small"
HOTKEY_COMBINATION = {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.Key.space}
SAMPLE_RATE = 16000
TEMP_FILE = os.path.join(tempfile.gettempdir(), "temp_audio.wav")

# --- 全局变量 ---
is_recording = False
audio_data = []
current_keys = set()
model = None
stream = None

# --- 功能函数 ---
def record_audio():
    """录音的主要逻辑"""
    global audio_data, stream, is_recording
    audio_data = []
    
    def audio_callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        audio_data.append(indata.copy())

    try:
        stream = sd.InputStream(device="MacBook Air麦克风", callback=audio_callback, samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        stream.start()
        print("\n[Whisper] 正在录音... 再次按下快捷键停止。")
    except Exception as e:
        print(f"\n[Whisper] 错误：无法启动录音。请检查设备名称或权限。错误信息: {e}", file=sys.stderr)
        is_recording = False # 重置状态

def stop_and_transcribe():
    """停止录音、转写并输入"""
    global stream, audio_data
    
    if not stream or not stream.active:
        return

    stream.stop()
    stream.close()
    stream = None
    print("[Whisper] 录音结束，正在处理...")

    if not audio_data:
        print("[Whisper] 没有录到有效音频。")
        return
    
    try:
        recording_np = np.concatenate(audio_data, axis=0)
        audio_data = []
        write(TEMP_FILE, SAMPLE_RATE, recording_np)
        
        if os.path.getsize(TEMP_FILE) < 1024:
            print("[Whisper] 录音文件过小，已忽略。")
            return

        prompt = "编写Python代码。定义一个函数，创建一个类。处理JSON数据，调用API接口。前端界面，后端逻辑，连接数据库。修复这个bug，重构这段代码。实现用户登录和注册功能。这是一个关于软件开发的任务。"
        result = model.transcribe(TEMP_FILE, fp16=False, initial_prompt=prompt)
        
        transcribed_text = result['text'].strip()
        
        if transcribed_text:
            print(f"[Whisper] 识别结果: {transcribed_text}")
            time.sleep(0.1)
            kb_controller = keyboard.Controller()
            kb_controller.type(transcribed_text)
        else:
            print("[Whisper] 识别结果为空。")

    except Exception as e:
        print(f"[Whisper] 严重错误，在处理过程中发生异常: {e}")
    finally:
        if os.path.exists(TEMP_FILE):
            os.remove(TEMP_FILE)

def on_hotkey_toggle():
    global is_recording
    is_recording = not is_recording
    if is_recording:
        record_audio()
    else:
        stop_and_transcribe()

# --- 热键监听逻辑 ---
def on_press(key):
    if key in HOTKEY_COMBINATION:
        current_keys.add(key)
        if all(k in current_keys for k in HOTKEY_COMBINATION):
            on_hotkey_toggle()

def on_release(key):
    try:
        if key in HOTKEY_COMBINATION:
            current_keys.remove(key)
    except KeyError:
        pass

# --- 主程序入口 ---
if __name__ == "__main__":
    print("="*30)
    print("  AI 语音输入工具已启动")
    print("="*30)
    print(f"快捷键: Ctrl + Shift + Space (空格)")
    
    print(f"[Whisper] 正在预加载模型 '{MODEL_SIZE}'，请稍候...")
    try:
        model = whisper.load_model(MODEL_SIZE)
        print(f"[Whisper] 模型 '{MODEL_SIZE}' 加载完毕。")
    except Exception as e:
        print(f"[Whisper] 致命错误：加载模型失败: {e}", file=sys.stderr)
        sys.exit(1)
        
    print("\n一切就绪！将光标定位到目标窗口即可开始使用。")
    print("按 Ctrl+C 退出脚本。")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()