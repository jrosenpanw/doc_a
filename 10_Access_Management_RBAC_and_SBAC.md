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
