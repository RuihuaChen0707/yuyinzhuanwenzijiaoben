AI 语音输入助手 - 终极使用指南 🎙️
这不仅仅是一个工具，更是一份详尽的指南，旨在帮助你从零开始，成功部署一个强大的、在本地运行的 AI 语音输入助手。
它将彻底改变你在终端（尤其是 Claude Code）中的交互方式，用自然的语音指令，解放你的键盘。
目录
✨ 功能特性
⚙️ 安装与配置
第一步：准备环境依赖
第二步：获取并安装项目
▶️ 启动与使用
🚑 问题排查指南
问题一：(macOS) 没反应或报错？终极权限解决方案
问题二：为什么识别结果为空或不准？麦克风终极解决方案
🎨 个性化定制
如何修改快捷键？
如何调整识别模型（速度 vs 准确度）？
🤝 参与贡献 & 项目缘起
📄 开源许可
✨ 功能特性
全局热键：默认 Ctrl + Shift + Space，在任何程序中无缝启动/停止录音。
本地运行：语音识别完全在你自己的电脑上完成，保护你的数据隐私。
高准确度：基于 OpenAI Whisper small 模型，并通过“编程提示”优化中文识别。
跨平台兼容：本指南及代码同时支持 macOS 和 Windows。
完全免费：所有依赖均为开源库，无任何 API 费用。
⚙️ 安装与配置
我们开始吧！请严格按照以下步骤操作。
第一步：准备环境依赖
在安装本项目之前，你的电脑需要一些基础“零件”。
Python: 核心语言。
👉 点击这里下载 Python
Windows 用户注意：在安装过程中，务必勾选 Add Python to PATH 选项！
Git: 用于从 GitHub 下载本项目。
👉 点击这里下载 Git
FFmpeg: Whisper 用来处理音频的强大工具。
macOS 用户 (最简单)：
首先，安装 Homebrew (macOS的软件管家)，在终端运行：
code
Bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
然后，用 Homebrew 安装 FFmpeg：
code
Bash
brew install ffmpeg
Windows 用户：
请参考这篇详细教程，手动安装 FFmpeg 并将其添加到系统环境变量中：Windows 安装 FFmpeg 教程
第二步：获取并安装项目
环境准备好后，我们只需几条命令即可完成所有安装。
打开终端
macOS: 打开 “终端” (Terminal) 程序。
Windows: 打开 “Git Bash” (安装 Git 后会自带)。
下载 (克隆) 本项目
code
Bash
# 我们将项目下载到你的桌面上
cd ~/Desktop
git clone https://github.com/你的用户名/你的仓库名.git
(请将 你的用户名/你的仓库名 替换成你真实的 GitHub 地址)
进入项目文件夹
code
Bash
cd 你的仓库名
一键安装所有 Python 依赖
我们已经将所有需要的库都列在了 requirements.txt 文件里，你只需一条命令即可全部安装。
code
Bash
# 在 macOS 上:
pip3 install -r requirements.txt

# 在 Windows 上:
pip install -r requirements.txt
▶️ 启动与使用
安装完成！现在，让我们启动它。
在终端中（确保你还在项目文件夹内），运行：
code
Bash
# 在 macOS 上:
python3 voice_input.py

# 在 Windows 上:
python voice_input.py
看到 一切就绪！ 的提示后，保持这个终端窗口不要关闭。
切换到 Claude Code 或任何你想输入文字的地方。
按下 Ctrl + Shift + Space，你会听到系统提示音（或看到终端输出），表示录音开始。
说完你的指令后，再次按下 Ctrl + Shift + Space 停止录音。
稍等片刻，识别出的文字就会自动出现在你的光标位置！
🚑 问题排查指南
我们在这个项目的调试过程中遇到了很多“坑”，并把它们总结成了这份终极解决方案。
问题一：(macOS) 没反应或报错？终极权限解决方案
macOS 对权限管理极其严格。如果脚本没反应，99%是权限问题。你必须为“终端”程序授予全部三项权限。
打开 系统设置 -> 隐私与安全性。
在右侧列表中，依次找到并进入以下三项：
辅助功能 (Accessibility)
输入监视 (Input Monitoring)
麦克风 (Microphone)
在这每一个设置项中，通过 + 号，从“应用程序/实用工具”文件夹里，将“终端”(Terminal.app)添加进去，并确保它后面的开关是打开状态。
最关键的一步：修改完权限后，完全退出并重启你的终端程序，这样新的权限才会生效！
问题二：为什么识别结果为空或不准？麦克风终极解决方案
这个问题的根源是：脚本录到的是“一片寂静”或微弱的噪音。
检查你的系统默认麦克风
本脚本会自动使用你系统的默认输入设备。请在系统的“声音”设置里，确认你正在使用的麦克风（如 MacBook 内置麦克风）被设为默认，并且音量适中。
对着麦克风说话，观察设置里的输入音量条，它必须有明显的跳动！
警惕蓝牙耳机 (AirPods 等)
当你连接蓝牙耳机时，系统可能会自动将它设为默认麦克风。如果你此时并没有戴着耳机说话，脚本录到的自然是空声音。
解决方法：在进行语音输入时，要么确保你正对着蓝牙耳机的麦克风说话，要么暂时断开蓝牙连接，让系统切换回电脑的内置麦克风。
🎨 个性化定制
如何修改快捷键？
打开 voice_input.py 文件，找到这一行：
code
Python
HOTKEY_COMBINATION = {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.Key.space}
你可以修改成你喜欢的组合，例如 keyboard.Key.alt (Option 键) 或 keyboard.Key.cmd (Command 键)。
如何调整识别模型（速度 vs 准确度）？
打开 voice_input.py 文件，找到这一行：
code
Python
MODEL_SIZE = "small"
你可以根据你的需求和电脑性能进行调整：
"tiny" 或 "base": 速度最快，但准确度较低。
"small": (默认) 速度和准确度的最佳平衡点。
"medium": 准确度更高，尤其适合处理口音或嘈杂环境，但速度会慢一些。
"large": 准确度最高，但对电脑性能要求也最高。