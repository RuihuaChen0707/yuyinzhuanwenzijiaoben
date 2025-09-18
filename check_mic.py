import sounddevice as sd

print("--- 可用的输入设备 ---")
print(sd.query_devices())

print("\n--- Python 当前默认使用的输入设备 ---")
default_device_index = sd.default.device[0]  # [0] is for input
default_device_info = sd.query_devices(default_device_index)
print(f"索引 (Index): {default_device_index}")
print(f"名称 (Name): {default_device_info['name']}")