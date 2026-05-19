from fastapi import FastAPI

app = FastAPI(
    title="EKS GitOps Platform App",
    version="0.1.0",
    description="Sample FastAPI service for GitOps deployment on Amazon EKS.",
)


@app.get("/")
def read_root():
    return {"message": "Hello from the EKS GitOps Platform App"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": "0.1.0"}
