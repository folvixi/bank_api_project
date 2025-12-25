# 🏦 Bank API - Django REST Framework

Простое RESTful API для кредитного банка с полной аутентификацией JWT, документацией Swagger и поддержкой CRUD операций.

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.8 или выше
- pip (менеджер пакетов Python)

### Установка за 5 минут

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/folvixi/bank_api_project.git

```

2. **Создайте виртуальное окружение**
```bash
python -m venv venv
```

3. **Активируйте окружение**
- **Windows:**
```bash
venv\Scripts\activate
```
- **Mac/Linux:**
```bash
source venv/bin/activate
```

4. **Установите зависимости**
```bash
pip install -r requirements.txt
```

5. **Настройте базу данных**
```bash
python manage.py migrate
```

6. **Создайте администратора**
```bash
python manage.py createsuperuser
```
Введите:
- Username: `admin`
- Password: `admin123` (или любой другой)

7. **Добавьте тестовые данные**
```bash
python create_test_data.py
```

8. **Запустите сервер**
```bash
python manage.py runserver
```

9. **Откройте в браузере**
- Документация: http://127.0.0.1:8000/api/swagger/
- Админка: http://127.0.0.1:8000/admin/

## 📚 API Документация

### Swagger UI
Полная интерактивная документация доступна по адресу:
**http://127.0.0.1:8000/api/swagger/**

#### Как использовать Swagger:
1. Откройте http://127.0.0.1:8000/api/swagger/
2. Найдите раздел "Auth" → `POST /api/token/`
3. Нажмите "Try it out"
4. Введите:
```json
{
  "username": "admin",
  "password": "admin123"
}
```
5. Нажмите "Execute"
6. Скопируйте `access` токен из ответа
7. Нажмите кнопку **"Authorize"** вверху справа
8. Введите: `Bearer ваш_токен`
9. Теперь можете тестировать все эндпоинты!

### ReDoc
Альтернативная документация: http://127.0.0.1:8000/api/redoc/

## 🔐 Аутентификация

### Получение JWT токена
```bash
POST /api/token/
Content-Type: application/json

{
    "username": "admin",
    "password": "admin123"
}
```

### Ответ
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Обновление токена
```bash
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "ваш_refresh_токен"
}
```

### Использование токена
Добавьте заголовок к каждому запросу:
```
Authorization: Bearer ваш_access_токен
```

## 📊 Эндпоинты API

### 👥 Клиенты
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/clients/` | Список всех клиентов |
| POST | `/api/clients/` | Создать нового клиента |
| GET | `/api/clients/{id}/` | Получить клиента по ID |
| PUT | `/api/clients/{id}/` | Обновить клиента |
| PATCH | `/api/clients/{id}/` | Частично обновить клиента |
| DELETE | `/api/clients/{id}/` | Удалить клиента |

### 💰 Кредиты
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/loans/` | Список всех кредитов |
| POST | `/api/loans/` | Создать новый кредит |
| GET | `/api/loans/{id}/` | Получить кредит по ID |
| PUT | `/api/loans/{id}/` | Обновить кредит |
| DELETE | `/api/loans/{id}/` | Удалить кредит |

### 🏦 Вклады
| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/deposits/` | Список всех вкладов |
| POST | `/api/deposits/` | Создать новый вклад |
| GET | `/api/deposits/{id}/` | Получить вклад по ID |
| PUT | `/api/deposits/{id}/` | Обновить вклад |
| DELETE | `/api/deposits/{id}/` | Удалить вклад |

## 📝 Примеры запросов

### Создание клиента
```bash
POST /api/clients/
Authorization: Bearer ваш_токен
Content-Type: application/json

{
    "full_name": "Иванов Иван Иванович",
    "birth_date": "1990-05-15",
    "passport": "4501-123456",
    "phone": "+79161234567"
}
```

### Создание кредита
```bash
POST /api/loans/
Authorization: Bearer ваш_токен
Content-Type: application/json

{
    "client": 1,
    "amount": "250000.00",
    "interest_rate": "12.50",
    "term_months": 24,
    "start_date": "2024-01-20",
    "status": "active",
    "monthly_payment": "12500.00"
}
```

### Создание вклада
```bash
POST /api/deposits/
Authorization: Bearer ваш_токен
Content-Type: application/json

{
    "client": 1,
    "amount": "100000.00",
    "interest_rate": "7.50",
    "term_months": 12,
    "start_date": "2024-01-20",
    "status": "active"
}
```

### Пагинация
Все списковые эндпоинты поддерживают пагинацию:
```
GET /api/clients/?page=2
```
Ответ включает:
```json
{
    "count": 50,
    "next": "http://localhost:8000/api/clients/?page=3",
    "previous": "http://localhost:8000/api/clients/?page=1",
    "results": [...]
}
```

## 🗄️ Модели данных

### Клиент (Client)
```json
{
    "id": 1,
    "full_name": "Иванов Иван",
    "birth_date": "1990-01-01",
    "passport": "1234-567890",
    "phone": "+79161234567",
    "created_at": "2024-01-15T10:30:00Z"
}
```

### Кредит (Loan)
```json
{
    "id": 1,
    "client": 1,
    "amount": "100000.00",
    "interest_rate": "10.50",
    "term_months": 12,
    "start_date": "2024-01-15",
    "status": "active",
    "monthly_payment": "10000.00"
}
```

### Вклад (Deposit)
```json
{
    "id": 1,
    "client": 1,
    "amount": "50000.00",
    "interest_rate": "5.50",
    "term_months": 6,
    "start_date": "2024-01-15",
    "status": "active"
}
```

## 🛠️ Команды управления

```bash
# Запуск сервера
python manage.py runserver

# Создание миграций при изменении моделей
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Создание нового администратора
python manage.py createsuperuser

# Запуск скрипта тестовых данных
python create_test_data.py

# Деактивация виртуального окружения
deactivate
```



### Настройки безопасности
- JWT access токен: 60 минут
- JWT refresh токен: 1 день
- Все эндпоинты требуют аутентификации
- CSRF защита отключена для API (стандартно для REST API)

### Особенности реализации
- Автоматическая генерация CRUD операций через ViewSets
- Пагинация по умолчанию: 10 записей на страницу
- Полная документация OpenAPI 3.0
- Готово к интеграции с React/Vue.js/мобильными приложениями

## 🚀 Интеграция с фронтендом

### Пример на JavaScript (fetch)
```javascript
// Получение токена
async function login(username, password) {
    const response = await fetch('http://localhost:8000/api/token/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username, password})
    });
    return await response.json();
}

// Получение списка клиентов
async function getClients(token) {
    const response = await fetch('http://localhost:8000/api/clients/', {
        headers: {'Authorization': `Bearer ${token}`}
    });
    return await response.json();
}

// Создание нового клиента
async function createClient(token, clientData) {
    const response = await fetch('http://localhost:8000/api/clients/', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(clientData)
    });
    return await response.json();
}
```

### Пример на Python (requests)
```python
import requests

# Получение токена
response = requests.post('http://localhost:8000/api/token/', 
    json={'username': 'admin', 'password': 'admin123'})
token = response.json()['access']

# Получение клиентов
headers = {'Authorization': f'Bearer {token}'}
clients = requests.get('http://localhost:8000/api/clients/', headers=headers).json()
```

## 🐛 Устранение неполадок

### Ошибка: "Authentication credentials were not provided"
- Получите новый JWT токен через `/api/token/`
- Добавьте заголовок `Authorization: Bearer ваш_токен`

### Ошибка: "Invalid token"
- Токен истек (действует 60 минут)
- Получите новый токен или обновите через `/api/token/refresh/`

### Ошибка: "Table doesn't exist"
```bash
python manage.py migrate
python manage.py makemigrations
```

### Сервер не запускается (порт занят)
```bash
# Используйте другой порт
python manage.py runserver 8001
```

### Ошибка импорта модулей
```bash
# Активируйте виртуальное окружение
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Переустановите зависимости
pip install -r requirements.txt
```


## ✅ Проверка требований задания

- [x] **3 связанные таблицы** - Client, Loan, Deposit
- [x] **JWT аутентификация** - через djangorestframework-simplejwt
- [x] **Пагинация** - на всех списковых эндпоинтах
- [x] **Swagger документация** - с кнопкой "Authorize"
- [x] **CRUD операции** - для всех моделей через ViewSets
- [x] **Готовность к фронтенду** - JSON API, CORS при необходимости


**Запуск проекта:** `python manage.py runserver`  
**Документация:** http://127.0.0.1:8000/api/swagger/  
**Админка:** http://127.0.0.1:8000/admin/