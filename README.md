# HTTP Log Collector

이 리포지터리는 사용자 PC에서 발생하는 HTTP 요청 로그를 수집하여 중앙 서버로 전송하는 데몬 서비스입니다.  
FastAPI 서버와 연동되며, 로그는 Fluentd를 통해 POST 방식으로 전송됩니다. 

## 📁 디렉토리 구조
http-log-collector/
├── fluent.conf # Fluentd 설정 파일 //
├── scripts/
│ └── install.sh # 초기 설치 스크립트 //
├── examples/
│ └── sample-log.json # 샘플 로그 예시 //
└── README.md

### 📄 로그 필드 정의
| 필드 이름     | 설명                     | 예시                              |
|---------------|--------------------------|-----------------------------------|
| 로그 ID       | 고유한 로그 식별자       | `log_00123`                       |
| 사용자 ID     | 로그를 생성한 사용자 ID  | `user_456`                        |
| 날짜          | 요청 발생 시각 (ISO 8601) | `2025-05-17 10:32:11`             |
| URL           | 요청된 경로              | `/login`                          |
| Contents      | 요청 내용 요약 또는 바디 | `POST /login with payload {...}` |
