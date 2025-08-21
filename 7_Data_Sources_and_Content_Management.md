# 7. Data Sources and Content Management

To get a complete picture of security incidents, Cortex XSIAM can ingest data from a wide variety of Palo Alto Networks and third-party sources. [cite_start]This is managed through content packs and integrations. [cite: 1147]

## Define Data Sources

[cite_start]The **Data Sources** page (**Settings > Data Sources**) is the starting point for ingesting logs and data from multiple products. [cite: 1149] [cite_start]The Data Onboarder wizard guides you through installing and configuring integrations, and it automatically downloads the required content packs from the Marketplace. [cite: 1152]

You can ingest data from:
* [cite_start]Third-party products (e.g., Microsoft Exchange Online) [cite: 1152]
* [cite_start]Palo Alto Networks products (e.g., Prisma Access, NGFW) [cite: 1152]
* [cite_start]Network connection logs (e.g., from Amazon S3) [cite: 1152]
* [cite_start]Authentication logs (e.g., AWS CloudTrail) [cite: 1152]
* [cite_start]Cloud assets and logs [cite: 1152]

## Cortex XSIAM Content and Marketplace

[cite_start]In Cortex XSIAM, "content" refers to items like playbooks, scripts, integrations, and dashboards that support security orchestration use cases. [cite: 1152, 1157] [cite_start]This content is organized into **content packs** available in the Marketplace. [cite: 1158]

### Cortex Marketplace

[cite_start]The Marketplace allows you to browse, download, and manage content packs created by Palo Alto Networks and other contributors. [cite: 1160, 1165, 1166] [cite_start]You can search and filter content packs by use case (e.g., Phishing, Malware), integration, or content type. [cite: 1174, 1176, 1180]

### Key Content Packs

[cite_start]Cortex XSIAM comes with several pre-installed content packs, such as `Common Scripts` and `Common Playbooks`, which provide essential building blocks for automation. [cite: 1191, 1193, 1194]

Recommended packs to review and install include:
* [cite_start]**Phishing**: To create and respond to phishing issues. [cite: 1203, 1204]
* [cite_start]**Cortex XDR**: To automate incident response for Cortex XDR. [cite: 1205, 1206]
* [cite_start]**ServiceNow / Atlassian Jira**: To manage tickets directly from Cortex XSIAM. [cite: 1207, 1208, 1209, 1210]
* [cite_start]**PAN-OS**: To manage Palo Alto Networks Firewalls and Panorama. [cite: 1211, 1212]

### How to Install Content Packs

1.  [cite_start]Go to **Marketplace > Browse** and find the content pack you need. [cite: 1244]
2.  [cite_start]Click the pack and review its contents and dependencies. [cite: 1245]
3.  Click **Install** to add it to your cart. [cite_start]Cortex XSIAM will automatically include any required dependencies. [cite: 1246, 1223]
4.  [cite_start]Click **Install** from the cart to complete the installation. [cite: 1248, 1250]
5.  [cite_start]After installation, you will need to configure the integration instances. [cite: 1252]

## Integrations and API Keys

[cite_start]Integrations are the mechanisms that connect Cortex XSIAM to other products via APIs, webhooks, etc. [cite: 1257, 1258]

### Configuring an Integration

[cite_start]After installing a content pack that includes an integration, you must configure an instance of it. [cite: 1262]
1.  [cite_start]Go to **Settings > Configuration > Data Collection > Automation and Feed Integrations**. [cite: 1360]
2.  [cite_start]Find the integration and click **+ Add instance**. [cite: 1360]
3.  Fill in the required parameters (e.g., API URL, credentials). [cite_start]You can use credentials stored in the Cortex XSIAM vault. [cite: 1439, 1449]
4.  [cite_start]Use the **Test** button to verify the connection works. [cite: 1569]
5.  **Enable** the instance. [cite_start]If it's a "fetch" integration, you can configure it to poll for new events and create issues automatically. [cite: 1345, 1361]

### Managing API Keys

[cite_start]API keys are used to grant access for scripts and applications to interact with the Cortex XSIAM API. [cite: 1306, 1307]

To create an API key:
1.  [cite_start]Go to **Settings > Configurations > Integrations > API Keys** and click **New Key**. [cite: 1311]
2.  [cite_start]Select a **Security Level** (Standard or Advanced). [cite: 1313]
3.  [cite_start]Assign a **Role** to define the key's permissions. [cite: 1316]
4.  [cite_start](Optional) Set an expiration date and apply a granular scope. [cite: 1321, 1324]
5.  Click **Generate**. [cite_start]**Important**: Copy the key immediately, as you will not be able to view it again. [cite: 1333, 1335, 1336]
```

-----

### **`08_Post_Deployment_and_Maintenance.md`**

```markdown
