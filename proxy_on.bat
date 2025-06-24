@echo off
:: 프록시 ON - 127.0.0.1:8080 사용
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d 127.0.0.1:8080 /f
echo [✅] 프록시 설정이 127.0.0.1:8080으로 활성화되었습니다.
