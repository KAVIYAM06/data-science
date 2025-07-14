from fastapi import FastAPI
from controllers.linkedin_controller import router

app = FastAPI(title="LinkedIn Stealth Automation API")
app.include_router(router, prefix="/linkedin")