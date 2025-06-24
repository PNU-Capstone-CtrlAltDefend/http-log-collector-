import wmi #Win32 API 사용 라이브러리
from fluent import sender
from datetime import datetime
import time
from fluent.asyncsender import FluentSender

# Fluentd 엔드포인트 설정
logger =  FluentSender("usb.device", host="localhost", port=24226)

# 이벤트 전송 함수
def send_to_fluentd(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = {
        "timestamp": timestamp,
        "event": action
    }
    try:
        logger.emit("event",payload)
        print(f"[{timestamp}] {action} → Sent to Fluentd via forward")
    except Exception as e:
        print(f"[{timestamp}] {action} → Failed to send to Fluentd: {e}")

# USB 이벤트 감지 시작
def get_connected_usb_set():
    c = wmi.WMI()
    usb_devices = c.Win32_USBControllerDevice()
    return set(d.Dependent for d in usb_devices)

def monitor_usb():
    print("🔌 Monitoring USB device connections (based on controller state)...")
    prev_devices = get_connected_usb_set()

    while True:
        time.sleep(1)
        current_devices = get_connected_usb_set()

        inserted = current_devices - prev_devices
        removed = prev_devices - current_devices

        if inserted:
            send_to_fluentd("CONNECTED")
        if removed:
            send_to_fluentd("DISCONNECTED")

        prev_devices = current_devices

if __name__ == "__main__":
    monitor_usb()
