import os
from io import BytesIO

import pandas as pd
import requests
import streamlit as st

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")

st.set_page_config(
    page_title="Cloud Compliance Readiness Toolkit",
    page_icon="🔐",
    layout="wide",
)


@st.cache_data(ttl=30)
def api_get(base_url: str, path: str):
    response = requests.get(f"{base_url}{path}", timeout=20)
    response.raise_for_status()
    return response.json()


@st.cache_data(ttl=30)
def get_projects(base_url: str):
    return api_get(base_url, "/projects")


@st.cache_data(ttl=30)
def get_dashboard(base_url: str, project_id: int):
    return api_get(base_url, f"/dashboard/project/{project_id}")


@st.cache_data(ttl=30)
def get_report(base_url: str, project_id: int):
    return api_get(base_url, f"/report/project/{project_id}")


@st.cache_data(ttl=30)
def get_crosswalk(base_url: str, control_id: int):
    return api_get(base_url, f"/crosswalk/control/{control_id}")


def get_pdf(base_url: str, project_id: int) -> BytesIO:
    response = requests.get(f"{base_url}/pdf-export/project/{project_id}", timeout=30)
    response.raise_for_status()
    return BytesIO(response.content)


def highlight_severity(val):
    if str(val).lower() == "critical":
        return "background-color: #7f1d1d; color: white"
    if str(val).lower() == "high":
        return "background-color: #b45309; color: white"
    if str(val).lower() == "medium":
        return "background-color: #1d4ed8; color: white"
    if str(val).lower() == "low":
        return "background-color: #166534; color: white"
    return ""


def highlight_status(val):
    status = str(val).lower()
    if status == "validated":
        return "background-color: #166534; color: white"
    if status == "implemented":
        return "background-color: #1d4ed8; color: white"
    if status == "in_progress":
        return "background-color: #b45309; color: white"
    if status == "gap_identified":
        return "background-color: #7f1d1d; color: white"
    if status == "not_started":
        return "background-color: #475569; color: white"
    return ""


st.markdown("""
<style>
.main-header {
    font-size: 36px;
    font-weight: 700;
    color: #0F172A;
}

.sub-header {
    font-size: 16px;
    color: #64748B;
    margin-bottom: 20px;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    background-color: #2563EB;
    color: white;
    border-radius: 6px;
    font-size: 12px;
    margin-right: 8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">🛡️ Cloud Compliance Readiness Toolkit</div>
<div class="sub-header">
Full-stack GRC platform for SOC 2, ISO 27001, and PCI DSS readiness
</div>

<span class="badge">FastAPI</span>
<span class="badge">Streamlit</span>
<span class="badge">GRC</span>
<span class="badge">Cloud Security</span>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Configuration")
    api_url = st.text_input("API Base URL", value=API_BASE_URL).rstrip("/")

    st.divider()
    st.subheader("Project Selection")

    try:
        projects = get_projects(api_url)
    except Exception as exc:
        st.error(f"Could not connect to FastAPI backend: {exc}")
        st.stop()

    if not projects:
        st.warning("No projects found. Create a project first in FastAPI Swagger.")
        st.stop()

    project_options = {
        f'{project["name"]} (ID: {project["id"]})': project["id"]
        for project in projects
    }

    selected_label = st.selectbox("Choose a project", list(project_options.keys()))
    selected_project_id = project_options[selected_label]

    st.divider()
    if st.button("Refresh Data", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

try:
    report = get_report(api_url, selected_project_id)
    dashboard = get_dashboard(api_url, selected_project_id)
except Exception as exc:
    st.error(f"Could not load project data: {exc}")
    st.stop()

project = report["project"]
controls = report["controls"]
evidence = report["evidence"]
findings = report["findings"]
remediation_tasks = report["remediation_tasks"]

header_left, header_right = st.columns([3, 1])

with header_left:
    st.subheader(project["project_name"])
    st.write(f'**Client:** {project["client_name"]}')
    st.write(f'**Status:** {project["status"]}')
    if project.get("description"):
        st.write(project["description"])

with header_right:
    try:
        pdf_buffer = get_pdf(api_url, selected_project_id)
        st.download_button(
            label="Download PDF Report",
            data=pdf_buffer,
            file_name=f"project_{selected_project_id}_readiness_report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    except Exception as exc:
        st.warning(f"PDF unavailable: {exc}")

metric1, metric2, metric3, metric4, metric5 = st.columns(5)
metric1.metric("Readiness %", dashboard["readiness_percentage"])
metric2.metric("Readiness Level", dashboard.get("readiness_level", "N/A"))
metric3.metric("Controls", dashboard["total_controls"])
metric4.metric("Open Findings", dashboard["open_findings"])
metric5.metric("Open Tasks", dashboard["open_remediation_tasks"])

st.progress(min(max(dashboard["readiness_percentage"] / 100, 0.0), 1.0))
st.caption(f'Readiness progress: {dashboard["readiness_percentage"]}%')

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Dashboard",
        "Controls",
        "Risk & Remediation",
        "Evidence",
        "Crosswalk",
    ]
)

with tab1:
    left, right = st.columns(2)

    with left:
        st.markdown("### Control Status Breakdown")
        status_df = pd.DataFrame(
            list(dashboard["control_status_breakdown"].items()),
            columns=["Status", "Count"],
        )
        st.bar_chart(status_df.set_index("Status"))
        st.dataframe(status_df, use_container_width=True, hide_index=True)

    with right:
        st.markdown("### Finding Severity Breakdown")
        severity_df = pd.DataFrame(
            list(dashboard["finding_severity_breakdown"].items()),
            columns=["Severity", "Count"],
        )
        st.bar_chart(severity_df.set_index("Severity"))
        st.dataframe(severity_df, use_container_width=True, hide_index=True)

    st.markdown("### Summary")
    st.write(
        f"This project currently has a **{dashboard.get('readiness_level', 'N/A')}** "
        f"readiness level with **{dashboard['evidence_count']}** evidence items, "
        f"**{dashboard['open_findings']}** open findings, and "
        f"**{dashboard['open_remediation_tasks']}** open remediation tasks."
    )

with tab2:
    st.markdown("### Controls in Scope")
    controls_df = pd.DataFrame(controls)

    if not controls_df.empty:
        preferred_columns = [
            "control_code",
            "control_title",
            "status",
            "validation_status",
            "readiness_score",
            "owner",
            "implementation_notes",
        ]
        available_columns = [c for c in preferred_columns if c in controls_df.columns]

        styled_controls = controls_df[available_columns].style.applymap(
            highlight_status,
            subset=[col for col in ["status", "validation_status"] if col in available_columns],
        )

        st.dataframe(styled_controls, use_container_width=True, hide_index=True)
    else:
        st.info("No controls found for this project.")

with tab3:
    critical_findings = [f for f in findings if str(f.get("severity", "")).lower() == "critical"]
    if critical_findings:
        st.error("⚠️ Critical Risks Identified")
        for finding in critical_findings:
            st.write(f'• {finding["title"]}')

    left, right = st.columns(2)

    with left:
        st.markdown("### Findings")
        findings_df = pd.DataFrame(findings)
        if not findings_df.empty:
            styled_findings = findings_df.style.applymap(
                highlight_severity,
                subset=["severity"] if "severity" in findings_df.columns else None,
            )
            st.dataframe(styled_findings, use_container_width=True, hide_index=True)
        else:
            st.info("No findings recorded.")

    with right:
        st.markdown("### Remediation Tasks")
        tasks_df = pd.DataFrame(remediation_tasks)
        if not tasks_df.empty:
            st.dataframe(tasks_df, use_container_width=True, hide_index=True)
        else:
            st.info("No remediation tasks recorded.")

with tab4:
    st.markdown("### Evidence Records")
    evidence_df = pd.DataFrame(evidence)
    if not evidence_df.empty:
        st.dataframe(evidence_df, use_container_width=True, hide_index=True)
    else:
        st.info("No evidence records found.")

with tab5:
    st.markdown("### Control Crosswalk Viewer")

    if controls:
        control_lookup = {
            f'{item["control_code"]} - {item["control_title"]}': item["control_id"]
            for item in controls
        }

        selected_control_label = st.selectbox(
            "Select a control",
            list(control_lookup.keys()),
            key="crosswalk_control_selector",
        )
        selected_control_id = control_lookup[selected_control_label]

        try:
            crosswalk = get_crosswalk(api_url, selected_control_id)
            st.write(f'**Control:** {crosswalk["control_code"]} - {crosswalk["control_title"]}')
            st.write(f'**Domain:** {crosswalk["control_domain"]}')

            mappings_df = pd.DataFrame(crosswalk["mappings"])
            if not mappings_df.empty:
                st.dataframe(mappings_df, use_container_width=True, hide_index=True)
            else:
                st.info("No mappings found for this control.")
        except Exception as exc:
            st.error(f"Could not load crosswalk: {exc}")
    else:
        st.info("No controls available for crosswalk view.")
