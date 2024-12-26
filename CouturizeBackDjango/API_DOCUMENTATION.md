# API Documentation | API Документация

## 🇷🇺 Русский

### Общая информация
API построено с использованием Django REST Framework и следует принципам RESTful.

### Аутентификация
Все запросы к API должны включать токен аутентификации в заголовке:
```
Authorization: Bearer <your_token>
```

### Endpoints

#### Аутентификация

##### Регистрация
- **URL**: `/api/auth/register/`
- **Метод**: `POST`
- **Тело запроса**:
  ```json
  {
    "email": "user@example.com",
    "password": "secure_password",
    "username": "username"
  }
  ```
- **Ответ**: `201 Created`

##### Вход
- **URL**: `/api/auth/login/`
- **Метод**: `POST`
- **Тело запроса**:
  ```json
  {
    "email": "user@example.com",
    "password": "secure_password"
  }
  ```
- **Ответ**: `200 OK`
  ```json
  {
    "token": "your_auth_token"
  }
  ```

#### Профиль пользователя

##### Получить мой профиль
- **URL**: `/api/profiles/my_profile/`
- **Метод**: `GET`
- **Аутентификация**: Токен аутентификации обязателен
- **Ответ**: `200 OK`

##### Обновить измерения профиля
- **URL**: `/api/profiles/update_measurements/`
- **Метод**: `PATCH`
- **Аутентификация**: Токен аутентификации обязателен
- **Тело запроса**:
  ```json
  {
    "chest": "number",
    "waist": "number", 
    "hips": "number",
    "height": "number"
  }
  ```
- **Ответ**: `200 OK`

#### Типы телосложения

##### Список типов телосложения
- **URL**: `/api/body-types/`
- **Метод**: `GET`
- **Параметры запроса**:
  - `body_type_id`: Фильтровать по конкретному типу телосложения
- **Аутентификация**: Необязательна
- **Ответ**: `200 OK`

##### Получить рекомендации по одежде
- **URL**: `/api/recommendations/`
- **Метод**: `GET`
- **Параметры запроса**:
  - `body_type_id`: Фильтровать рекомендации по типу телосложения
- **Аутентификация**: Токен аутентификации обязателен
- **Ответ**: `200 OK`

---

## 🇬🇧 English

### General Information
The API is built using Django REST Framework and follows RESTful principles.

### Authentication
All API requests must include an authentication token in the header:
```
Authorization: Bearer <your_token>
```

### Endpoints

#### Authentication

##### Register
- **URL**: `/api/auth/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "secure_password",
    "username": "username"
  }
  ```
- **Response**: `201 Created`

##### Login
- **URL**: `/api/auth/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "secure_password"
  }
  ```
- **Response**: `200 OK`
  ```json
  {
    "token": "your_auth_token"
  }
  ```

#### User Profile

##### Get My Profile
- **URL**: `/api/profiles/my_profile/`
- **Method**: `GET`
- **Authentication**: Bearer Token Required
- **Response**: `200 OK`

##### Update Profile Measurements
- **URL**: `/api/profiles/update_measurements/`
- **Method**: `PATCH`
- **Authentication**: Bearer Token Required
- **Request Body**:
  ```json
  {
    "chest": "number",
    "waist": "number", 
    "hips": "number",
    "height": "number"
  }
  ```
- **Response**: `200 OK`

#### Body Types

##### List Body Types
- **URL**: `/api/body-types/`
- **Method**: `GET`
- **Query Parameters**:
  - `body_type_id`: Filter by specific body type ID
- **Authentication**: Optional
- **Response**: `200 OK`

##### Get Clothing Recommendations
- **URL**: `/api/recommendations/`
- **Method**: `GET`
- **Query Parameters**:
  - `body_type_id`: Filter recommendations by body type
- **Authentication**: Bearer Token Required
- **Response**: `200 OK`

## Authentication

### JWT Token Flow
1. Register user
2. Login to receive access and refresh tokens
3. Use access token for authenticated requests
4. Use refresh token to obtain new access token when expired

## Support
For any issues or questions, please contact our support team.
skobelkin.zahar@gmail.com