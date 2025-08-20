Here is the content from the document, organized into separate Markdown files based on logical areas.

-----

### **`01_Plan_and_Prepare.md`**

```markdown
# 1. Plan and Prepare Your Cortex XSIAM Deployment

Before you begin the deployment process, it's crucial to plan and prepare. [cite_start]This involves understanding your storage and bandwidth needs, determining the hosting region, and familiarizing yourself with the overall onboarding process. [cite: 5, 11]

## Prepare for Deployment

[cite_start]Consider the following key aspects before you start[cite: 13]:

* **Log Storage:** Determine the amount of log storage your deployment will require. [cite_start]You may need to consult with your partner or sales representative to purchase additional storage for your Cortex XSIAM tenant. [cite: 14, 15]
* **Hosting Region:** Decide on the geographic region where you want to host your Cortex XSIAM tenant and any related services. [cite_start]If you plan to stream data from a Strata Logging Service, it must be in the same region as your XSIAM instance. [cite: 16, 17] [cite_start]A list of supported regions is available in the documentation. [cite: 18]
* **Bandwidth Requirements:** If you are using a Cortex XDR Pro per Endpoint license, you must calculate the necessary bandwidth to support your agents. The general requirement is **1.2Mbps of bandwidth for every 1,000 agents**. [cite_start]This scales proportionally; for example, 100,000 agents would require 120Mbps of bandwidth. [cite: 19, 20, 21, 23, 24]

## Cortex XSIAM Onboarding Checklist

[cite_start]The onboarding process follows a structured checklist to ensure a successful deployment. [cite: 10, 25] The recommended steps are:

1.  [cite_start]**Activate Cortex XSIAM:** The initial step to get your tenant up and running. [cite: 25]
2.  [cite_start]**Pre-installation steps for Cortex XDR agents:** Prepare your environment for agent deployment. [cite: 25]
3.  [cite_start]**Install Cortex XDR agents:** Roll out the agents to your endpoints. [cite: 25]
4.  [cite_start]**Configure and deploy:** Set up the core components of Cortex XSIAM. [cite: 25]
5.  [cite_start]**Define data sources:** Integrate various data sources for comprehensive analytics. [cite: 25]
6.  [cite_start]**Perform health checks:** Verify that the system is operating correctly post-deployment. [cite: 25]

```

-----

### **`02_Activate_Cortex_XSIAM.md`**

```markdown
# 2. Activate Cortex XSIAM

Activation is the first step in the deployment process. [cite_start]You will use the Cortex Gateway, a centralized portal, to activate and manage your tenants. [cite: 29]

## Prerequisites for Activation

[cite_start]Before you can activate your tenant, you must have the following[cite: 33]:

* [cite_start]The **Cortex XSIAM activation email**. [cite: 34]
* A **Customer Support Portal (CSP) account**. [cite_start]You can set up two-factor authentication (2FA) for your CSP account. [cite: 35, 36, 37]
* The appropriate **user roles**:
    * [cite_start]**CSP role**: You need the **Super User** role in your CSP account. [cite: 40]
    * **Cortex role**: You must have the **Account Admin** role in Cortex Gateway. [cite_start]The first user to access the Gateway with a CSP Super User role is automatically granted this permission. [cite: 40]

## How to Activate Your Tenant

1.  **Log in to Cortex Gateway** using your CSP credentials. [cite_start]You can use the link from your activation email. [cite: 42, 43, 44]
2.  [cite_start]In the `Available for Activation` section, find the tenant using its serial number and click **Activate**. [cite: 50] [cite_start]A production tenant is activated first; a development tenant can be set up later if your license allows it. [cite: 52]
3.  [cite_start]On the **Tenant Activation** page, define the following[cite: 53]:
    * [cite_start]**Tenant Name**: A unique name for your tenant. [cite: 54]
    * [cite_start]**Region**: The geographic location where your tenant will be hosted. [cite: 54]
    * [cite_start]**Tenant Subdomain**: A DNS record used to access the tenant directly. [cite: 54]
    * [cite_start]**Encryption Method**: Choose between default encryption (recommended) or Bring Your Own Keys (BYOK). [cite: 54]
4.  [cite_start]Agree to the terms and conditions and click **Activate**. [cite: 55] [cite_start]The activation process can take about an hour, and you will be notified by email upon completion. [cite: 57, 58]
5.  [cite_start]After activation, verify that you can access the tenant from the Cortex Gateway. [cite: 60]
6.  [cite_start]Enable access to required Palo Alto Networks resources in your firewall configuration to ensure proper communication. [cite: 67, 68, 69]

## Bring Your Own Keys (BYOK)

[cite_start]Cortex BYOK allows you to generate your own encryption keys (KEKs) and import them to the Cortex Gateway, giving you greater control over your tenant's data encryption. [cite: 78, 82, 99] [cite_start]This feature enhances the default Google Cloud envelope encryption model by using your customer-provided KEK to encrypt the Data Encryption Keys (DEKs). [cite: 80, 81, 82]

### BYOK Architecture and Security

* [cite_start]Each tenant has its own isolated Key Management Service (KMS) instance within Palo Alto Networks' GCP-based infrastructure. [cite: 85, 86]
* [cite_start]Two separate keys are used for encrypting data: one for BigQuery and another for other services. [cite: 88]
* [cite_start]Key material is wrapped for protection during transit and unwrapped only within the tenant's KMS. [cite: 90, 91]
* [cite_start]Detailed audit logs and email notifications are provided for all key management operations. [cite: 93, 94]

### BYOK Key Management

[cite_start]You can perform several key management operations through the Cortex Gateway[cite: 96]:

* [cite_start]**Set up a new tenant with BYOK**: During activation, select the BYOK option and follow the setup wizard. [cite: 98, 104]
* [cite_start]**Rotate encryption keys**: Open the options menu for the tenant and select `Rotate Encryption Key`. [cite: 109]
* **Disable encryption keys**: This deactivates the tenant and makes it inaccessible. [cite_start]This action requires an Account Admin role and intervention from the Customer Success team to re-enable. [cite: 115, 117, 119, 121]

### BYOK Setup Process

[cite_start]The setup process involves generating a 32-byte symmetric key and then wrapping it using a key provided by Cortex XSIAM. [cite: 122, 134]

1.  [cite_start]**Generate your key**: Use a method like OpenSSL (`openssl rand 32 <FILENAME>`). [cite: 135, 136]
2.  **Wrap & Upload**: For both the "Data lake" and "Services" keys, do the following:
    * [cite_start]Download the wrapping key from the setup screen (valid for three days). [cite: 138, 139, 140]
    * [cite_start]Use the provided OpenSSL command to wrap your encryption key with the downloaded wrapping key. [cite: 142, 143]
    * [cite_start]Upload the wrapped key to complete the process. [cite: 144]
```

-----

### **`03_User_Management_and_Authentication.md`**

```markdown
# 3. User Management and Authentication

After activating your tenant, you need to manage user roles, permissions, and authentication methods. [cite_start]Cortex XSIAM uses a combination of Role-Based Access Control (RBAC) and Scope-Based Access Control (SBAC). [cite: 173, 174]

## Assigning User Roles and Groups

[cite_start]You can manage roles and users from either **Cortex Gateway** (for multiple tenants) or **Cortex XSIAM Access Management** (for a specific tenant). [cite: 180, 181, 192] [cite_start]It is recommended to create user groups in the Cortex XSIAM tenant, as this supports granular scoping and SAML group mapping. [cite: 237, 238, 239]

### Predefined User Roles

Cortex XSIAM provides several default roles with specific access rights. [cite_start]These roles cannot be edited directly, but you can save them as new roles and customize the permissions. [cite: 200, 207, 208] Key roles include:

* [cite_start]**Account Admin**: A super user with full access to all Cortex products and tenants. [cite: 212]
* [cite_start]**Instance Administrator**: Has full view and edit permissions for all components within a specific tenant. [cite: 212]
* [cite_start]**Investigator**: Can view and triage issues and cases. [cite: 212]
* [cite_start]**Responder**: Can view and triage issues and access response capabilities (excluding Live Terminal). [cite: 212]
* [cite_start]**Viewer**: Can view most features and edit reports. [cite: 212]

### Creating User Groups

[cite_start]It is best practice to create user groups with assigned roles and then add users to these groups. [cite: 195] [cite_start]A user group can only have one role, but users can be part of multiple groups, inheriting the highest level of access from the combination of their roles. [cite: 216, 218]

To create a user group:
1.  [cite_start]Go to **Settings > Configurations > Access Management > User Groups**. [cite: 241]
2.  [cite_start]Click **New Group** and provide a name, description, and assign a role. [cite: 243, 244]
3.  [cite_start]Add users and any nested groups. [cite: 244]
4.  [cite_start](Optional) Configure granular scoping for Assets, Cases and Issues, and Endpoints. [cite: 245]

## Setting Up Authentication

[cite_start]You can authenticate users through the Customer Support Portal (CSP) or by using SAML Single Sign-On (SSO). [cite: 291]

### CSP Authentication

[cite_start]This is the default authentication method. [cite: 295] [cite_start]Users are added to your CSP account and then assigned a role or user group in Cortex Gateway or the tenant to gain access. [cite: 317, 318]

1.  [cite_start]Add users to your CSP account by creating a new user or sending an account registration link. [cite: 330, 331, 336]
2.  [cite_start]Once the user accepts the invitation, they will appear in Cortex Gateway. [cite: 345]
3.  [cite_start]Assign a role to the user directly or add them to a user group. [cite: 346]

### SAML Single Sign-On (SSO) Authentication

[cite_start]SSO allows users to authenticate using your organization's Identity Provider (IdP), such as Okta or Azure AD, that supports SAML 2.0. [cite: 298, 299] [cite_start]This method enforces multi-factor authentication (MFA) at the IdP level and simplifies access management by mapping SAML groups to Cortex XSIAM user groups. [cite: 302, 303]

[cite_start]**Note:** If you use SSO, users must log in directly via the tenant's FQDN, not through the Cortex Gateway. [cite: 356, 472]

#### Setting up Okta as the IdP

1.  [cite_start]**Configure Okta Groups**: Create groups in Okta that correspond to user groups in Cortex XSIAM. [cite: 418]
2.  [cite_start]**Copy SSO and URI values from Cortex XSIAM**: In Cortex XSIAM, navigate to `Settings > Configurations > Access Management > Authentication Settings` and copy the `Single Sign-On URL` and `Audience URI (SP Entity ID)`. [cite: 425, 429]
3.  **Configure the Application in Okta**: Create a new application in Okta and paste the values copied from Cortex XSIAM into the SAML settings. [cite_start]Configure the required attribute statements (FirstName, LastName, Email, memberOf). [cite: 433, 434, 437, 445]
4.  [cite_start]**Copy IdP values from Okta**: Copy the `Identity Provider Single Sign-On URL`, `Identity Provider Issuer`, and the `X.509 Certificate` from Okta. [cite: 449]
5.  [cite_start]**Configure Cortex XSIAM SSO Integration**: Paste the values from Okta into the SSO Integration settings in Cortex XSIAM. [cite: 457]
6.  [cite_start]**Map SAML Groups**: In Cortex XSIAM, edit your user groups and add the corresponding Okta group names in the `SAML Group Mapping` field. [cite: 465]
7.  [cite_start]**Test the SSO Login**: Go to your tenant URL and click `Sign-In with SSO`. [cite: 470]

#### Setting up Azure AD as the IdP

1.  [cite_start]**Configure Azure AD Security Groups**: Create security groups in Azure AD that match user groups in Cortex XSIAM. [cite: 485]
2.  [cite_start]**Copy SSO and URI values from Cortex XSIAM**: Follow the same process as with Okta to get the necessary URLs from Cortex XSIAM. [cite: 491, 496]
3.  **Configure the Application in Azure AD**: Create an enterprise application in Azure AD. In the Basic SAML Configuration, paste the URLs from Cortex XSIAM. The `Sign on URL` from XSIAM goes into the `Reply URL` and `Sign on URL` fields in Azure. [cite_start]The `Audience URI` goes into the `Identifier (Entity ID)` and `Relay State` fields. [cite: 503, 505, 506]
4.  **Configure Attributes & Claims**: Add a group claim to send security groups using the `Group ID` as the source attribute. [cite_start]Customize the claim name to `memberOf`. [cite: 509, 510, 512]
5.  [cite_start]**Copy URLs and Certificate from Azure**: Copy the `Login URL`, `Azure AD Identifier`, and download the `Certificate (Base64)`. [cite: 518, 526]
6.  **Copy Object IDs**: For each security group, copy its `Object Id` from Azure AD. [cite_start]This is what you'll use for mapping. [cite: 529, 531]
7.  [cite_start]**Configure Cortex XSIAM SSO Integration**: Paste the values from Azure into the SSO settings in Cortex XSIAM. [cite: 540]
8.  [cite_start]**Map SAML Groups**: Edit your user groups in Cortex XSIAM and paste the corresponding Azure AD group `Object Id`s into the `SAML Group Mapping` field. [cite: 554]
9.  [cite_start]**Test the SSO Login**: Go to your tenant URL and test the login. [cite: 559]
```

-----

### **`04_Agent_Configuration.md`**

```markdown
# 4. Agent Pre-installation and Configuration

Before deploying Cortex XDR agents, you need to perform several configuration steps to ensure policies are applied correctly and data is collected effectively.

## Define Endpoint Groups

[cite_start]Endpoint groups allow you to apply specific policy rules and manage endpoints collectively. [cite: 568] You can create two types of groups:

* [cite_start]**Dynamic Groups**: Endpoints are automatically added to the group based on characteristics like OS, IP address, or endpoint tags. [cite: 571]
* [cite_start]**Static Groups**: You manually select a specific list of endpoints to include in the group. [cite: 572]

To create a group:
1.  [cite_start]Go to **Inventory > Endpoints > Groups** and click **+Add Group**. [cite: 576]
2.  [cite_start]Enter a name and description. [cite: 580]
3.  [cite_start]Choose whether to create a **Dynamic** group (using filters) or a **Static** group (by selecting endpoints). [cite: 582, 583, 587]
4.  Create the group. [cite_start]It can then be used to assign security profiles. [cite: 593, 594]

## Customize Endpoint Security Profiles

[cite_start]Cortex XSIAM includes default security profiles that offer immediate protection. [cite: 603] [cite_start]These profiles customize and reuse settings across different endpoint groups. [cite: 605] You can find profiles for exploits, malware, agent settings, and exceptions. [cite_start]Review your policy rules and the assigned security profiles to make any necessary adjustments for your environment. [cite: 27]

## Enable Enhanced Data Collection

[cite_start]While Cortex XSIAM provides out-of-the-box protection, you must enable **Data Collection** in an Agent Settings profile to leverage endpoint data for features like Analytics and Host Insights. [cite: 27] [cite_start]This allows the Cortex XDR agent to continuously monitor endpoint activity for malicious events. [cite: 615]

The specific data collected varies by platform (Windows, macOS, Linux) and may include:
* [cite_start]File and process activity [cite: 625, 632, 634]
* [cite_start]Network connections [cite: 625, 632, 634]
* [cite_start]Registry modifications (Windows) [cite: 625]
* [cite_start]Windows Event Logs (requires configuration) [cite: 627, 628]

[cite_start]**Note**: Some advanced data collection, such as for RPC calls or system calls on Windows, requires the **Extended Threat Hunting Data (XTH)** add-on. [cite: 619, 625]

## Configure Global Agent Settings

You can configure global settings that apply to all endpoints in your network. [cite_start]These are found under **Settings > Configurations > General > Agent Configurations**. [cite: 638, 639]

Key global settings include:

* **Global Uninstall Password**: Set a password required to remove a Cortex XDR agent. [cite_start]This can be overridden in individual Agent Settings profiles. [cite: 640, 641, 645]
* **Content Updates Bandwidth and Frequency**:
    * **Bandwidth Control**: Control the network consumption for content updates. [cite_start]Cortex XSIAM provides a calculator to recommend the optimal bandwidth based on the number of agents. [cite: 651, 652]
    * [cite_start]**Minor Content Updates**: Enabled by default, this ensures agents receive the most frequent updates between major content versions. [cite: 655, 656]
* [cite_start]**Agent Auto Upgrade Scheduler**: If auto-upgrades are enabled, you can control the number of parallel upgrades and schedule them for specific days and times. [cite: 665, 668, 670]
* **Advanced Analysis**: Automatically upload alert data for further analysis by Palo Alto Networks. [cite_start]You can also enable automatic creation of exceptions based on the analysis results. [cite: 673, 676, 679]
* **License Revocation and Deletion Period**:
    * [cite_start]**Connection Lost (Days)**: Configure how many days an agent can be disconnected before its license is returned (default is 30 days). [cite: 689, 690]
    * [cite_start]**Agent Deletion (Days)**: Configure how many days after losing connection an agent's data is removed from the console (default is 180 days). [cite: 692, 693]
* [cite_start]**Periodic Duplicate Cleanup**: Enable a periodic cleanup of duplicate endpoint entries in the administration table based on hostname, IP, or MAC address. [cite: 712, 716]
```

-----

### **`05_Agent_Installation_and_Deployment.md`**

```markdown
# 5. Agent Installation and Deployment

After initial configuration, the next step is to deploy the Cortex XDR agent to your endpoints. A phased approach is recommended to ensure a smooth rollout.

## Plan Your Agent Deployment

[cite_start]A multi-step implementation in your production environment is recommended to minimize disruption and isolate any potential issues with business applications. [cite: 730, 732, 734]

A typical deployment plan includes the following phases:

| Step                                          | Duration      | Plan                                                                                                                                                             |
| --------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Prerequisite: Setup Access** | 1 week        | [cite_start]Configure firewall rules, required certificates, and validate compatibility with third-party security products. [cite: 736]                                         |
| **1. Bandwidth Calculation** | As needed     | [cite_start]Allocate 120 Mbps of bandwidth for every 100,000 agents. [cite: 736]                                                                                               |
| **2. Pilot Group Installation** | 1 week        | [cite_start]Install the agent on a small group of 3-10 endpoints to test behavior and user experience. [cite: 736]                                                           |
| **3. Expanded Deployment** | 2 weeks       | [cite_start]Gradually expand distribution to larger groups with similar attributes, reaching up to 100 endpoints. [cite: 736]                                                 |
| **4. Full Installation** | 2+ weeks      | [cite_start]Distribute the agent throughout the organization until all endpoints are protected. [cite: 736]                                                                    |
| **5. & 6. & 7. Policy Definition & Refinement** | 1-2 weeks     | [cite_start]Define, test, and refine corporate policies and protection rules, deploying them globally once finalized. [cite: 736]                                                 |

## Create Agent Installation Packages

[cite_start]You must first create an installation package from the Cortex XSIAM console. [cite: 724, 865]

1.  [cite_start]Navigate to **Inventory > Endpoints > Agent Installations**. [cite: 869]
2.  [cite_start]Click **Create** to start a new installer. [cite: 870]
3.  [cite_start]Enter a unique name and select the **Package Type** (e.g., Standalone Installer, Kubernetes Installer). [cite: 871, 873]
4.  [cite_start]Select the platform (Windows, macOS, Linux, etc.) and the desired agent version. [cite: 932]
5.  [cite_start]After the package is created, right-click it and select **Download**. [cite: 935]

[cite_start]For Windows, it's recommended to download the distribution package that includes both the installer and the latest content to reduce network load during initial roll-out. [cite: 938, 939]

## Deploy the Installation Packages

[cite_start]Once downloaded, you can install the package directly on an endpoint or use a software deployment tool like JAMF, GPO, or SCCM to distribute it to multiple endpoints. [cite: 937]

* [cite_start]**Windows**: Use the `.msi` installer. [cite: 938]
* [cite_start]**macOS**: Use the `.pkg` file from the downloaded `.zip`. [cite: 941, 943]
* [cite_start]**Linux**: Use the `.rpm` or `.deb` installers with a package manager, or the shell installer for manual deployment. [cite: 944, 945]

## Keep Agents and Content Updated

[cite_start]Regularly updating agents and content is essential for protection against new threats. [cite: 738, 739]

### Agent Upgrade Guidelines

Use a phased rollout plan for agent upgrades to minimize risk. A common approach is:

1.  [cite_start]**Phase 1: Control Group**: A small, diverse group of low-risk endpoints. [cite: 772, 773]
2.  [cite_start]**Phase 2: 10% Rollout**: Expand to 10% of endpoints, including low- to medium-risk systems. [cite: 776, 777]
3.  [cite_start]**Phase 3: 40% Rollout**: Continue expansion, incorporating more medium-risk endpoints. [cite: 779]
4.  [cite_start]**Phase 4: 80% Rollout**: Include a wide variety of endpoints, including high-risk systems. [cite: 782, 783]
5.  [cite_start]**Phase 5: Full Rollout**: Complete the update for the remaining 20%. [cite: 785]

### Content Update Guidelines

[cite_start]Content updates, released weekly, are critical for defending against new threats. [cite: 742, 743] A phased approach is also recommended here, often over a shorter period (e.g., one week).

1.  [cite_start]**Phase 1: Control Group**: Deploy updates immediately to a test group. [cite: 796]
2.  [cite_start]**Phase 2: 10% Rollout**: Deploy to a larger group after a 1-day delay. [cite: 797]
3.  [cite_start]**Phase 3: 60% Rollout**: Deploy after a 2-day delay. [cite: 798]
4.  [cite_start]**Phase 4: Full Rollout**: Complete the rollout to the entire organization. [cite: 799]

### How to Configure Updates

* [cite_start]**Agent Upgrades**: You can manually push upgrades to selected endpoints from `Inventory > Endpoints > All Endpoints`. [cite: 807, 811] [cite_start]Alternatively, you can enable **Agent Auto-Upgrade** in an Agent Settings profile, which allows you to define the upgrade scope (e.g., latest release) and rollout timing (immediate or delayed). [cite: 834, 837, 838]
* [cite_start]**Content Updates**: **Content Auto-Update** is enabled by default in Agent Settings profiles. [cite: 759] You can configure the rollout to be immediate, delayed by up to 30 days, or pinned to a specific version. [cite_start]You can also enable **Staging Content** for a test group to get a preview of updates a week before general availability. [cite: 859]
```

-----

### **`06_Core_Functionality.md`**

```markdown
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
# 8. Post-Deployment and Maintenance

After the initial deployment and configuration, you should perform health checks and set up your environment for ongoing operations.

## Perform Health Checks

[cite_start]It is recommended to perform the following health checks to validate your deployment[cite: 1584]:

1.  [cite_start]**Update Prevention Policies**: Ensure that policies and profiles have their action modes set to **Block** for active prevention. [cite: 1585]
2.  **Monitor Operational Status**: Verify that Cortex XDR agents are protecting endpoints as expected. You can check the **Operational Status** column in **Endpoints > All Endpoints**. [cite_start]The status can be `Protected`, `Partially protected`, or `Unprotected`. [cite: 1587, 1601, 1602, 1603, 1605]
3.  [cite_start]**Test Sample Malware**: Use a test malware file (e.g., an EICAR file) to verify end-to-end sample processing by WildFire. [cite: 1589]
4.  **Validate Detectors and Log Ingestion**:
    * [cite_start]Check that issues are being generated from their expected sources (e.g., WildFire malware issues, NGFW issues). [cite: 1591, 1593, 1594]
    * [cite_start]Verify that logs from external integrations are being ingested correctly by checking the **Dataset Management** page. [cite: 1595]

## Configure Server and Security Settings

You can customize various server and security settings to create a more personalized and secure user experience.

### Server Settings

[cite_start]Navigate to **Settings > Configurations > General > Server Settings** to configure the following[cite: 1615]:

* [cite_start]**Timezone and Timestamp Format**: Set your preferred timezone and format, which applies only to your user account. [cite: 1617, 1618]
* [cite_start]**Password Protection for Downloads**: Enable password protection for files retrieved from an endpoint to prevent accidental execution of malicious files. [cite: 1618]
* **Scope-Based Access Control (SBAC)**: Enforce granular scoping for users. [cite_start]This is disabled by default. [cite: 1618]
* [cite_start]**Data Ingestion Monitoring**: Enable health alerts for disruptions in data collection. [cite: 1618]

### Security Settings

[cite_start]Navigate to **Settings > Configurations > General > Security Settings** to configure[cite: 1621]:

* [cite_start]**Session Expiration**: Set the number of hours after which a user's session expires. [cite: 1623]
* [cite_start]**Approved IP Ranges**: Restrict user login access to Cortex XSIAM from specific IP ranges. [cite: 1623]
* [cite_start]**Allowed Domains**: Specify which domain names can be used in distribution lists for reports to prevent sending them outside your organization. [cite: 1623]

## Log Forwarding

[cite_start]You can forward logs from Cortex XSIAM to external services like an email distribution list, a Slack channel, or a syslog receiver to stay informed about important events. [cite: 1627, 1628]

### How to Configure Log Forwarding

1.  **Integrate the External Service**:
    * **For a Syslog Receiver**: Go to `Settings > Configurations > Integrations > External Applications`. Add a new server, specifying its destination, port, and protocol. [cite_start]You must enable access to the appropriate Cortex XSIAM IP addresses in your firewall. [cite: 1643, 1645, 1646, 1647]
    * [cite_start]**For Slack**: Use the provided link under `External Applications` to install the Cortex XSIAM app in your Slack workspace. [cite: 1663, 1664]
2.  **Create a Forwarding Configuration**:
    * [cite_start]Go to **Settings > Configurations > General > Notifications**. [cite: 1683]
    * [cite_start]Click **+ Add Forwarding Configuration**. [cite: 1684]
    * [cite_start]Select the **log type** to forward (e.g., Issues, Agent Audit Logs, Management Audit Logs). [cite: 1686]
    * [cite_start]Use the **Scope** filter to specify the exact criteria for events you want to forward (e.g., `Severity = High`). [cite: 1697]
    * [cite_start]Define the destination (email list, Slack channel, or syslog receiver). [cite: 1700, 1708]

## Monitor Administrative Activity

[cite_start]The **Management Audit Logs** (**Settings > Management Audit Logs**) track all administrative and investigative actions performed in the tenant. [cite: 1720] [cite_start]Logs are stored for 365 days. [cite: 1721] [cite_start]You can filter the logs and configure forwarding to stay informed about important changes. [cite: 1722, 1723]
```

-----

### **`09_Remote_Repository_for_Content_Development.md`**

```markdown
# 9. Remote Repository for Content Development

[cite_start]Cortex XSIAM supports using a development tenant and a remote repository to create, test, and manage content before deploying it to your production environment. [cite: 1924, 1926]

## Understanding Development Tenants and Content

* **Content**: Includes integrations, scripts, playbooks, layouts, and other custom components. [cite_start]It can be either **system content** (from Marketplace content packs) or **custom content** (developed by you). [cite: 1929, 1930, 1934]
* **Development Tenant**: A test environment for developing and checking content safely without impacting your production data. [cite_start]Development tenants have fewer resources and are not intended for performance checks. [cite: 1926, 1936, 1938, 1939]

## Content Management with a Remote Repository

[cite_start]You can use a content management system with a remote repository to push content from a development tenant and then pull it into a production tenant. [cite: 1943]

* [cite_start]**Repository Type**: You can use the **Cortex XSIAM built-in remote repository** (default) or a **private Git-based repository** (e.g., GitHub, GitLab). [cite: 1944, 1971]
* **Push/Pull Workflow**:
    * [cite_start]In a cluster of tenants, one development tenant is designated as the **push tenant**. [cite: 1948]
    * [cite_start]The production tenant and any other development tenants are **pull tenants**. [cite: 1949]
    * The push tenant is the only one with access to the Marketplace. [cite_start]It manages all system content updates, which are then pushed to the repository for the pull tenants to retrieve. [cite: 1951, 1954, 1955]
    * [cite_start]Custom content that is supported for push/pull (like playbooks, scripts, and integrations) is also managed through this workflow. [cite: 1959, 1968]

## How to Set Up a Remote Repository

Setup is typically done when activating a development tenant from the Cortex Gateway or can be configured within an existing tenant's settings. [cite_start]You must have Account Admin or Instance Administrator permission. [cite: 1995]

### Using the Built-in Repository

[cite_start]This is the simplest method and is recommended for a one-branch deployment. [cite: 1974, 1988]

**Scenario: New Development Tenant**
1.  **In the Production Tenant**: Go to `Settings > Configurations > General > Remote Repository Settings` and enable the **Content repository**. The sync direction will be set to `Pull`. [cite_start]Select `Built-in` as the repository type. [cite: 2005, 2006, 2007]
2.  [cite_start]**In Cortex Gateway**: Find your production tenant and click **Activate Dev Tenant**. [cite: 2010]
3.  [cite_start]**During Activation**: Fill in the dev tenant details and select **ENABLE CONTENT REPOSITORY**. [cite: 2011, 2013] This first development tenant will automatically be configured as the push tenant. [cite_start]Additional dev tenants will be pull tenants. [cite: 1977, 1978]

### Using a Private Git Repository

[cite_start]This method is for when you need multiple branches or access to the repository outside of Cortex XSIAM. [cite: 1989] [cite_start]The process is similar to setting up a built-in repository, but you will select **Private** as the repository type and provide the Git repository URL, branch name, and credentials (HTTPS or SSH). [cite: 2064, 2065]

[cite_start]**Note**: If the repository branch you are connecting to is not empty, you must choose whether to keep the content on the tenant (which overwrites the repository) or keep the content in the repository (which overwrites the tenant). [cite: 1985]

## How to Push and Pull Content

### Push Content from the Development Tenant

1.  [cite_start]In the development (push) tenant, navigate to **Settings > Configurations > Remote Repository Content > User-Defined Content**. [cite: 2180]
2.  [cite_start]Select the custom content items you want to push to production. [cite: 2188]
3.  Click **Push to Prod**. [cite_start]You can add a message describing the changes. [cite: 2188, 2191]

### Pull Content into the Production Tenant

1.  [cite_start]After content has been pushed, a notification **"Remote Repository Content Available"** will appear in the production tenant's navigation bar. [cite: 2194]
2.  [cite_start]Click the notification to open the content update window. [cite: 2196]
3.  [cite_start]Click **Install content**. [cite: 2197]
4.  If there are any conflicts between the local content and the repository content, you will be prompted to resolve them. [cite_start]For each conflicting item, you can choose to **Skip** (keep the local version) or **Replace** (use the version from the repository). [cite: 2198, 2199, 2200, 2201]
5.  [cite_start]Click **Continue** to complete the update. [cite: 2202]
```

-----

### **`10_Access_Management_RBAC_and_SBAC.md`**

```markdown
# 10. Access Management: RBAC and SBAC

[cite_start]Cortex XSIAM uses a powerful combination of Role-Based Access Control (RBAC) and Scope-Based Access Control (SBAC) to manage permissions and ensure that users only have access to the data and functions necessary for their roles. [cite: 2221]

## Understanding RBAC vs. SBAC

* **Role-Based Access Control (RBAC)**: This model assigns permissions based on a user's organizational role (e.g., Investigator, Administrator). It defines **what** a user can do and **which parts** of the UI they can access. [cite_start]For example, RBAC determines if a user can view the `Policy Management` page or execute a response action like `Isolate Endpoint`. [cite: 2223, 2224]

* **Scope-Based Access Control (SBAC)**: This model refines RBAC by restricting access to **specific data** within the areas a user is permitted to see. [cite_start]For example, while RBAC might allow an investigator to view the `All Endpoints` table, SBAC can limit their view to only show endpoints belonging to a specific department or region. [cite: 2225, 2228]

[cite_start]This hybrid approach provides both simplicity and granular control over security permissions. [cite: 2229]

## Key Access Management Concepts

* **User Roles**: Define the type of access and actions a user can perform. Cortex XSIAM comes with predefined roles, and you can also create custom roles. [cite_start]Roles control permissions for UI components and XQL datasets. [cite: 2237, 2242, 2245]
* **User Groups**: Group together users with similar access requirements. [cite_start]It is best practice to assign roles and scopes to groups rather than individual users. [cite: 2255]
* **Scoping Areas**: SBAC is applied through three main scoping areas:
    * **Assets**: Restricts access based on asset groups. [cite_start]This also affects the visibility of related cases, issues, and findings. [cite: 2452]
    * [cite_start]**Cases and Issues**: Restricts access based on issue domains (e.g., Security, Health). [cite: 2456]
    * [cite_start]**Endpoints**: Restricts access to specific endpoint groups or tags, which affects endpoint management and policy visibility. [cite: 2457]

## How to Configure User Scope (SBAC)

By default, SBAC is **disabled**. [cite_start]Before enabling it, you must configure the necessary scopes for your users, user groups, and API keys to avoid locking users out. [cite: 2423, 2424]

1.  **Plan Your Scopes**: Determine how your organization's data should be segregated. For example, by business unit, geographic region, or asset type. [cite_start]Ensure there are always designated users with full access to handle cases that span across scopes. [cite: 2440]
2.  **Assign Scopes to Users/Groups**:
    * [cite_start]Navigate to **Settings > Configurations > Access Management** and select either **Users** or **User Groups**. [cite: 2509, 2510]
    * [cite_start]Right-click a user or group and select to edit their permissions/settings. [cite: 2509, 2510]
    * [cite_start]Go to the **Scope** tab. [cite: 2512]
    * For each scoping area (Assets, Cases and Issues, Endpoints), define the scope. [cite_start]For example, for **Assets**, you can choose `All assets`, `No assets`, or `Select asset groups`. [cite: 2516]
3.  **Enable SBAC Globally**:
    * [cite_start]Go to **Settings > Configurations > General > Server Settings**. [cite: 2520]
    * [cite_start]Toggle on **Enable Scope Based Access Control**. [cite: 2520]
    * (Optional) Choose an **Endpoint Scoping Mode**:
        * [cite_start]**Permissive**: Users can access an endpoint if they have at least one of the required scope tags. [cite: 2522]
        * [cite_start]**Restrictive**: Users must have *all* of the scope tags assigned to an endpoint to access it. [cite: 2523]
    * [cite_start]**Save** the settings. [cite: 2524]

**Important**: Some functional areas in Cortex XSIAM, like Graph Search and parts of the Command Centers, do not fully respect SBAC. [cite_start]In these cases, you must use RBAC permissions to restrict access. [cite: 2476, 2482, 2483]
```

-----

### **`11_Dashboards_and_Reports.md`**

```markdown
# 11. Dashboards and Reports

[cite_start]Cortex XSIAM provides powerful visualization tools through dashboards and reports to help you analyze data and monitor your security posture. [cite: 2527]

## Dashboards

[cite_start]Dashboards offer a high-level, visual overview of your system's activity, powered by customizable widgets. [cite: 2527]

* [cite_start]**Predefined Dashboards**: Cortex XSIAM includes several out-of-the-box dashboards that display key statistics about agents, incidents, and system health. [cite: 2528]
* [cite_start]**Command Center Dashboards**: These are special interactive dashboards that provide a dynamic overview of security operations, allowing you to drill down into more detailed views and associated pages. [cite: 2529]
* **Custom Dashboards**: You can create your own dashboards from scratch or by modifying existing ones. [cite_start]The **Dashboard Manager** allows you to add, remove, and arrange widgets to surface the statistics that are most important to you. [cite: 2528, 2534]

## Widgets

Widgets are the individual components that make up a dashboard. [cite_start]They can display data in various formats like graphs, pie charts, tables, and text. [cite: 2527] [cite_start]The **Widget Library** contains a collection of predefined widgets and allows you to create your own custom widgets to visualize data from Cortex XSIAM or external sources. [cite: 2536]

## Reports

[cite_start]Reports are static snapshots of your dashboards that can be generated on-demand or scheduled for regular delivery. [cite: 2528, 2535]

* **Creating Reports**: You can save any dashboard as a report. [cite_start]The **Reports Templates** section allows you to build reports using pre-defined templates or customize your own. [cite: 2528, 2535]
* [cite_start]**Viewing Reports**: The **Reports** page displays all the reports that have been run by administrators, allowing you to view and download them. [cite: 2532]
```

-----

### **`12_Glossary.md`**

```markdown
# 12. Glossary of Terms

[cite_start]This glossary provides definitions for key terms and acronyms used in Cortex products. [cite: 2539]

* [cite_start]**BIOC (Behavioral Indicators of Compromise)**: Rules that detect malicious behavior by looking at a chain of activities (related to processes, registry, files, network) rather than static indicators like hashes. [cite: 2550, 2551]
* [cite_start]**Broker VM (Broker Virtual Machine)**: A secure virtual machine that bridges your network with Cortex products, enabling secure routing of endpoint traffic and collection of logs. [cite: 2557, 2558]
* [cite_start]**Case (formerly Incident)**: A collection of related security alerts and data that tells the full contextual story of a security problem, streamlining investigation. [cite: 2565]
* [cite_start]**CGO (Causality Group Owner)**: The root process that is responsible for an entire chain of events and alerts displayed in the Causality View. [cite: 2568, 2569]
* **EDR (Endpoint Detection and Response)**: A cybersecurity approach that relies on endpoint data to detect and respond to threats. [cite_start]Cortex XDR expands on this by incorporating data from network, cloud, and other sources. [cite: 2598, 2600]
* [cite_start]**IOC (Indicators of Compromise)**: Traditional indicators of a breach, such as malicious file hashes, IP addresses, or domain names. [cite: 2640, 2641]
* [cite_start]**Issue (formerly Alert)**: An event or finding that identifies a problem in your environment that crosses a defined risk threshold and requires attention. [cite: 2643, 2644]
* [cite_start]**Playbook**: An automated workflow that orchestrates a series of tasks, commands, and conditions to respond to security events, improving efficiency. [cite: 2676, 2677]
* [cite_start]**SOAR (Security Orchestration, Automation, and Response)**: A capability that automates security use cases through the use of integrations and playbooks. [cite: 2688]
* [cite_start]**XDM (Cortex Data Model)**: A unified data model that maps logs from various sources into a single, consolidated schema, simplifying data interaction and queries. [cite: 2583, 2584]
* [cite_start]**XDR (Extended Detection and Response)**: An advanced approach to threat detection that gathers and analyzes telemetry from multiple sources—including endpoint, network, and cloud—to provide greater accuracy and coverage than traditional EDR. [cite: 2619]
* [cite_start]**XQL (Cortex Query Language)**: A powerful query language used to search and analyze data from the wide variety of sources ingested into Cortex XSIAM. [cite: 2587]
```