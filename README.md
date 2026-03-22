# 🛡️ Cloud Compliance Readiness Toolkit

A portfolio-ready **FastAPI + Streamlit** application designed to simulate how organisations assess cloud compliance readiness across frameworks such as **SOC 2, ISO/IEC 27001, and PCI DSS**.

---

## 🚀 Overview

This toolkit models the full lifecycle of a cloud compliance assessment, including:

- Control implementation tracking  
- Evidence collection  
- Risk identification (findings)  
- Remediation task management  
- Readiness scoring and dashboard reporting  
- Cross-framework control mapping  
- PDF report generation  

The goal is to demonstrate practical understanding of **GRC (Governance, Risk & Compliance)** workflows used in real-world cyber assurance engagements.

---

## 🧠 Key Features

### 🔹 Project-Based Assessments
Create and manage compliance readiness assessments for SaaS or cloud environments.

### 🔹 Control Lifecycle Management
Track controls through:
- Not Started  
- In Progress  
- Implemented  
- Validated  
- Gap Identified  

### 🔹 Evidence Tracking
Attach and manage audit evidence such as:
- Cloud configuration exports  
- Screenshots  
- System logs  

### 🔹 Findings & Risk Management
Identify and classify risks by severity:
- Low / Medium / High / Critical  

### 🔹 Remediation Workflow
Assign and track remediation tasks with:
- Priority  
- Ownership  
- Status  

### 🔹 Dashboard Reporting
Visualise:
- Readiness percentage  
- Control status breakdown  
- Risk distribution  
- Open remediation workload  

### 🔹 Cross-Framework Mapping
Map controls across:
- SOC 2  
- ISO/IEC 27001  
- PCI DSS  

### 🔹 PDF Report Export
Generate consultant-style readiness reports for stakeholders.

---

## 🖥️ Frontend Dashboard (Streamlit)

Interactive dashboard for:
- Viewing project readiness  
- Monitoring risks and remediation  
- Exploring control mappings  
- Downloading PDF reports  

---

## 🏗️ Tech Stack

| Layer        | Technology |
|-------------|------------|
| Backend API | FastAPI |
| Database    | SQLite + SQLAlchemy |
| Frontend    | Streamlit |
| Reporting   | ReportLab |
| Data Handling | Pandas |
| HTTP Client | Requests |

---

## 📂 Project Structure
cloud-compliance-readiness-toolkit/
├── app/
│ ├── models/
│ ├── routes/
│ ├── services/
│ ├── db.py
│ └── main.py
├── docs/
│ ├── sample-report.pdf
│ └── screenshots/
├── streamlit_app.py
├── requirements.txt
└── README.md
---

## 📸 Screenshots

> 📌 Add your screenshots to `docs/screenshots/` and update the filenames below

### Dashboard
![Dashboard](docs/screenshots/dashboard.png)

### Risk & Remediation
![Findings](docs/screenshots/findings.png)

### Controls View
![Controls](docs/screenshots/controls.png)

### Crosswalk Mapping
![Crosswalk](docs/screenshots/crosswalk.png)

### PDF Report
![PDF](docs/screenshots/pdf.png)

---

## 📄 Sample Report

Download a generated readiness report:

👉 [Sample PDF Report](docs/sample-report.pdf)

---
## ⚙️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start FastAPI backend
```bash
uvicorn app.main:app --reload
```

### 3. Launch Streamlit frontend
```bash
streamlit run streamlit_app.py
```
---
## 🎯 Learning Outcomes

This project demonstrates:

Practical GRC workflow implementation
Control-based risk assessment methodology
Evidence-driven assurance
API-driven architecture design
Reporting and stakeholder communication
---
## 🚀 Future Enhancements
* AWS integration (CloudTrail, IAM, S3 checks)
* Automated evidence ingestion
* Role-based access control (RBAC)
* Multi-project analytics dashboard
* React-based frontend
---

👤 Author

Patrick Adefowora
Cyber Risk & Assurance | ISO 27001 | SOC 2 | Cloud Security