# URL Shortener API

Этот проект представляет собой HTTP-сервис на FastAPI, который позволяет сокращать URL, получать оригинальные ссылки по их сокращённым версиям и выполнять асинхронные HTTP-запросы. Это тестовое задание было выполнено Владиславом Лахтионовым (@vladelo) для стажировку по направлению Backend Developer в 5D Hub. Readme.md файл был сгенерирован нейросетью)

## Установка и запуск

### 1. Установка зависимостей
Создайте виртуальное окружение (рекомендуется) и установите необходимые библиотеки:

```bash
python3 -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate  # Для Windows

pip install fastapi uvicorn httpx
```

### 2. Запуск сервера
```bash
uvicorn app:app --reload
```
Сервер будет запущен на `http://127.0.0.1:8000`.

## Использование API

### 1. Сократить URL
**POST /**  
Отправьте JSON-запрос с URL для сокращения:

```json
{
    "url": "https://example.com"
}
```

**Ответ (201 Created):**
```json
{
    "shortened_url": "http://127.0.0.1:8080/1"
}
```

### 2. Получить оригинальный URL
**GET /{short_url_id}**  
Отправьте запрос с идентификатором сокращенного URL.

**Пример запроса:**
```bash
curl -X GET http://127.0.0.1:8080/1
```

**Ответ (307 Redirect):**
```json
{
    "Location": "https://example.com"
}
```

### 3. Выполнить асинхронный HTTP-запрос
**GET /async-request**  
Этот эндпоинт делает асинхронный запрос к внешнему API.

**Пример запроса:**
```bash
curl -X GET http://127.0.0.1:8080/async-request
```

**Ответ (JSON-данные):**
```json
{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
}
```

## Документация API
После запуска сервера документация доступна по адресу:  
📄 **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
📄 **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Лицензия
Проект распространяется под лицензией MIT.
