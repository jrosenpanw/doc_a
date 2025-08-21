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
