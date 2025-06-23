from mitmproxy import http
from fluent import sender, event
import urllib.parse
import datetime
import re

# Fluentd 설정
sender.setup('fluentd.webmail', host='localhost', port=24225)

def strip_html_tags(html):
    html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL)
    html = re.sub(r'<.*?>', '', html)
    return html.strip()

def request(flow: http.HTTPFlow):
    if "mail.naver.com" in flow.request.pretty_url and "/json/write/send" in flow.request.path:
        try:
            content = flow.request.get_text()
            data = urllib.parse.parse_qs(content)
            raw_body = data.get("body", [""])[0]
            decoded_body = urllib.parse.unquote(raw_body)

            log = {
                "timestamp": datetime.datetime.now().isoformat(),
                "from": data.get('senderAddress', [""])[0],
                "to": [x for x in data.get("to", [""])[0].split(";") if x.strip()],
                "cc": [x for x in data.get("cc", [""])[0].split(";") if x.strip()],
                "bcc": [x for x in data.get("bcc", [""])[0].split(";") if x.strip()],
                "subject": data.get("subject", [""])[0],
                "content": strip_html_tags(decoded_body),
                "attachment_count": data.get("attachCount", ["0"])[0],
                "email_size": len(content)
            }

            event.Event('webmail', log)

        except Exception as e:
            print("Error parsing email:", e)
