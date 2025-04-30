# Test Task Python

## Описание
Простой CRUD API для управления пользователями на FastAPI с поддержкой репозиториев `memory` и `database` (PostgreSQL, sqlite).

## Установка
1. Клонируйте репозиторий:
   ```cmd
   git clone https://github.com/Shauremi/test-task-python.git
   cd test-task-python
   ```
2. Создайте виртуальное окружение и активируйте его:
   ```cmd
   python -m venv venv
   venv\\Scripts\\activate.bat
   ```
3. Установите зависимости:
   ```cmd
   pip install -r requirements.txt
   ```
4. Создайте файл `.env` в корне проекта:
   ```env
   REPOSITORY_TYPE=memory   # или database
   DB_URL=postgresql+psycopg2://user:password@localhost:5432/dbname # или для sqlite DB_URL=sqlite:///:memory:
   ```

## Запуск
```cmd
uvicorn src.main:app --reload --port 8000
```
## Доступ к документации
Чтобы получить доступ к документации по автоматическому API, просто перейдите в раздел http://127.0.0.1:8000/docs в веб-браузере. На этой странице будет отображаться интерактивная документация, созданная FastAPI, позволяющая увидеть доступные эндпоинты и их параметры.

![image](https://github.com/user-attachments/assets/4a736e87-a51d-4e99-b781-9393ecd929ff)

## Примеры запросов
- **Создание пользователя**:
  ```cmd
  curl -X POST "http://127.0.0.1:8000/users/" \
    -H "Content-Type: application/json" \
    -d '{"fullname":"Alice"}'
  ```
- **Получение списка пользователей**:
  ```cmd
  curl "http://127.0.0.1:8000/users/"
  ```
- **Получение пользователя**:
  ```cmd
  curl "http://127.0.0.1:8000/users/{id}"
  ```
- **Обновление пользователя**:
  ```cmd
  curl -X PUT "http://127.0.0.1:8000/users/{id}" \
    -H "Content-Type: application/json" \
    -d '{"fullname":"Alice Updated"}'
  ```
- **Удаление пользователя**:
  ```cmd
  curl -X DELETE "http://127.0.0.1:8000/users/{id}"
  ```

