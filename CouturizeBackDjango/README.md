# Couturize Backend (Django) | Бэкенд Couturize (Django)

## 🇷🇺 Русский

### О проекте
Бэкенд часть приложения Couturize, разработанная с использованием Django и Django REST Framework.

### Требования
- Python 3.8 или выше
- pip (менеджер пакетов Python)
- virtualenv или venv

### Установка и запуск
1. Создайте виртуальное окружение:
```bash
python -m venv venv
```

2. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Запустите сервер разработки:
```bash
python manage.py runserver
```

### Структура проекта
- `authentication/` - Приложение аутентификации
- `api/` - API endpoints
- `models/` - Модели данных
- `services/` - Бизнес-логика
- `utils/` - Вспомогательные функции
- `tests/` - Тесты

### API Документация
Подробная документация API доступна в файле [API_DOCUMENTATION.md](./API_DOCUMENTATION.md).

---

## 🇬🇧 English

### About
The backend part of the Couturize application, developed using Django and Django REST Framework.

### Requirements
- Python 3.8 or higher
- pip (Python package manager)
- virtualenv or venv

### Installation and Running
1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Run development server:
```bash
python manage.py runserver
```

### Project Structure
- `authentication/` - Authentication application
- `api/` - API endpoints
- `models/` - Data models
- `services/` - Business logic
- `utils/` - Helper functions
- `tests/` - Tests

### API Documentation
Detailed API documentation is available in [API_DOCUMENTATION.md](./API_DOCUMENTATION.md).

## Project Setup

### Prerequisites
- Python 3.8+
- Django 3.2+
- pip

### Installation
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup
1. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Load initial body type data:
   ```bash
   python manage.py loaddata body_type/fixtures/initial_data.json
   ```

### Running the Server
```bash
python manage.py runserver
```

## Body Type Models
The project includes models for:
- Body Types
- Clothing Recommendations
- User Profiles

Each body type has associated clothing recommendations and can be used to provide personalized style advice.

## API Endpoints and Testing

### Authentication Endpoints
- **Register**: `POST /api/auth/register/`
  - Required fields: `username`, `email`, `first_name`, `last_name`, `password`, `password2`
  - Creates a user and associated UserProfile

- **Login**: `POST /api/token/`
  - Required fields: `username`, `password`
  - Returns access and refresh tokens

- **User Details**: `GET /api/auth/user/`
  - Requires authentication
  - Returns user profile information

### Body Type and Recommendations Endpoints
- **List Body Types**: `GET /api/body-types/`
  - Returns list of all body types

- **Clothing Recommendations**: `GET /api/recommendations/by_body_type/`
  - Query parameter: `body_type_id`
  - Returns clothing recommendations for a specific body type

- **User Profile**:
  - `GET /api/profile/my_profile/`: Get current user's profile
  - `PATCH /api/profile/update_measurements/`: Update user measurements

### Troubleshooting

### Common Registration Errors

#### IntegrityError: UNIQUE constraint failed
- Occurs when trying to create a user profile for an existing user
- Solution: 
  - Use `get_or_create()` method
  - Check for existing users before registration
  - Ensure unique username constraints are followed

#### Validation Errors
- Ensure all required fields are provided
- Password must match confirmation password
- Email and username must be unique

### Debugging Registration
1. Check server logs for specific error messages
2. Verify request payload matches required fields
3. Use Django Debug Toolbar for detailed error insights
