from app.db import Base, SessionLocal, engine
from app.models.control import Control
from app.models.control_mapping import ControlMapping
from app.models.framework import Framework
from app.models.lab import Lab

Base.metadata.create_all(bind=engine)


def seed():
    db = SessionLocal()

    if db.query(Framework).count() == 0:
        frameworks = [
            Framework(name="SOC 2", version="2022", description="SOC 2 readiness framework"),
            Framework(name="ISO 27001", version="2022", description="ISO 27001 ISMS readiness framework"),
            Framework(name="PCI DSS", version="4.0.1", description="PCI DSS compliance readiness framework"),
        ]
        db.add_all(frameworks)

    if db.query(Control).count() == 0:
        controls = [
            Control(
                control_code="AC-01",
                title="Multi-Factor Authentication for Privileged Access",
                description="Privileged access should be protected by MFA.",
                domain="Identity and Access Management",
                control_type="technical",
                priority="high",
            ),
            Control(
                control_code="LG-01",
                title="Centralized Audit Logging",
                description="Security-relevant activities should be centrally logged and reviewable.",
                domain="Logging and Monitoring",
                control_type="technical",
                priority="high",
            ),
            Control(
                control_code="AS-01",
                title="Cloud Asset Inventory",
                description="Cloud assets should be inventoried and reviewed regularly.",
                domain="Asset Management",
                control_type="technical",
                priority="medium",
            ),
            Control(
                control_code="ST-01",
                title="Public Storage Exposure Review",
                description="Public object storage exposure should be identified and addressed.",
                domain="Data Protection",
                control_type="technical",
                priority="high",
            ),
            Control(
                control_code="NW-01",
                title="Security Group and Firewall Review",
                description="Network security rules should be reviewed for risky exposure.",
                domain="Network Security",
                control_type="technical",
                priority="high",
            ),
        ]
        db.add_all(controls)

    if db.query(Lab).count() == 0:
        labs = [
            Lab(
                name="CloudTrail Logging Check",
                description="Verify audit logging coverage in AWS CloudTrail.",
                cloud_provider="AWS",
                execution_type="scripted",
                evidence_type="config_snapshot",
            ),
            Lab(
                name="MFA Coverage Check",
                description="Verify MFA coverage for privileged accounts.",
                cloud_provider="AWS",
                execution_type="manual",
                evidence_type="access_review",
            ),
            Lab(
                name="EC2 Inventory Collector",
                description="Collect EC2 inventory for asset review.",
                cloud_provider="AWS",
                execution_type="scripted",
                evidence_type="system_export",
            ),
            Lab(
                name="S3 Public Bucket Check",
                description="Identify publicly exposed S3 buckets.",
                cloud_provider="AWS",
                execution_type="scripted",
                evidence_type="lab_output",
            ),
            Lab(
                name="Security Group Drift Check",
                description="Review risky ingress and overly permissive firewall rules.",
                cloud_provider="AWS",
                execution_type="scripted",
                evidence_type="lab_output",
            ),
        ]
        db.add_all(labs)
    if db.query(ControlMapping).count() == 0:
        mappings = [
            ControlMapping(
                control_id=1,
                framework_id=1,
                framework_control_code="CC6.3",
                framework_control_title="Logical access security measures",
                mapping_notes="MFA supports secure logical access for privileged users."
            ),
            ControlMapping(
                control_id=1,
                framework_id=2,
                framework_control_code="A.5.17",
                framework_control_title="Authentication information",
                mapping_notes="MFA aligns to secure authentication management."
            ),
            ControlMapping(
                control_id=1,
                framework_id=3,
                framework_control_code="8.4",
                framework_control_title="MFA for access into the CDE",
                mapping_notes="PCI DSS requires MFA in relevant administrative access scenarios."
            ),
            ControlMapping(
                control_id=2,
                framework_id=1,
                framework_control_code="CC7.2",
                framework_control_title="Monitoring system components",
                mapping_notes="Audit logging supports monitoring and anomaly detection."
            ),
            ControlMapping(
                control_id=2,
                framework_id=2,
                framework_control_code="A.8.15",
                framework_control_title="Logging",
                mapping_notes="Centralized logs support audit trail requirements."
            ),
            ControlMapping(
                control_id=2,
                framework_id=3,
                framework_control_code="10.2",
                framework_control_title="Audit logs are implemented",
                mapping_notes="PCI DSS requires logging of relevant events."
            ),
            ControlMapping(
                control_id=4,
                framework_id=2,
                framework_control_code="A.8.12",
                framework_control_title="Data leakage prevention",
                mapping_notes="Public storage exposure may undermine data protection objectives."
            ),
            ControlMapping(
                control_id=4,
                framework_id=3,
                framework_control_code="3.3",
                framework_control_title="Stored account data is protected",
                mapping_notes="Storage exposure may affect protection of stored cardholder-related data."
            ),
        ]
        db.add_all(mappings)
    db.commit()
    db.close()
    print("Seed data inserted successfully.")


if __name__ == "__main__":
    seed()