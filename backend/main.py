from app.main import app

if _name_ == "main":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)