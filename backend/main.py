from fastapi import FastAPI


app = FastAPI(
    title="Finance Dashboard API",
    description="Finance Data Processing and Access Control System",
    version="1.0.0",
    lifespan=lifespan,
)