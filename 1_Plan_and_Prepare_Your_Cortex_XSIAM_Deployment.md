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
