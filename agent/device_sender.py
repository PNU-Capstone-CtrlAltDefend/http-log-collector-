import wmi #Win32 API 사용 라이브러리
import requests
from datetime import datetime

# Fluentd 엔드포인트 설정
FLUENTD_URL = "http://localhost:9880/usb.device"

# 이벤트 전송 함수
def send_to_fluentd(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = {
        "timestamp": timestamp,
        "event": action
    }
    try:
        response = requests.post(FLUENTD_URL, json=payload)
        print(f"[{timestamp}] {action} → Sent to Fluentd (Status: {response.status_code})")
    except Exception as e:
        print(f"[{timestamp}] {action} → Failed to send to Fluentd: {e}")

# USB 이벤트 감지 시작
def monitor_usb():
    c = wmi.WMI()
    watcher_insert = c.Win32_VolumeChangeEvent.watch_for(notification_type="Creation")
    watcher_remove = c.Win32_VolumeChangeEvent.watch_for(notification_type="Deletion")

    print("🔌 USB 연결/해제 감시 시작 중... (Ctrl+C 종료)")
    while True:
        try:
            insert_event = watcher_insert(timeout_ms=500)
            #if insert_event:
            #    send_to_fluentd("CONNECTED")
        except wmi.x_wmi_timed_out:
            pass

        try:
            remove_event = watcher_remove(timeout_ms=500)
            #if remove_event:
            #    send_to_fluentd("DISCONNECTED")
        except wmi.x_wmi_timed_out:
            pass

if __name__ == "__main__":
    monitor_usb()
