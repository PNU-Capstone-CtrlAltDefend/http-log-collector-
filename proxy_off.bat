@echo off
:: 프록시 OFF - 사용 안 함
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f
echo [🛑] 프록시가 비활성화되었습니다.