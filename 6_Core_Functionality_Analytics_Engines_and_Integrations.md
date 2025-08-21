# 6. Core Functionality: Analytics, Engines, and Integrations

After deploying agents, the next step is to configure the core analytical and integration capabilities of Cortex XSIAM.

## Cortex XSIAM - Analytics

[cite_start]The Analytics engine analyzes data from various sensors to establish a baseline of normal behavior and then raises alerts when it detects anomalies or malicious activities. [cite: 955]

### Prerequisites for Analytics

1.  **Configure Network Parameters**: Define your internal IP address ranges and domain suffixes so XSIAM can identify and track network assets. [cite_start]This is done under **Inventory > Assets > Network Configuration**. [cite: 958, 963, 970, 974]
2.  [cite_start]**Enable the Analytics Engine**: Go to **Settings > Configurations > Cortex XSIAM - Analytics** and click **Enable**. [cite: 959, 991, 992] [cite_start]Creating the initial baseline requires a minimum amount of data (e.g., logs from 30 endpoints over 2 weeks) and can take up to three hours. [cite: 984, 992]
3.  [cite_start]**Set up Cloud Identity Engine**: This is a prerequisite for Identity Analytics. [cite: 960]
4.  [cite_start]**Enable Identity Analytics**: Activating this allows the engine to aggregate user profile details and activities, which is highly recommended for enriching investigations. [cite: 961, 981]

## Cortex XSIAM Engines

[cite_start]Engines are installed in a remote network to allow communication and execution of integration commands between that network and Cortex XSIAM. [cite: 996, 997]

### Engine Requirements

* [cite_start]**Operating System**: Supported Linux distributions include Ubuntu, RHEL, Oracle Linux, and Amazon Linux. [cite: 1008, 1009]
* [cite_start]**Hardware**: For a production environment, a minimum of 16 CPU cores, 32 GB RAM, and 100 GB of storage is recommended. [cite: 1006]
* **Dependencies**: Docker or Podman must be installed. [cite_start]The shell installer will handle this automatically. [cite: 1000, 1001]
* [cite_start]**Network**: The engine needs outbound access on port 443 to several URLs for connectivity and pulling container images. [cite: 1014, 1017]

### How to Install an Engine

1.  [cite_start]**Create an Engine**: Go to **Settings > Configurations > Data Broker > Engines** and click **Create New Engine**. [cite: 1050]
2.  [cite_start]**Name the Engine**: Provide a meaningful name. [cite: 1052]
3.  [cite_start]**Select Installer Type**: The **Shell** installer is recommended for most Linux deployments as it handles dependencies automatically. [cite: 1029, 1030, 1037] [cite_start]Other options include DEB, RPM, and Zip. [cite: 1028]
4.  **Install on the Host Machine**:
    * [cite_start]Move the installer file to the engine machine. [cite: 1061]
    * [cite_start]Grant execution permissions (`chmod +x <engine-file-path>`). [cite: 1063]
    * [cite_start]Run the installer with `sudo`. [cite: 1065]
5.  [cite_start]**Verify Connection**: After installation, check the **Engines** page in the Cortex XSIAM UI to ensure the engine is connected. [cite: 1100, 1103]

## Set up Cloud Identity Engine (CIE)

[cite_start]Cloud Identity Engine (CIE) is an optional service that provides Palo Alto Networks applications with read-only access to your on-premise (Active Directory) or cloud-based (Microsoft Entra) directory information. [cite: 1112, 1115, 1122, 1125] [cite_start]This allows you to write security policies based on users and groups instead of just IP addresses. [cite: 1111]

### How to Configure CIE with Cortex XSIAM

1.  [cite_start]**Activate CIE**: Follow the instructions to activate a CIE instance in the same region as your Cortex XSIAM tenant. [cite: 1123, 1128, 1129]
2.  [cite_start]**Connect to Cortex XSIAM**: In the Cortex XSIAM UI, go to **Settings > Configuration > Integrations > Cloud Identity Engine**. [cite: 1133]
3.  [cite_start]**Select Instance**: Choose your CIE instance name from the dialog box and click **Save**. [cite: 1134]

[cite_start]You can also enable **risk signal sharing** from Cortex XSIAM to CIE, which allows CIE to support adaptive policy enforcement based on real-time user and host risk assessments. [cite: 1136, 1137]
```

-----

### **`07_Data_Sources_and_Content_Management.md`**

```markdown
