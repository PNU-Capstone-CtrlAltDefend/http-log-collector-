# HTTP Log Collector

이 프로그램은 사용자 PC에서 발생하는 HTTP 요청, Email 전송, 로그온/로그오프, 디바이스 연결, 파일 복사 이벤트를 감지하고 로그를 전송하는 서비스입니다.
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
