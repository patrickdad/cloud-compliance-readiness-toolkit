from fastapi import FastAPI

from app.db import Base, engine
from app.routes import (
    control_mappings,
    controls,
    evidence,
    findings,
    frameworks,
    labs,
    project_controls,
    projects,
    remediation,
    crosswalk,
    dashboard,
    report,
    pdf_export,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Cloud Compliance Readiness Toolkit",
    version="0.1.0",
    description="A FastAPI toolkit for mapping compliance controls, labs, and project readiness.",
)

app.include_router(frameworks.router)
app.include_router(controls.router)
app.include_router(control_mappings.router)
app.include_router(projects.router)
app.include_router(project_controls.router)
app.include_router(labs.router)
app.include_router(evidence.router)
app.include_router(findings.router)
app.include_router(remediation.router)
app.include_router(crosswalk.router)
app.include_router(dashboard.router)
app.include_router(report.router)
app.include_router(pdf_export.router)


@app.get("/")
def healthcheck():
    return {"message": "Cloud Compliance Readiness Toolkit API is running"}