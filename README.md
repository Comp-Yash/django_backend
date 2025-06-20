# 📘 NotifyMe – A Django Backend Project with REST APIs, Celery Tasks & Telegram Bot Integration

---

## 🎯 Objective

To develop a scalable, secure, and functional backend system that demonstrates:

- REST API development with Django and Django REST Framework (DRF)
- Authentication via TokenAuth
- Background task execution using Celery and Redis
- Real-time user integration via a Telegram bot
- Production-ready settings and clean code organization

---

## ⚙️ Functional Overview

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Public & Protected APIs| Expose endpoints to retrieve or create user-specific reminders              |
| Authentication         | Token-based login for secure access                                        |
| Reminder Management    | Users can view and create reminders via API                                |
| Email Notification     | Users receive an email when a reminder is created (via Celery)             |
| Telegram Integration   | Users can link their Telegram account with their NotifyMe account           |
| Environment-Safe Config| `.env` file to manage secrets and production settings                      |

---

## 🏗️ Project Structure

```
notifyme/
├── core/               # DRF app with models, views, serializers, tasks
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tasks.py
│   └── urls.py
├── bot/                # Telegram bot integration
│   ├── bot_handler.py
│   └── telegram_utils.py
├── notifyme/           # Django project settings and celery integration
│   ├── settings.py
│   ├── urls.py
│   └── celery.py
├── .env                # Sample environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔐 Authentication

- Token-based authentication using `obtain_auth_token` from DRF
- Token is generated after login via `/api/login/`
- Protected endpoints (like `/api/reminders/`) require the token in the `Authorization` header

---

## 🧪 API Endpoints

| URL                    | Method | Auth Required | Purpose                                      |
|------------------------|--------|---------------|----------------------------------------------|
| `/api/public/`         | GET    | ❌ No          | Welcome public message                        |
| `/api/reminders/`      | GET    | ✅ Yes         | List user's reminders                         |
| `/api/reminders/`      | POST   | ✅ Yes         | Create a new reminder (triggers email)        |
| `/api/login/`          | POST   | ❌ No          | User login and token issuance                 |
| `/api-auth/login/`     | GET    | ✅ Optional    | Web login for DRF browsable API               |
| `/api/token/`, `/refresh/` | —  | Optional      | JWT endpoints (currently unused)              |

---

## 📨 Email Functionality (Celery)

- **Trigger**: After a user creates a reminder
- **Setup**:
  - SMTP backend (e.g., Gmail)
  - Celery worker:  
    ```bash
    celery -A notifyme worker --loglevel=info
    ```
  - Redis as the message broker
- **Task defined in**: `core/tasks.py`

---

## 🤖 Telegram Bot Functionality

- Created using `@BotFather` on Telegram
- When a user sends `/start`, the bot:
  - Retrieves `telegram_id` and `telegram_username`
  - Links with corresponding Django `User`
  - Saves in `TelegramProfile` model
- Bot logic is handled in `bot/bot_handler.py`

---

## 🛡️ Security Measures

- `.env` file managed using `python-decouple`
- `DEBUG=False` for production readiness
- `ALLOWED_HOSTS`, SMTP credentials hidden from codebase
- `.gitignore` excludes secrets, cache, and unnecessary files

---

## 📦 Deployment Readiness

- Fully modular app structure
- Portable `.env.example` for quick setup
- Easily containerizable with **Docker**
- Deployable on **Heroku**, **Render**, or **EC2** with Redis add-on

---

## 📂 Database Models

### 🔸 Reminder

| Field      | Type         | Description           |
|------------|--------------|-----------------------|
| user       | FK(User)     | Owner of reminder     |
| title      | CharField    | Title of the reminder |
| time       | DateTime     | When reminder is due  |
| created_at | DateTime     | Auto timestamp        |

### 🔸 TelegramProfile

| Field             | Type         | Description                 |
|------------------|--------------|-----------------------------|
| user             | OneToOne     | Linked Django user          |
| telegram_username| CharField    | Telegram username           |
| telegram_user_id | CharField    | Telegram ID from bot        |

---

## ✅ Assignment Requirement Checklist

| Requirement                            | Status     |
|----------------------------------------|------------|
| DRF Project Setup                      | ✅ Done     |
| Environment-safe production settings   | ✅ Done     |
| Token Authentication                   | ✅ Done     |
| Public & Protected Endpoints           | ✅ Done     |
| Celery Integration with Redis          | ✅ Done     |
| Background Task (Email sending)        | ✅ Done     |
| Telegram Bot `/start` with user linking| ✅ Done     |
| Clean modular code                     | ✅ Done     |

---

## 🚀 Future Extensions

- Use Telegram bot to send **reminder alerts** (via Celery scheduler)
- Add **JWT** login and refresh token endpoints
- Generate automatic API documentation with **Swagger/OpenAPI**
- Enable **Dockerized deployment**
- Extend reminders to include **categories**, **status**, or **recurrence**

