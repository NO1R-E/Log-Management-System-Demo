### Basic Commands

```
uvicorn app.main:app --reload
docker compose down
docker compose up -d
```

```
LogManagement
├─ .pytest_cache
│  ├─ CACHEDIR.TAG
│  ├─ README.md
│  └─ v
│     └─ cache
│        ├─ lastfailed
│        └─ nodeids
├─ backend
│  ├─ .pytest_cache
│  │  ├─ CACHEDIR.TAG
│  │  ├─ README.md
│  │  └─ v
│  │     └─ cache
│  │        └─ nodeids
│  ├─ app
│  │  ├─ api
│  │  │  └─ ingest.py
│  │  ├─ core
│  │  │  ├─ config.py
│  │  │  ├─ database.py
│  │  │  ├─ init_db.sql
│  │  │  └─ log_writer.py
│  │  ├─ main.py
│  │  ├─ normalizers
│  │  │  ├─ ad_norm.py
│  │  │  ├─ api_norm.py
│  │  │  ├─ aws_norm.py
│  │  │  ├─ m365_norm.py
│  │  │  ├─ syslog_norm.py
│  │  │  └─ __init__.py
│  │  ├─ schemas
│  │  │  └─ log.py
│  │  └─ __init__.py
│  ├─ pytest.ini
│  ├─ requirements.txt
│  └─ tests
│     ├─ unit
│     │  ├─ test_normalize_ad.py
│     │  ├─ test_normalize_api.py
│     │  ├─ test_normalize_aws.py
│     │  ├─ test_normalize_m365.py
│     │  ├─ test_normalize_syslog.py
│     │  └─ __init__.py
│     └─ __init__.py
├─ docker-compose.yml
├─ docs
├─ frontend
├─ ingest
├─ README.md
├─ samples
└─ testAPI.http

```