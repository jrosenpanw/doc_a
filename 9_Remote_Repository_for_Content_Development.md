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
