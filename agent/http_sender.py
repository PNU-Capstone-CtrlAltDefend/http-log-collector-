
from fluent import sender, event
from mitmproxy import http
import traceback
from datetime import datetime
# Fluentd 설정
sender.setup('fluentd.http', host='localhost', port=24224)

def request(flow: http.HTTPFlow):
    try:
        body = flow.request.get_text(strict=False)
    except:
        body = "<unreadable>"
    current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    log_data = {
        "date": current_time,
        "url": flow.request.pretty_url
    }

    try:
        event.Event('http_request', log_data)  # 태그: fluentd.http.http_request
        print(f"Http log sent successfully")
    except Exception as e:
        print(f"Http log sent failed")
        print(traceback.format_exc())
