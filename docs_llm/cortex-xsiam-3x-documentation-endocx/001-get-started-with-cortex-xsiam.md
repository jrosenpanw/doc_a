## Get started with Cortex XSIAM

Alert Alert Exclusion Analytics behavioral indicators of compromise
Attack Surface Management Behavioral indicators of compromise Bring Your
Own Machine Learning Broker Virtual Machine Broker Virtual Machine Fully
Qualified Domain Name Causality Chain Causality Group Owner Causality
View Cloud Detection and Response Cortex Copilot Cortex Data Model
Cortex Query Language Dataset Elasticsearch Filebeat Endpoint Detection
and Response Endpoint Protection Platform Exception Exception vs Alert
Exclusion Extended Detection and Response External Dynamic List Filebeat
Forensics Fully Qualified Domain Name Identity Threat Detection and
Response Indicators of compromise IT Metrics Dashboard Managed Threat
Hunting Management, Reporting, and Compliance Master Boot Record
Protection MITRE ATT&CK Framework Coverage Dashboard Next-Generation
Firewall Notebooks On-write File Protection Playbook Prisma Script
Security Orchestration, Automation, and Response Security Information
and Event Management Threat Intel Management User and Entity Behavior
Analytics Unified Extensible Firmware Interface Protection Virtual
Machine Vulnerability Assessment Windows Event Collector XDR Collector
XSIAM Command Center

### What is Cortex XSIAM?

Cortex XSIAM (extended security intelligence and automation management)
is an AI-driven platform that transforms the security operations center
(SOC), harnessing the power of AI and automation to simplify operations,
stop threats at scale, and accelerate incident remediation. Reduce risk
and operational complexity by centralizing multiple products into a
single, converged platform purpose-built for security operations.

By consolidating data and tools into a single AI-driven platform, SOCs
can simplify security operations, stop threats at scale, and
signiﬁcantly accelerate security outcomes.

### Key features

1.  Simplify security operations with a converged platform:

    - Subject to your Cortex XSIAM license, it combines SOC capabilities
      like XDR, SOAR, ASM, and SIEM, with Cloud Posture and Cloud
      Runtime Security into one uniﬁed platform, eliminating the need
      for console switching.

    - Supports broad integration, enabling easy onboarding of diverse
      data sources without extensive engineering efforts.

    - Ensures continuous collection, stitching, and normalization of raw
      data, going beyond alerts to deliver enriched insights.

    - Enhances investigation capabilities for faster and more effective
      threat identiﬁcation and remediation.

2.  Stop threats at scale with AI-driven outcomes:

    - Leverages out-of-the-box AI models to connect events across data
      sources, delivering a uniﬁed view of incidents and risks.

    - Employs alert grouping and AI-driven incident scoring to
      prioritize incidents based on overall risk.

    - Transforms low-conﬁdence events into high-conﬁdence incidents,
      enabling security teams to focus efﬁciently on critical threats.

3.  Accelerate incident remediation with an automation-ﬁrst approach:

    - Offers hundreds of pre-built content packs from the Cortex
      Marketplace to streamline security operations.

    - Automates manual tasks, including responding to incidents and
      managing risks, saving time and effort.

    - Supports customization of automations, allowing SOCs to tailor
      workﬂows to their speciﬁc needs.

    - Features alert-speciﬁc playbooks that trigger automatically,
      addressing risks before analysts intervene.

    - Continuously learns from analyst actions, providing
      recommendations for future automations and improving incident
      resolution efﬁciency.

### Security challenges addressed by Cortex XSIAM

- Data overload: Reduces noise from high volumes of security events,
  prioritizing actionable incidents.

- Fragmented security Visibility: Uniﬁes endpoint, network, cloud, and
  identity data for comprehensive threat detection and response.

- Slow incident response: Accelerates investigations with intelligent
  alert grouping and detailed attack timelines.

- Manual alert management: Automates enrichment and resolution of
  low-risk alerts, reducing analysts' manual workload.

- Evolving threat landscape: Keeps defenses up-to-date with real-time
  threat intelligence and continuous ML model optimization.

- Operational inefﬁciencies: Delivers an out-of-the-box solution with
  built-in optimizations, eliminating the need for extensive
  customer-led tuning.

- Analyst burnout: Alleviates alert fatigue by focusing analyst efforts
  on high-priority threats.

### Cortex XSIAM architecture

The following diagram shows the high-level architecture for key Cortex
XSIAM components and integrations:

![](media/rId23.png){width="5.833333333333333in"
height="2.092707786526684in"}

The architecture varies between product licenses, but includes these
standard components:

- Cortex XSIAM provides a single interface from which you can
  investigate and triage issues, take remediation actions, and define
  policies to detect malicious activity in the future.

- The XDR data layer within your Cortex XSIAM tenant stores the logs
  from all the data types.

- The Cortex XSIAM analytics can also consume endpoint data to
  automatically detect and report on post-intrusion threats. The
  analytics engine can use endpoint data to raise alerts about abnormal
  network behavior (for example, port scan activity).

- Cortex Native Data Lake is a cloud-based logging infrastructure that
  allows you to centralize the collection and storage of logs generated
  by your Cortex XDR agents regardless of location. The Cortex XDR
  agents and Cortex XSIAM forward all logs to the Cortex Native Data
  Lake. You can view the logs for your agents in Cortex XSIAM. With the
  Log Forwarding app, you can also forward logs to an external syslog
  receiver.

<!-- -->

- > **Note**

  > You can host your Cortex Native Data Lake instance in either the
  > United States (US) Region or the European Union (EU) Region.

<!-- -->

- Directory Sync Service enables Palo Alto Networks cloud-based
  applications to leverage computer, user, and group attributes from
  your on-prem Active Directory for use in policy and endpoint
  management. The Directory Sync Service uses an on-prem agent to
  collect those attributes from your on-prem Active Directory. The
  Directory Sync Service agent runs in the background to collect the
  Active Directory information and syncs it with the cloud-based
  Directory Sync Service that you configure using the Hub.

<!-- -->

- > **Note**

  > You can host your Directory Sync Service instance in either the US
  > Region or EU Region.

<!-- -->

- WildFire Cloud Service identifies previously unknown malware and
  generates signatures that Palo Alto Networks firewalls and Cortex
  XSIAM can use to then detect and block that malware. When a Cortex XDR
  agent detects an unknown sample (an attempt to run a macro, DLL, or
  executable file), Cortex XSIAM can automatically forward the sample
  for WildFire analysis. Based on the properties, behaviors, and
  activities the sample displays when analyzed and executed in the
  WildFire sandbox, WildFire determines the sample to be benign,
  grayware, phishing, or malicious. WildFire then generates signatures
  to recognize the newly discovered malware and makes the latest
  signatures globally available every five minutes.

Additional optional architecture components include:

- Palo Alto Networks\' next-generation firewalls, on-prem or virtual
  firewalls, enforce network security policies in your campus, branch
  offices, and cloud data centers.

- PANW sources such as Prisma Access and Global Protect, enable you to
  extend your firewall security policy to mobile users and remote
  networks. You can also forward related traffic logs, including IoT
  logs, to Cortex Native Data Lake. The analytics engine can then
  analyze those logs and raise alerts on anomalous behavior.

- External firewalls and alerts enable Cortex XSIAM to ingest traffic
  logs and use the analytics engine to analyze those logs and raise
  alerts on anomalous behavior.

- External alert sources can add additional context to your incidents.
  You can send Cortex XSIAM alerts from external sources using the
  Cortex XSIAM API.

#### Detailed product architecture

This diagram illustrates components and their connections without
differentiating between Cloud and On-Premises environments. It
represents the full system architecture. Please note that it may change
depending on your exact license.

![](media/rId26.png){width="5.833333333333333in"
height="3.879166666666667in"}

