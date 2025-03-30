# Сделано Владиславом Лахтионовым (@vladelo)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

# Создаем экземпляр FastAPI
app = FastAPI()

# Хранилище для сопоставления коротких и длинных URL
url_store = {}
shortened_urls = {}


# Описание модели входного запроса с URL
class URLRequest(BaseModel):
    url: str


# Эндпоинт для сокращения URL
@app.post("/", status_code=201)
async def shorten_url(request: URLRequest):
    """
    Принимает URL в теле запроса и возвращает укороченную версию.
    """
    short_id = str(len(url_store) + 1)  # Генерируем уникальный идентификатор
    url_store[short_id] = request.url  # Сохраняем в словарь по этому ID
    shortened_urls[request.url] = short_id  # Обратное сопоставление (необязательно)
    return {"shortened_url": f"http://127.0.0.1:8080/{short_id}"}  # Возвращаем короткий URL


# Эндпоинт для получения оригинального URL по короткому идентификатору
@app.get("/{shorten_url_id}", status_code=307)
async def redirect_to_url(shorten_url_id: str):
    """
    Получает короткий идентификатор и возвращает оригинальный URL.
    Если идентификатор не найден, возвращает ошибку 404.
    """
    original_url = url_store.get(shorten_url_id)  # Ищем URL по идентификатору
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")  # Если не найдено, возвращаем 404
    return {"Location": original_url}  # Возвращаем оригинальный URL


# Эндпоинт для выполнения асинхронного HTTP-запроса
@app.get("/async-request")
async def async_request():
    """
    Выполняет асинхронный запрос к тестовому API и возвращает полученные данные.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get('https://jsonplaceholder.typicode.com/todos/1')  # Делаем запрос к внешнему API
        return response.json()  # Возвращаем JSON-ответ
