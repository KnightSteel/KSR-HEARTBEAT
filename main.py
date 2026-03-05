from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(title="KSR-HEARTBEAT")

# Montamos carpetas de activos
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Esta es la primera luz que ella verá
    return templates.TemplateResponse(
        "index.html", {"request": request, "status": "SISTEMA BENDECIDO"}
    )


if __name__ == "__main__":
    # Nos movemos al puerto 9999: Frecuencia libre para el Caballero
    uvicorn.run(app, host="0.0.0.0", port=9999)
