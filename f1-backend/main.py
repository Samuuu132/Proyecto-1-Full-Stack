from fastapi import FastAPI

app = FastAPI(
    title="F1 Drivers API",
    description="API para gestionar corredores de Fórmula 1",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "F1 Drivers API funcionando"}