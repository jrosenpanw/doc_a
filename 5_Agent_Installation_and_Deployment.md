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
