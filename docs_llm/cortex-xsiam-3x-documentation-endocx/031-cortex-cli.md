## Cortex CLI

The Cortex CLI provides a unified command interface to efficiently scan
your Cloud Workload Protection (CWP), API Security and Application
Security environments with a single installation, enabling you to
seamlessly integrate security checks into your development process.

### User roles and permissions

Cortex CLI provides a role-based access control mechanism that controls
user permissions and access to the CLI features and functionalities.
Permissions for CLI scans are based on the associated API key. Each API
key can be associated with a specific role, regardless of the user who
generated it. This allows for fine-grained control over API access, even
for users with broader roles, such as Admin or Developer.

- **Preconfigured roles**: The CLI includes these out-of-the-box roles
  with predefined permissions:

  - **CLI Role**: Grants the user permission to onboard and install
    the CLI. Enables uploading scan result to the tenant, and provides
    management capabilities for the uploaded results. In addition,
    includes **CLI Read Only Role** permissions

  - **CLI Read Only Role**: Grants the user permission to run the CLI
    and view output in the CLI. Scan results are not uploaded to the
    tenant

  <!-- -->

  - > **Note**

    > The CLI Read Only Role is not supported for CWP as the system does
    > not support offline mode.

- **Custom roles**: You can create custom roles that include CLI
  permissions, providing fine-grained control over CLI access in roles
  that include other platform permissions to tailor your specific
  requirements

For more information about user roles in Cortex XSIAM, refer to [Assign
user roles and groups](#UUIDc0966cb32b3c88e214d33131de93fa8a).

### Connect Cortex CLI

Connect Cortex CLI to scan supported Cortex Cloud modules and gain
insights into your security posture, enabling you to identify, analyze
and address potential risks.

> **Prerequisites**

- > **System requirements**:

  - > **macOS** (Intel Core i7, such as Sequoia): To ensure all
    > functionalities work correctly, you must install the `vectorscan`
    > dependency via **Homebrew**, using this command:
    > `brew install vectorscan`

  - > **Ubuntu 20** requires the `prefetch` utility

  - > **Ubuntu (for linux-amd64)** also requires the `libhyperscan5`
    > library. To install, run `sudo apt install libhyperscan5`

  - > **Linux for AppSec Module**: Support is provided for systems
    > meeting the following specifications:

    - > **RHEL 10**: Kernel: 6.12, glibc: 2.39

    - > **Debian 12**: Kernel: 6.1.27, glibc: 2.36

    - > **Ubuntu**:

      - > Version 18.04 - Kernel: 4.15, glibc: 2.27

      - > Version 20.04 - Kernel: 5.4, glibc: 2.31

      - > Version 22.04 - Kernel: 5.15, Glibc: 2.35

      - > Version 24.04 - Kernel: 6.8, Glibc: 2.39

  - > **Windows**: AMD 64 and ARM 64

- > For cURL-based downloads:

  - > `curl`

  - > `jq`

    - > On **Ubuntu/Debian-based Linux **distributions:
      > `sudo apt-get install jq`

    - > On **RedHat/CentOS/Fedora**: `sudo yum install jq`

    - > **macOS** (using `Homebrew`): `brew install jq`

    - > **Windows**:

      - > Download the executable from [jq GitHub
        > releases](https://github.com/stedolan/jq/releases)

      - > If `Chocolatey` is installed: `choco install jq`

- > **Permissions**: Grant the user installing the CLI required
  > permissions. For more information refer to
  > [#UUID479c01b6c5644b12c22da36a823a69af](#UUID479c01b6c5644b12c22da36a823a69af)

- > Best Practice (required for SCA vulnerability suppression):

  - > Run the CLI within your current working directory
    > (\<current_directory_path\>). It is recommended to use the
    > absolute file path for your current working directory

  - > Ensure that the `--repo-id` parameter includes
    > the `<repo_owner_name>/<repo_name>` structure, with
    > the `<repo_name>` matching the exact name of the directory

  <!-- -->

  - Example
    > The present working directory is `Users/test/<repo_name>`.
    > Therefore, the `--repo-id` parameter must
    > be `--repo-id <repo_owner_name>/<repo_name>`, ensuring
    > that `<repo_name>` precisely matches the directory name within the
    > structure.

  <!-- -->

  - > For terminal actions performed by Cortex XSIAM IDE extensions on
    > Windows, Command Prompt (CMD) is the supported environment.
    > PowerShell is not supported for these actions

1.  Navigate to Settings \> Data Sources (Under Data Collections) \> +
    Data Source \> Show More \> CI/CD.

- > **Tip**

  > You can also locate your CI tool by typing its name (such as
  > Jenkins) into the search bar on the **Add Data Source** page after
  > selecting **+ Data Sources**.

2.  Hover over **Cortex CLI** and click Connect.

- > **Tip**

  > You can enter **CLI** in the search bar to locate the Cortex CLI
  > tool.

3.  In the **Configure** step of the integration wizard.

    a.  Select your operating system from the menu.

    b.  Download the CLI binary: copy (or download) the command provided
        in the wizard and paste into your terminal.

    c.  Click Next.

    - The **Authenticate** step of the wizard is displayed.

4.  On The **Authenticate** step of the wizard.

    a.  Generate an API:

        i.  Select Generate API key.

            - **IMPORTANT**: This option
              **is required for CWP image scans**

            - This option creates a **CLI** role for the API key with
              CLI **View/Edit** options. It is recommended as it grants
              the API key permissions to not only access data, but also
              to upload or send data back

            - If you do not select this option, the generated API key
              creates a **CLI Read Only** role with CLI **View**
              permissions only

            - **Warning**: Using **With upload results** permissions may
              incur additional costs as per your license agreement

        ii. Copy the the generated `API Key ID` and `API key` that are
            displayed in their respective fields.

        iii. Copy and save the the generated API key from the
             **Retrieve your API key** field.

        - A code command is generated and displayed.

        iv. Verify that the generated API key is displayed under the API
            Keys inventory.

    - > **Note**

      > **Using an existing API Key (or verifying existing API Key permissions)**:
      > If you are using an existing API key, verify it has CLI
      > permissions. **CLI View/Edit** permissions correspond to
      > selecting **With upload results** permissions, while
      > **CLI Read Only** or **View** permissions corresponds to not
      > selecting the **With upload results** permissions.

    b.  Download and save the CLI tool to your system:

        i.  Copy or download the provided code.

        - > **Note**

          > On macOS arm 64 architecture you must unpack the downloaded
          > file to retrieve the executable.

        ii. Replace `${API_KEY}` in the code with your API key.

        iii. Retrieve and paste the Cortex Cloud public API URL in the
             code: Navigate to Settings \> API Keys (under
             Configurations) \> click Copy API URL .

    c.  Run the command in your terminal.

    d.  Click Done.

5.  Make the `cortexcli` file executable: run `chmod +x cortexcli`.

> **Note**
>
> To add an additional CLI instance, navigate to Settings \> Data
> Sources \> select the menu for your connected CLI instance \> + New
> Instance, and repeat the onboarding steps.

#### Download and run the Cortex CLI

1.  Download the CLI: Run
    `curl -k -u $CORTEX_API_ID::$CORTEX_API_KEY --output ./cortexcli $CORTEX_FQDN/api/v2/remote-li/{version}/{platform}/artifacts`

2.  Execute the CLI: Run `chmod +x cortexcli`.

3.  Verify installation: Run `cortexcli -v`.

- The CLI version is displayed.

#### Authentication

You can authenticate the Cortex CLI using one of two methods:
command-line flags or an environment configuration file.

- **Using command-line flags**: Provide your API credentials and base
  URL directly in the command using the following flags

  - `--api-base-url`: \[\$CORTEX_API_BASE_URL\]

  - `--api-key`: \[\$CORTEX_API_KEY\]

  - `--api-key-id` \[\$CORTEX_KEY_ID\]

<!-- -->

- For more information about these flags, refer to [Cortex CLI common
  command line reference guide](#UUID692df6034f88296f74eba572bb9ff237).

<!-- -->

- **Using an environment configuration file**: Instead of using flags,
  you can create an environment configuration file named `cortex.env`.
  Save this file in your working directory and add your credentials as
  variables:

  - `CORTEX_API_KEY`: \<api key id\>

  - `CORTEX_API_KEY`: \<secret\>

  - `CORTEX_API_BASE_URL`: \<tenant URL\>, for example
    `https://api-tenantname.paloaltonetworks.com/`

#### Cortex CLI usage

To execute a Cortex CLI scan, run
`cortexcli [global flags] [module name] scan [module flags]`.

**Command breakdown**

- **Global flags**:

  - `--api-base-url <value>`

  - `--api-key <value>`

  - `--api-key-id <value>`

- `cortexcli` acts as the global option, establishing the environment
  for subsequent Cortex CLI commands

- **Module name**: Select the module (environment) to be scanned:

  - `api` for API Security. For more information about API Security
    scans, refer to [Cortex CLI for API
    Security](#UUIDb1ffc59aa0e6d095fb27175615393ebe)

  - `image` for CWP. For more information about CWP scans, refer to
    [Cortex CLI for Cloud Workload
    Protection](#UUID2aaaaa4730b7203d8fe6833d61c99f3d)

  - `code scan` for Application Security. For more informations about
    Application Security refer to [Cortex CLI for Application
    Security](#UUID74b44110560ce8becddb8cd6ed4ba60d)

- **Module flags**: The flags available for the selected command:

  - For flags common to all environments, refer to [Cortex CLI common
    command line reference guide](#UUID692df6034f88296f74eba572bb9ff237)

  - For flags specific to CWP refer to
    [/document/preview/1394340#UUID-0b78b5d4-d82e-f0ac-e375-0b3f5220e19c](/document/preview/1394340#UUID-0b78b5d4-d82e-f0ac-e375-0b3f5220e19c)

  - For flags specific to API Security, refer to [Cortex CLI API
    Security command line reference
    guide](#UUIDb16a2f075a39c3754a6e4b12b0012a59)

  - For flags specific to Application Security, refer to [Cortex CLI
    Application Security command line
    reference](#UUID1f7b753f144f4db8dd3f589b8832d66d)

> **Note**

- > For more information about CLI usage for CWP, refer to [Cortex CLI
  > for Cloud Workload
  > Protection](#UUID2aaaaa4730b7203d8fe6833d61c99f3d)

- > For more information about CLI usage for API Security, refer to
  > [Cortex CLI for API Security](#UUIDb1ffc59aa0e6d095fb27175615393ebe)

- > For more information about CLI usage for Application Security, refer
  > to [Cortex CLI usage for Application
  > Security](#UUIDb8f6c20b0b698af8d1ce68c976f7e227)

### Cortex CLI common command line reference guide

This reference guide describes the common command line flags used to
manage the Application Security,Cloud Workload Protection (CWP) ) and
API Security modules through the Cortex CLI, including the structure of
base commands and subcommands.

#### Common Cortex CLI commands and flags

The following table describes CLI commands common to all supported
Cortex CLI modules.

+-----------------------------------+-----------------------------------+
| Command                           | Description                       |
+===================================+===================================+
| \--api-base-url                   | The public facing API URL. To     |
|                                   | retrieve the URL, under           |
|                                   | **Settings**, select              |
|                                   | Configurations \> API Keys \>     |
|                                   | copy API URL. Required: true.     |
|                                   | \[\$CORTEX_API_BASE_URL\]         |
+-----------------------------------+-----------------------------------+
| \--api-key                        | The API key used for              |
|                                   | authorization. Required: true.    |
|                                   | \[\$CORTEX_API_KEY\]              |
+-----------------------------------+-----------------------------------+
| \--api-key-id                     | The API key ID. Required: true.   |
|                                   | \[\$CORTEX_API_KEY_ID\]           |
+-----------------------------------+-----------------------------------+
| \--soft-fail                      | Identifies and reports errors     |
|                                   | identified during a scan but does |
|                                   | not trigger a failing condition.  |
|                                   | Instead, the scan returns a       |
|                                   | successful result with an exit    |
|                                   | code of `0`. Unlike skipped or    |
|                                   | suppressed checks, soft fail      |
|                                   | errors are still reported but do  |
|                                   | not cause the scan to fail.       |
|                                   | Required: false.                  |
|                                   | \[\$CORTEX_SOFT_FAIL\]            |
|                                   |                                   |
|                                   | > **Note**                        |
|                                   | >                                 |
|                                   | > For soft fails, a failed check  |
|                                   | > matches the defined severity    |
|                                   | > threshold. If multiple soft     |
|                                   | > fail severities are specified,  |
|                                   | > the highest severity acts as    |
|                                   | > the threshold for determining a |
|                                   | > soft fail. However, a           |
|                                   | > successful scan will always     |
|                                   | > return an exit code of `0`,     |
|                                   | > even if block-level findings    |
|                                   | > (which might trigger soft fails |
|                                   | > based on severity) are present. |
+-----------------------------------+-----------------------------------+
| \--log-level                      | Set the logging level (INFO,      |
|                                   | WARNING, ERROR) for Stdout output |
+-----------------------------------+-----------------------------------+
| \--http-proxy                     | The HTTP proxy server URL to      |
|                                   | route traffic through             |
|                                   | \[\$HTTP_PROXY\]                  |
+-----------------------------------+-----------------------------------+
| \--help                           | Show help options                 |
+-----------------------------------+-----------------------------------+
| \--version                        | Retrieves the version of the      |
|                                   | Cortex CLI currently in use       |
+-----------------------------------+-----------------------------------+

### Cortex CLI for Cloud Workload Protection

Integrate Cloud Workload Protection (CWP) scans for secrets,
vulnerabilities and malware during your continuous integration (CI)
process. By leveraging Software Bill of Materials (SBOM) analysis, you
can identify and remediate vulnerabilities before images are pushed to
the registry, shifting security left and reducing risk in your cloud
environments.

> **Prerequisite**

- > Ensure you have the required user permissions. Refer to
  > [#UUID479c01b6c5644b12c22da36a823a69af](#UUID479c01b6c5644b12c22da36a823a69af)
  > for more information

- > Onboard and install the Cortex CLI. Refer to [Connect Cortex
  > CLI](#UUID24585c529b8f7d01ff2e6718dc8b3fe1) for more information

- > Verify that Java version 11 and above is installed: Run
  > `java -version` in your terminal. If not, refer to [Java SE
  > Development Kit
  > 11.0.25](https://www.oracle.com/java/technologies/downloads/#java11?er=221886)
  > for information about installing Java

#### Run CWP security scans

To scan CWP, run:

          ./cortexcli --api-base-url <API URL> --api-key <API key from the "Authenticate" step in the CLI connector screen> --api-key-id <API key ID from the "Authenticate" step in the CLI connector screen> image scan <archive file of container image>
        

> **Note**
>
> The output contains the number of created issues for malware, secrets,
> and vulnerabilities, organized by severity, based on the current
> policy configuration.

The run command above accepts the following arguments:

- `--api-base-url`: Required - true. The public facing API URL. Refer to
  [Connect Cortex CLI](#UUID24585c529b8f7d01ff2e6718dc8b3fe1) for more
  information

- `--api-key`: Required - true. Your Cortex Cloud API key. Refer to
  [Connect Cortex CLI](#UUID24585c529b8f7d01ff2e6718dc8b3fe1) for more
  information

- `--api-key-id`: Required - true.. Your Cortex Cloud API key ID

- `image scan`: Required - true. Refers to CWP as the type of scan

#### Image scans

For CWP image scans, there are two options: the default Docker daemon
integration and scanning a `.tar` archive.

CWP does not support container image secret scanning for systems running
on ARM architecture.

> **Warning**
>
> Before you begin, ensure you have sudo privileges to execute the image
> scan.

##### Scan with Docker daemon integration (default)

The default method for a cortexcli image scan is Docker daemon
integration.

- **NAME**: Scan a container image archive: `cortexcli image scan`

- **USAGE**: `cortexcli image scan [command options]`

You do not need to specify an extra flag for this method. Use
`--docker-host` to specify the path to the Docker daemon socket if
necessary. The default address for the Docker daemon socket is
`unix:///var/run/docker.sock`.

##### Scan a `.tar` archive

To scan a container image as a .tar archive, you must explicitly specify
the `--archive` flag. The default value for this flag is false. To scan
an archive, you must run `--archive true` (Running `--archive` is the
same as `--archive=true`).

Example

To scan a file named `ubuntu.tar`, run the following command:
`sudo ./cortexcli --api-base-url "${xdr_url}" --api-key "${xdr_token}" --api-key-id "${xdr_auth_id}" image scan --archive ubuntu.tar`.

#### Create an image archive

This example demonstrates how to use the **Create an image archive**
feature in conjunction with the image scan process.

- With Docker: `docker save -o ubuntu.tar ubuntu`

- With Podman:
  `podman save --format oci-archive -o /tmp/alpine-oci.tar alpine:latest`

#### Generate a Software Bill of Materials (SBOM)

You can generate a SBOM for your container images using Cortex CLI and
save the output to a specified file. This functionality enables you to
store the SBOM for further analysis, auditing, and compliance.

The following details the command, usage, and available options for
exporting an SBOM.

**Command**: `cortexcli image sbom`: Exports a Software Bill of
Materials (SBOM) document for a container image archive.

**Usage**: `cortexcli image sbom [command options]`.

**Options**:

- `--archive-format value`: Specifies the image archive format. Values:
  `docker-archive` (default), `oci-archive`

- `--output-format value`: Specifies the SBOM document output format.
  Values: `json` (default), `xml`

- `--output-file value`: Specifies the path to the file where the SBOM
  document will be saved

- \-`-fields value` `[ --fields value ]`: Specifies the fields to
  include in the SBOM document. Multiple fields can be specified.
  Values: author, binaries, license, name, purl, sourcePackage, type,
  version

- \-`-help`, `-h`: Displays help information for the command

#### Generating an SBOM with Docker daemon integration

The default method for generating an SBOM with `cortexcli image sbom` is
to use Docker daemon integration. You do not need to specify an extra
flag for this method.

    sudo ./cortexcli --api-base-url "${xdr_url}" --api-key "${xdr_token}" --api-key-id "${xdr_auth_id}" image sbom <image-name>

#### Generating an SBOM from a `.tar` archive for SBOM

To generate an SBOM from a `.tar` archive, you must explicitly use the
`--archive` flag.

    sudo ./cortexcli-api-base-url "${xdr_url}" --api-key "${xdr_token}" --api-key-id "${xdr_auth_id}" image scan-archive <archive-file>

#### Cloud Workload Protection command line reference

This reference guide documents the Cloud Workload Protection commands
and flags for the Cortex CLI, including the structure of base commands
and subcommands. Refer to [Cortex CLI common command line reference
guide](#UUID692df6034f88296f74eba572bb9ff237) for Cortex CLI commands
common to all supported modules.

  -----------------------------------------------------------------------
  Command                             Description
  ----------------------------------- -----------------------------------
  \--image scan                       Scans a container image archive

  \--ci-pipeline-id value             The CI pipeline identifier

  \--ci-build-id value                The CI build identifier

  \--timeout value                    Timeout (in seconds) after which
                                      the scan will be terminated if it
                                      has not completed (default: 60)

  \--output-format value              Output format options:
                                      `human-readable`, `json` (default:
                                      human-readable)

  \--archive-format value             The image archive format options:
                                      `docker-archive`, `oci-archive`
                                      (default: docker-archive)

  \--name value                       The name assigned to the image

  \--docker-host \<path\>             Specifies the path to the Docker
                                      socket

  \--docker-address                   Specifies the path to the Docker
                                      daemon socket. The default value is
                                      `unix:///var/run/docker.sock`

  \--archive                          Specifies that the image scan
                                      should use an archive file. The
                                      default is false. To scan archive
                                      format, run `--archive=true`
  -----------------------------------------------------------------------

### Cortex CLI for API Security

API Security testing is implemented in Cortex XSIAM through the Cortex
CLI.

This testing evaluates APIs for vulnerabilities and misconfigurations
using fuzzing techniques to ensure secure data transmission, prevent
unauthorized access, and to ensure that the API behaves as expected
under unexpected or malformed input.

> **Prerequisite**

- > Ensure you have the required user permissions. Refer to
  > [/document/preview/1203998#UUID-5f83dcd6-a392-b2c7-a864-65407ab6bfa6_section-idm234735378274209](/document/preview/1203998#UUID-5f83dcd6-a392-b2c7-a864-65407ab6bfa6_section-idm234735378274209)
  > for more information

- > Onboard and install the Cortex CLI. Refer to [Connect Cortex
  > CLI](#UUID24585c529b8f7d01ff2e6718dc8b3fe1) for more information

- > Ensure your application exposes APIs and provides a corresponding
  > OpenAPI Specification file

- > Ensure that you have installed `Java v 11` and above

#### Authentication

The authentication file schema defines the authentication method (such
as JWT, Basic) used to authorize connections to your scanned
application. The following example provides configurations examples for
common methods, including Basic authentication, API Keys and bearer
tokens.

Authentication File Schema Example

    type: headers
    creds:
        name: <header name>
        value: <header value>
    ------------------------------------
    For basic auth
    type: basic
    creds:
        username: {USERNAME}
        password: {PASSWORD}
    ------------------------------------
    For API Keys
    type: headers
    creds:
        name: x-api-key
        value: {API key}
    ------------------------------------
    For Bearer tokens
    type: headers
    creds:
        name: Authorization
        value: Bearer {BEARER_TOKEN} 

#### Running API Security scans

To scan API Security, run:

            ./cortexcli  --log-level <ERROR LEVEL> –-api-base-url <API URL> --api-key <API key from the "Authenticate" step in the CLI connector screen> --auth-id 1 api scan  --api-spec-file <OPENAPI SPEC LOCATION>   --scanned-app-url <BASE URL OF THE SCANNED APP> --java-location <JAVA BIN LOCATION>
            

#### Output

The API Security scan generates a detailed scan report that includes:

- **Findings**: These include vulnerabilities and risks identified in
  the scanned application\'s APIs, such as SQL Injection, sensitive data
  leaks, and other issues

- **Errors**: This section lists error responses returned by the scanned
  application

- **Metadata**: Information such as runtime details, scan status
  (success or failure), scan duration, hostname and scan parameters

The following schema defines the structure and format of API Security
scan reports.

    {
      "reportID": "string",
      "results": [
        {
          "id": "string",
          "name": "string",
          "description": "string",
          "url": "string",
          "method": "string",
          "risk": "string",
          "alert": "string",
          "tags": {},
          "statusCode": "integer",
          "requestBody": "string",
          "curlCommand": "string"
        }
      ],
      "serverErrors": [
        {
          "id": "string",
          "name": "string",
          "description": "string",
          "url": "string",
          "method": "string",
          "risk": "string",
          "alert": "string",
          "tags": {},
          "statusCode": "integer",
          "requestBody": "string",
          "curlCommand": "string"
        }
      ],
      "scanStartTime": "string (ISO 8601 datetime)",
      "elapsedSeconds": "number",
      "hostname": "string",
      "scanStatus": "string",
      "parameters": {
        "scannedAppURL": "string",
        "apiSpecFile": "string",
        "apiSpecType": "string",
        "timeoutSeconds": "integer"
      }
    }
              
          

The following is an example of API Security scan output.

    {
      "reportID": "0a739ae6-d18e-11ef-8a06-263731778ec0",
      "results": [
        {
          "id": "0",
          "name": "Server Leaks Version Information via \"Server\" HTTP Response Header Field",
          "description": "The web/application server is leaking version information via the \"Server\" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.",
          "url": "http://localhost:5000/api/v1/extract",
          "method": "POST",
          "risk": "Low",
          "alert": "Server Leaks Version Information via \"Server\" HTTP Response Header Field",
          "tags": {
            "CWE-200": "https://cwe.mitre.org/data/definitions/200.html",
            "OWASP_2017_A06": "https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html",
            "OWASP_2021_A05": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/",
            "WSTG-v42-INFO-02": "https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server"
          },
          "statusCode": 404,
          "requestBody": "--d3b92f4f-e2e3-4caa-8b00-4e43c8df0d87\r\nContent-Disposition: form-data; name=\"file\"\r\nContent-Type: text/plain\r\n\r\n\"John Doe\"\r\n--d3b92f4f-e2e3-4caa-8b00-4e43c8df0d87--",
          "curlCommand": "curl -X POST \"http://localhost:5000/api/v1/extract\" -H host: localhost:5000 -H user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0 -H pragma: no-cache -H cache-control: no-cache -H accept: application/json -H content-type: multipart/form-data; boundary=d3b92f4f-e2e3-4caa-8b00-4e43c8df0d87 -H content-length: 165 -d '--d3b92f4f-e2e3-4caa-8b00-4e43c8df0d87\r\nContent-Disposition: form-data; name=\"file\"\r\nContent-Type: text/plain\r\n\r\n\"John Doe\"\r\n--d3b92f4f-e2e3-4caa-8b00-4e43c8df0d87--'"
        }
      ],
      "serverErrors": [],
      "scanStartTime": "2025-01-13T11:09:04.919359+02:00",
      "elapsedSeconds": 1.349090375,
      "hostname": "My Computer",
      "scanStatus": "Failed",
      "parameters": {
        "scannedAppURL": "http://localhost:5000",
        "apiSpecFile": "openapi.json",
        "apiSpecType": "openapi",
        "timeoutSeconds": 300
      }
    }
            

#### Cortex CLI API Security command line reference guide

This reference guide describes the dedicated API Security commands and
flags, including the structure of base commands and subcommands. Refer
to [Cortex CLI common command line reference
guide](#UUID692df6034f88296f74eba572bb9ff237) for Cortex CLI commands
common to all supported modules.

+-----------------------------------+--------------------------------------------------+
| Value                             | Command                                          |
+===================================+==================================================+
| \--scanned-app-url (string)       | Base URL of the app to scan (required)           |
+-----------------------------------+--------------------------------------------------+
| \--api-spec-file                  | Path to the API specification file (required)    |
|                                   |                                                  |
| (string)                          |                                                  |
+-----------------------------------+--------------------------------------------------+
| \--api-spec-type                  | Type of the API specification (\'openapi)        |
|                                   | (default \"openapi\")                            |
| (string)                          |                                                  |
+-----------------------------------+--------------------------------------------------+
| \--auth-file                      | Path to the authentication file (optional). For  |
|                                   | more information on authentication, refer to     |
| (string)                          | [Cortex CLI for API                              |
|                                   | Security](#UUIDb1ffc59aa0e6d095fb27175615393ebe) |
+-----------------------------------+--------------------------------------------------+
| \--concurrency                    | Concurrency limit for scan requests (default 5)  |
|                                   |                                                  |
| (int)                             |                                                  |
+-----------------------------------+--------------------------------------------------+
| \--java-location                  | Path to the Java (version \>= 11) binary file    |
|                                   | (default: Java)                                  |
| (string)                          |                                                  |
+-----------------------------------+--------------------------------------------------+
| \--no-publish                     | Avoid publish results to Cortex                  |
|                                   |                                                  |
| (boolean)                         |                                                  |
+-----------------------------------+--------------------------------------------------+
| \--output-file                    | Output path for the report file (optional)       |
|                                   |                                                  |
| (string)                          |                                                  |
+-----------------------------------+--------------------------------------------------+
| \--timeout                        | Scan timeout in seconds (default 300)            |
|                                   |                                                  |
| (int)                             |                                                  |
+-----------------------------------+--------------------------------------------------+
| \--zap-port                       | Listening port to be used by ZAP (default 35391) |
|                                   |                                                  |
| (int)                             |                                                  |
+-----------------------------------+--------------------------------------------------+

### Cortex CLI for Application Security

Cortex CLI for Application Security scans allow developers and security
teams to integrate security checks directly into their application
development workflows.

The Application Security CLI supports the following scan types:

- **Secrets**: Identifies exposed sensitive secrets within your codebase

- **Infrastructure-as-Code** (IaC): Analyzes infrastructure
  configuration files to detect potential security misconfigurations

- **Software Composition Analysis** (SCA): Performs vulnerability
  detection in third-party dependencies, assesses their license
  compliance and their package operational risk

In addition, the Application Security CLI serves as the integration
mechanism for security scanning within supported CI tools such as
Jenkins, GitHub Actions, and others. This is achieved by adding a code
snippet containing the CLI command into the configuration files of your
CI tool when integrating the CI tool with Cortex XSIAM. It acts as a
wrapper, enabling security scanning within your pipelines, and direct
upload of results to the platform.

The Application Security CLI supports the following outputs:

- json

- spdx

- cli

- junitxml

- sarif

- cyclonedx

- cyclonedx_json

#### Application Security CLI scan behavior and output

- Scans generate findings which can be elevated to issues, depending on
  Cortex XSIAM policies

- If one scanner (such as Secrets) fails, the other scanners will
  continue to run and produce results

- Scan failures trigger an error message indicating the scanner that
  failed

- The Application Security CLI provides these output modes for flexible
  management and viewing of scan results:

  - **Upload to platform**: Uploads scan results directly to the
    platform for centralized analysis and management

  - **Upload findings only**. Upload findings, but without including the
    actual source code content. This prevents raw source code from
    leaving your local environment or being stored on the platform

  - **CLI output only**: View scan results directly in your command-line
    interface without being uploaded to the platform

<!-- -->

- For more information about the output flags, refer to [Cortex CLI
  Application Security command line
  reference](#UUID1f7b753f144f4db8dd3f589b8832d66d).

#### Authentication

For authentication, refer to [Connect Cortex
CLI](#UUIDb88d52a7f91d2740c00cf7756a227ae8).

#### Requirements

> **Prerequisites**

- > **For the Cortex CLI binary**:

  - > Ensure you have `Node.js v22` installed on your host machine
    > before running any scans with the Cortex CLI. This is crucial to
    > prevent runtime errors, as the CLI depends on Node.js for
    > executing JavaScript analysis

  <!-- -->

  - > **Note**

    - > To check your version of `Node.js`, run `node -v`

    - > To download Node.js, refer to the official
      > [Node.js](https://nodejs.org/) site

  <!-- -->

  - > For Linux OS systems, ensure that **GLIBC **(GNU C library)
    > version 3.25 or greater is installed

<!-- -->

- > **Note**

  > This requirement does not apply when using the CLI as a container
  > image.

<!-- -->

- > **Permissions**: Ensure you have the required user permissions.
  > Refer to
  > [/document/preview/1203998#UUID-5f83dcd6-a392-b2c7-a864-65407ab6bfa6_section-idm234735378274209](/document/preview/1203998#UUID-5f83dcd6-a392-b2c7-a864-65407ab6bfa6_section-idm234735378274209)
  > for more information

- > Onboard and install the Cortex CLI. Refer to [Connect Cortex
  > CLI](#UUID24585c529b8f7d01ff2e6718dc8b3fe1) for more information

#### Cortex CLI usage for Application Security

To scan Application Security, run:

    cortexcli –-api-base-url <API URL> --api-key <API key from the "Authenticate" step in the CLI connector screen> --api-key-id <API Key ID> code scan --directory {{DIRECTORY}} --branch main --repo-id organization/repo-name –output json --output-file-path ./output.json

##### Command line reference

The command structure includes global flags which are used for
authentication, and then specifies the module name and command specific
to Application Security which are followed by dedicated flags unique to
this module as well as flags common to all modules.

- **Global flags**: These flags are part of the initial `cortexcli`
  command and are necessary to authenticate and connect to Cortex XSIAM

  - `--api-base-url`: (Required = true). The public facing API URL.
    Refer to [Connect Cortex CLI](#UUID24585c529b8f7d01ff2e6718dc8b3fe1)
    for more information

  - `--api-key`: (Required = true). The Cortex Cloud API key generated
    when onboarding the CLI as a data source. Refer to [Connect Cortex
    CLI](#UUID24585c529b8f7d01ff2e6718dc8b3fe1) for more information

  - `--api-key-id`: (Required = true). The Cortex Cloud API key ID
    generated when onboarding the CLI as a data source

<!-- -->

- For a comprehensive list of Application Security global flags, refer
  to [Cortex CLI Application Security command line
  reference](#UUID1f7b753f144f4db8dd3f589b8832d66d)

<!-- -->

- **Application Security specifics**: Following the global flags, the
  command specifies the module and the commands required for initiating
  a scan using the Cortex Cloud Application Security module:

  - `code scan`: Required - true. This command instructs the CLI to
    perform an Application Security scan.

  - For the optional flags, refer to the dedicated Application Security
    [command line reference](#UUID1f7b753f144f4db8dd3f589b8832d66d)

##### CLI Usage Examples

- **Send output to a file**: Direct the command\'s output to a specified
  file instead of displaying it in the console

<!-- -->

- ./cortexcli --api-base-url <BASE_URL> --api-key <API_KEY> --api-key-id <API_KEY_ID> code scan --branch <branch name> --repo-id <repo name> --directory <path> --output json --output-file-path <path>

<!-- -->

- **Perform a scan without upload**: Run a scan for local analysis or
  testing without uploading the results to Cortex XSIAM. This command
  runs a code scan and saves all standard output (human-readable format)
  to `scan_results.txt`

<!-- -->

- ./cortexcli --api-base-url <BASE_URL> --api-key <API_KEY> --api-key-id <API_KEY_ID> code scan --upload-mode no-upload --branch <branch name> --repo-id <repo name> --directory <path>

##### Sample outputs

The `cortexcli` provides different options for how scan results are
presented.

- **Standard output** (stdout): When no specific output format flags
  (such as `--output json` or `--output sarif)` are provided, the Cortex
  CLI will produce standard output directly to your terminal or console

- **JSON output**: To obtain the output of a scan command as a JSON
  file, specify the flags
  `--output json --output-file-path ./output.json`. This command will
  save the detailed scan results in JSON format to output.json in the
  current directory.

##### Supported flags

The Application Security CLI supports both common Cortex CLI and
dedicated Application Security flags.

- For dedicated Application Security flags, refer to [Cortex CLI
  Application Security command line
  reference](#UUID1f7b753f144f4db8dd3f589b8832d66d)

- For common flags, refer to [Cortex CLI common command line reference
  guide](#UUID692df6034f88296f74eba572bb9ff237)

#### Cortex CLI Application Security command line reference

This reference guide documents the commands and flags unique to the
Application Security CLI. For CLI commands common to all supported
modules refer to [Cortex CLI common command line reference
guide](#UUID692df6034f88296f74eba572bb9ff237).

> **Important**
>
> The Cortex CLI Application Security only supports single occurrences
> of each flag. If the same flag is passed multiple times, only the last
> provided value will be used. For example, in the following command,
> only TF CloudFormation will be the scanned framework.
>
> ./cortexcli \--api-base-url \<YOUR_API_URL\> \--api-key
> \<YOUR_API_KEY\> \--auth-id \<YOUR_AUTH_ID\> \--framework terraform
> \--framework \"terraform cloudformation\"

+-----------------------------------+---------------------------------------------------------------------------------------------------+
| Command/Variable                  | Description                                                                                       |
+===================================+===================================================================================================+
| \--source                         | The source of execution. Default source: CLI. Examples: Jenkins, GitHub Actions, CLI              |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--repo-id                        | Required for upload mode.                                                                         |
|                                   |                                                                                                   |
|                                   | Identity string of the repository. Format `repo_owner/repo_name`.                                 |
|                                   |                                                                                                   |
|                                   | > **Note**                                                                                        |
|                                   | >                                                                                                 |
|                                   | > The repo-id flag must not end with `.config`, `.log` or `.ini`. `-config` is acceptable.        |
|                                   |                                                                                                   |
|                                   | - > `--repo-id foo.config` will be blocked                                                        |
|                                   |                                                                                                   |
|                                   | - > `--repo-id foo-config` will pass                                                              |
|                                   |                                                                                                   |
|                                   | To retrieve the repository ID, under **Inventory**, navigate to All Assets \> Repositories (under |
|                                   | Code) \> select a repository \> copy the Asset ID value from the Properties section of the side   |
|                                   | card.                                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--branch                         | Required for upload mode.                                                                         |
|                                   |                                                                                                   |
|                                   | Selected branch of the persisted repository                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--directory                      | Required.                                                                                         |
|                                   |                                                                                                   |
|                                   | The directory path to scan. Cannot be used together with `--file`                                 |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--file                           | The file path to scan. Cannot be used together with `--directory`. When using this option, the    |
|                                   | Cortex CLI will filter runners based on the file type provided. For example, if you specify a     |
|                                   | `.tf` file, only the Terraform and secrets frameworks will be included. You can further limit     |
|                                   | this (for example; skip secrets) by using the `--skip-framework` argument                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--var-file                       | Variable files to load in addition to the default files. This feature is currently supported for  |
|                                   | both source Terraform (.tfvars files) and Helm chart scans (for providing custom values or        |
|                                   | variable overrides). Refer to                                                                     |
|                                   | <https://www.terraform.io/docs/language/values/variables.html#variable-definitions-tfvars-files>) |
|                                   | for more information                                                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--framework                      | Filter scan to run only on specific frameworks {`arm`, `ansible`, `bicep`, `cloudformation`,      |
|                                   | `docker`, `dockerfile`, `helm`, `kubernetes`, `kustomize`, `openapi`, `sca`, `secrets`,           |
|                                   | `serverless`, `terraform`, `terraform_json`, `terraform_plan`}                                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--skip-framework                 | Filter scans to skip specific infrastructure code frameworks. Add multiple frameworks using       |
|                                   | spaces. For example, `--skip-framework terraform sca_package`                                     |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--ca-certificate                 | CA Certificate to use                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| -no-cert-verify                   | (default: false)                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--summary-position               | Sets the position for displaying the summary information                                          |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--upload-mode                    | Upload mode determines the method or mode used to upload data, and includes these options:        |
|                                   |                                                                                                   |
|                                   | - `upload` : Uploads scan results to the Cortex XSIAM platform                                    |
|                                   |                                                                                                   |
|                                   | - `no-upload` : Disables uploads of scan results to the platform                                  |
|                                   |                                                                                                   |
|                                   | - `no-code`: Uploads scan findings to the platform, but without including the actual source code  |
|                                   |   content (code blocks in the uploaded data                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--external-modules-download-path | Specifies the directory to download external modules to. Defaults to `.external_modules`          |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--output                         | Output format for reporting                                                                       |
|                                   |                                                                                                   |
| Supported formats: cli, json,     |                                                                                                   |
| spdx, junitxml, sarif, cyclonedx, |                                                                                                   |
| cyclonedx_json                    |                                                                                                   |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--output-file-path               | Specifies the output path for the scan result file                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--deep-analysis                  | Enables or disables deep analysis of the Terraform plan and related files                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--repo-root-for-plan-enrichment  | Enriches Terraform plan findings by mapping them to their original `.tf` files                    |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--skip-path                      | Specifies a path (file or directory) that should be skipped during the scanning process. This     |
|                                   | option is useful for excluding specific files or directories that are not relevant to the         |
|                                   | scanning analysis, increasing the efficiency and accuracy of scan results                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--create-repo-if-missing         | Determines whether the system should create a repository if it is missing. This option allows     |
|                                   | users to automate the creation of repositories as needed and ensure that all required             |
|                                   | repositories are available for scanning. For example, when running automated scans or integrating |
|                                   | with version control systems, enabling `--create-repo-if-missing` can help maintain consistency   |
|                                   | and prevent disruptions due to missing repositories                                               |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--compact                        | Do not display code blocks in the output                                                          |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--no-fail-on-crash               | Prevents the application from failing (blocking pipelines) in the event of a scanner or backend   |
|                                   | failure. Instead of returning a `2` exit code, it will return a `0` exit code in such scenarios.  |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--var-file                       | Variable files to load in addition to the default files, Currently only supported for source      |
|                                   | Terraform (.tf file) and Helm chart scans                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| CORTEX_APPSEC_VALIDATE_SECRETS    | Controls whether secret validation is performed. By default, this feature is disabled. Set        |
|                                   | `CORTEX_APPSEC_VALIDATE_SECRETS = true` to enable it                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------+
| \--help                           | Help                                                                                              |
+-----------------------------------+---------------------------------------------------------------------------------------------------+

#### CLI pipeline code snippets

You can integrate the Cortex CLI directly into your CI/CD pipelines to
enable automated code scans by adding code snippets to your to your
build script or pipeline configuration, such as a `YAML` or `Groovy`
file. Both `ARM` and `AMD` architectures are supported, ensuring you can
scan your codebase regardless of your runner's environment.

You must replace placeholder variables with your own credentials and
environment-specific details.

##### AWS CodeBuild

- For AMD architecture

<!-- -->

- version: 0.2
      env:
        variables:
          CORTEX_API_URL: "https://api-viso-cq3sdpg7uyd6vqk66ccjyv.xdr-qa2-uat.us.paloaltonetworks.com"
          CORTEX_CLI_VERSION: "0.13.14"
        secrets-manager:
          CORTEX_API_KEY: "CORTEX_API_KEY"   
          CORTEX_API_KEY_ID: "CORTEX_API_KEY_ID"
      phases:
        install:
          commands:
            - apt-get update
            - apt-get install -y curl jq git
        pre_build:
          commands:
            - echo "Getting repo name"
            - export CODEBUILD_ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)  
            - export CODEBUILD_GIT_BRANCH="$(git symbolic-ref HEAD --short 2>/dev/null)"
            - |
              if [ "$CODEBUILD_GIT_BRANCH" = "" ] ; then
                export CODEBUILD_GIT_BRANCH="$(git rev-parse HEAD | xargs git name-rev | cut -d' ' -f2 | sed 's/remotes\/origin\///g')";
              fi
            - export CODEBUILD_PROJECT=${CODEBUILD_BUILD_ID%:$CODEBUILD_LOG_PATH}
            - echo "Downloading cortexcli"
            - |
              crtx_resp=$(curl "${CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=amd64" \
                -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
                -H "Authorization: ${CORTEX_API_KEY}")
            - crtx_url=$(echo "$crtx_resp" | jq -r ".signed_url")
            - curl -o cortexcli "$crtx_url"
            - chmod +x cortexcli
            - ./cortexcli --version
            
        build:
          commands:
            - |
              ./cortexcli \
                         --api-base-url "${CORTEX_API_URL}" \
                         --api-key "${CORTEX_API_KEY}" \
                         --api-key-id "${CORTEX_API_KEY_ID}" \
                         code scan \
                         --directory "$(pwd)" \
                         --repo-id $CODEBUILD_ACCOUNT_ID/$CODEBUILD_PROJECT \
                         --branch $CODEBUILD_GIT_BRANCH \
                         --source AWS_CODE_BUILD \
                         --create-repo-if-missing
      artifacts:
        files:
          - '**/*'

<!-- -->

- For ARM architecture

<!-- -->

- version: 0.2
      env:
        variables:
          CORTEX_API_URL: "https://api-viso-89wjoyyvubntuqjnq8mfub.xdr-qa2-uat.us.paloaltonetworks.com"
          CORTEX_CLI_VERSION: "0.13.16"
        secrets-manager:
          CORTEX_API_KEY: "CORTEX_API_KEY"   
          CORTEX_API_KEY_ID: "CORTEX_API_KEY_ID"
      phases:
        install:
          commands:
            - apt-get update
            - apt-get install -y curl jq git
        pre_build:
          commands:
            - echo "Getting repo name"
            - export CODEBUILD_ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)  
            - export CODEBUILD_GIT_BRANCH="$(git symbolic-ref HEAD --short 2>/dev/null)"
            - |
              if [ "$CODEBUILD_GIT_BRANCH" = "" ] ; then
                export CODEBUILD_GIT_BRANCH="$(git rev-parse HEAD | xargs git name-rev | cut -d' ' -f2 | sed 's/remotes\/origin\///g')";
              fi
            - export CODEBUILD_PROJECT=${CODEBUILD_BUILD_ID%:$CODEBUILD_LOG_PATH}
            - echo "Downloading cortexcli"
            - |
              crtx_resp=$(curl "${CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=arm64" \
                -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
                -H "Authorization: ${CORTEX_API_KEY}")
            - crtx_url=$(echo "$crtx_resp" | jq -r ".signed_url")
            - curl -o cortexcli "$crtx_url"
            - chmod +x cortexcli
            - ./cortexcli --version
            
        build:
          commands:
            - |
              ./cortexcli \
                         --api-base-url "${CORTEX_API_URL}" \
                         --api-key "${CORTEX_API_KEY}" \
                         --api-key-id "${CORTEX_API_KEY_ID}" \
                         code scan \
                         --directory "$(pwd)" \
                         --repo-id $CODEBUILD_ACCOUNT_ID/$CODEBUILD_PROJECT \
                         --branch $CODEBUILD_GIT_BRANCH \
                         --source AWS_CODE_BUILD \
                         --create-repo-if-missing
      artifacts:
        files:
          - '**/*'

##### Azure Pipelines

- For AMD architecture

<!-- -->

- trigger:
        branches:
          include: ['*']
      pr:
        branches:
          include: ['*']
      pool:
        vmImage: ubuntu-latest
      variables:
        CORTEX_API_URL: "https://api-viso-ddk8ww8iuhyvvnnq5ayhr4.xdr-qa2-uat.us.paloaltonetworks.com"
        MIN_LOG_LEVEL: "DEBUG"
      steps:
      - checkout: self
        clean: true
      - task: NodeTool@0
        displayName: "Use Node.js 22.x"
        inputs:
          versionSpec: "22.x"
      - bash: |
          set -euo pipefail
          sudo apt-get update
          sudo apt-get install -y --no-install-recommends jq ca-certificates curl
          BASE="${CORTEX_API_URL%/}"
          URL="$BASE/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=amd64"
          set +x
          CRTX_URL=$(curl -fsSL "$URL" \
            -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
            -H "Authorization: ${CORTEX_API_KEY}" | jq -r '.signed_url')
          set -x
          curl -fsSL -o cortexcli "$CRTX_URL"
          chmod +x cortexcli
        displayName: "Download cortexcli (amd64)"
        env:
          CORTEX_API_URL: $(CORTEX_API_URL)
          CORTEX_API_KEY_ID: $(CORTEX_API_KEY_ID)
          CORTEX_API_KEY: $(CORTEX_API_KEY)
      - bash: |
          set -euo pipefail
          ./cortexcli \
            --api-base-url "${CORTEX_API_URL}" \
            --api-key "${CORTEX_API_KEY}" \
            --api-key-id "${CORTEX_API_KEY_ID}" \
            code scan \
            --directory "$(Build.SourcesDirectory)" \
            --repo-id "$(Build.Repository.Name)" \
            --branch "$(Build.SourceBranchName)" \
            --source "CORTEX_CLI" \
            --create-repo-if-missing
        displayName: "Cortex CLI Code Scan"
        env:
          CORTEX_API_URL: $(CORTEX_API_URL)
          CORTEX_API_KEY_ID: $(CORTEX_API_KEY_ID)
          CORTEX_API_KEY: $(CORTEX_API_KEY)
          MIN_LOG_LEVEL: $(MIN_LOG_LEVEL)

<!-- -->

- For ARM architecture

<!-- -->

- trigger:
        branches:
          include: ['*']
      pr:
        branches:
          include: ['*']
      variables:
        CORTEX_API_URL: "https://api-viso-ddk8ww8iuhyvvnnq5ayhr4.xdr-qa2-uat.us.paloaltonetworks.com"
      pool:
        name: arm
        demands:
          - Agent.OS -equals Linux
      steps:
      - checkout: self
        clean: true
      - task: NodeTool@0
        displayName: "Use Node.js 22.x"
        inputs: { versionSpec: "22.x" }
      - bash: |
          set -euo pipefail
          BASE="${CORTEX_API_URL%/}"
          URL="$BASE/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=arm64"
          set +x
          CRTX_URL=$(curl -fsSL "$URL" \
            -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
            -H "Authorization: ${CORTEX_API_KEY}" | jq -r '.signed_url')
          set -x
          curl -fsSL -o cortexcli "$CRTX_URL"
          chmod +x cortexcli
        displayName: "Download cortexcli (arm64)"
        env:
          CORTEX_API_URL: $(CORTEX_API_URL)
          CORTEX_API_KEY_ID: $(CORTEX_API_KEY_ID)
          CORTEX_API_KEY: $(CORTEX_API_KEY)
      - bash: |
          set -euo pipefail
          ./cortexcli \
            --api-base-url "${CORTEX_API_URL}" \
            --api-key "${CORTEX_API_KEY}" \
            --api-key-id "${CORTEX_API_KEY_ID}" \
            code scan \
            --directory "$(Build.SourcesDirectory)" \
            --repo-id "$(Build.Repository.Name)" \
            --branch "$(Build.SourceBranchName)" \
            --source "CORTEX_CLI" \
            --create-repo-if-missing
        displayName: "Cortex CLI Code Scan (ARM64)"
        env:
          CORTEX_API_URL: $(CORTEX_API_URL)
          CORTEX_API_KEY_ID: $(CORTEX_API_KEY_ID)
          CORTEX_API_KEY: $(CORTEX_API_KEY)

##### Bitbucket

- For AMD architecture

<!-- -->

- image: ubuntu:24.04
      clone:
        depth: full
      pipelines:
        default:
          - step:
              name: Cortex CLI Code Scan (Hosted AMD64)
              script:
                - set -euo pipefail
                - apt-get update && apt-get install -y --no-install-recommends curl jq ca-certificates tar gzip file
                - curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
                - apt-get install -y nodejs
                - node -v && npm -v
                - export CORTEXCLI_HOME="/root/.cortexcli"; rm -rf "$CORTEXCLI_HOME" || true; mkdir -p "$CORTEXCLI_HOME"
                - |
                  CRTX_URL=$(curl -fsSL "${CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=amd64" \
                    -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
                    -H "Authorization: ${CORTEX_API_KEY}" | jq -r '.signed_url')
                  curl -fsSL -o cortexcli "$CRTX_URL"
                  chmod +x cortexcli
                  ./cortexcli --version
                - |
                  ./cortexcli \
                    --api-base-url "${CORTEX_API_URL}" \
                    --api-key "${CORTEX_API_KEY}" \
                    --api-key-id "${CORTEX_API_KEY_ID}" \
                    code scan \
                    --directory "${BITBUCKET_CLONE_DIR}" \
                    --repo-id "${BITBUCKET_REPO_FULL_NAME}" \
                    --branch "${BITBUCKET_BRANCH}" \
                    --source "CORTEX_CLI" \
                    --create-repo-if-missing \
                    --upload-mode no-upload
              artifacts:
                - cortexcli

<!-- -->

- For ARM architecture

<!-- -->

- image: node:22-bookworm

      pipelines:
        default:
          - step:
              name: Cortex CLI Code Scan
              runs-on:
                - self.hosted
                - linux.arm64 
              script:
                - set -euo pipefail
                - apt-get update && apt-get install -y --no-install-recommends curl jq ca-certificates file
                - export CORTEXCLI_HOME="/root/.cortexcli"; rm -rf "$CORTEXCLI_HOME" || true; mkdir -p "$CORTEXCLI_HOME"

                - |
                  set +x
                  CRTX_URL=$(curl -fsSL "${CORTEX_API_URL%/}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=arm64" \
                    -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
                    -H "Authorization: ${CORTEX_API_KEY}" | jq -r '.signed_url')
                  set -x
                  curl -fsSL -o cortexcli "$CRTX_URL"
                  chmod +x cortexcli
                  ./cortexcli --version

                # Run the scan
                - |
                  ./cortexcli \
                    --api-base-url "${CORTEX_API_URL}" \
                    --api-key "${CORTEX_API_KEY}" \
                    --api-key-id "${CORTEX_API_KEY_ID}" \
                    code scan \
                    --directory "${BITBUCKET_CLONE_DIR}" \
                    --repo-id "${BITBUCKET_REPO_FULL_NAME}" \
                    --branch "${BITBUCKET_BRANCH}" \
                    --source "CORTEX_CLI" \
                    --create-repo-if-missing
              artifacts:
                - cortexcli

##### CircleCI

- For AMD architecture

<!-- -->

- version: 2.1
      jobs:
        cortex-code-scan:
          docker:
            - image: cimg/node:22.17.0  # Replace with a suitable image or executor
          environment:
            CORTEX_API_URL: https://api-viso-cq3sdpg7uyd6vqk66ccjyv.xdr-qa2-uat.us.paloaltonetworks.com
          steps:
            - checkout
            - run:
                name: Download cortexcli
                command: |
                  set -x
                  crtx_resp=$(curl "${CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=amd64" \
                    -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
                    -H "Authorization: ${CORTEX_API_KEY}")
                  crtx_url=$(echo $crtx_resp | jq -r ".signed_url")
                  curl -o cortexcli $crtx_url
                  chmod +x cortexcli
                  ./cortexcli --version
            - run:
                name: Run Cortex CLI Code Scan
                command: |
                  ./cortexcli \
                    --api-base-url "${CORTEX_API_URL}" \
                    --api-key "${CORTEX_API_KEY}" \
                    --api-key-id "${CORTEX_API_KEY_ID}" \
                    code scan \
                    --directory "$(pwd)" \
                    --repo-id "${CIRCLE_PROJECT_USERNAME}/${CIRCLE_PROJECT_REPONAME}" \
                    --branch "${CIRCLE_BRANCH}" \
                    --source "CIRCLE_CI" \
                    --create-repo-if-missing
      workflows:
        cortex-scan-workflow:
          jobs:
            - cortex-code-scan:
                context: cortex-secrets

<!-- -->

- For ARM architecture

<!-- -->

- version: 2.1
      jobs:
        cortex-code-scan:
          docker:
            - image: <Replace with image supporting node js version 22 or higher>
          environment:
            CORTEX_API_URL: https://api-viso-89wjoyyvubntuqjnq8mfub.xdr-qa2-uat.us.paloaltonetworks.com
          steps:
            - checkout
            - run:
                name: Download cortexcli
                command: |
                  set -x
                  crtx_resp=$(curl "${CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=arm64" \
                    -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
                    -H "Authorization: ${CORTEX_API_KEY}")
                  crtx_url=$(echo $crtx_resp | jq -r ".signed_url")
                  curl -o cortexcli $crtx_url
                  chmod +x cortexcli
                  ./cortexcli --version
            - run:
                name: Run Cortex CLI Code Scan
                command: |
                  ./cortexcli \
                    --api-base-url "${CORTEX_API_URL}" \
                    --api-key "${CORTEX_API_KEY}" \
                    --api-key-id "${CORTEX_API_KEY_ID}" \
                    code scan \
                    --directory "$(pwd)" \
                    --repo-id "${CIRCLE_PROJECT_USERNAME}/${CIRCLE_PROJECT_REPONAME}" \
                    --branch "${CIRCLE_BRANCH}" \
                    --source "CIRCLE_CI" \
                    --create-repo-if-missing
      workflows:
        cortex-scan-workflow:
          jobs:
            - cortex-code-scan:
                context: cortex-secrets

##### GitHub Actions

- For AMD architecture

<!-- -->

- name: Cortex CLI Code Scan
      on:
        push:
          branches:
            - main
        workflow_dispatch:
      env:
        CORTEX_API_KEY: ${{secrets.CORTEX_API_KEY}}
        CORTEX_API_KEY_ID: ${{secrets.CORTEX_API_KEY_ID}}
        CORTEX_API_URL: https://api-viso-cq3sdpg7uyd6vqk66ccjyv.xdr-qa2-uat.us.paloaltonetworks.com
        
      jobs:
        cortex-code-scan:
          runs-on: ubuntu-latest
          steps:
          - name: Checkout Repository
            uses: actions/checkout@v2
          
          - name: Set up Node.js
            uses: actions/setup-node@v4
            with:
              node-version: 22
          - name: Verify Node.js Version
            run: node -v
          - name: Download cortexcli
            run: |
              set -x
              crtx_resp=$(curl "${CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=amd64" \
                -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
                -H "Authorization: ${CORTEX_API_KEY}")
              crtx_url=$(echo $crtx_resp | jq -r ".signed_url")
              curl -o cortexcli $crtx_url
              chmod +x cortexcli
              ./cortexcli --version
          - name: Run Cortex CLI Code Scan
            run: |
              ./cortexcli \
                --api-base-url "${CORTEX_API_URL}" \
                --api-key "${CORTEX_API_KEY}" \
                --api-key-id "${CORTEX_API_KEY_ID}" \
                code scan \
                --directory "${{github.workspace}}" \
                --repo-id "${{github.repository}}" \
                --branch "${{github.ref_name}}" \
                --source "GITHUB_ACTIONS" \
                --create-repo-if-missing

<!-- -->

- For ARM architecture

<!-- -->

- name: Cortex CLI Code Scan
      on:
        push:
          branches:
            - main
        workflow_dispatch:
      env:
        CORTEX_API_KEY: ${{secrets.CORTEX_API_KEY}}
        CORTEX_API_KEY_ID: ${{secrets.CORTEX_API_KEY_ID}}
        CORTEX_API_URL: https://api-viso-89wjoyyvubntuqjnq8mfub.xdr-qa2-uat.us.paloaltonetworks.com
        
      jobs:
        cortex-code-scan:
          runs-on: ubuntu-latest
          steps:
          - name: Checkout Repository
            uses: actions/checkout@v2
          
          - name: Set up Node.js
            uses: actions/setup-node@v4
            with:
              node-version: 22
          - name: Verify Node.js Version
            run: node -v
          - name: Download cortexcli
            run: |
              set -x
              crtx_resp=$(curl "${CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=arm64" \
                -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
                -H "Authorization: ${CORTEX_API_KEY}")
              crtx_url=$(echo $crtx_resp | jq -r ".signed_url")
              curl -o cortexcli $crtx_url
              chmod +x cortexcli
              ./cortexcli --version
          - name: Run Cortex CLI Code Scan
            run: |
              ./cortexcli \
                --api-base-url "${CORTEX_API_URL}" \
                --api-key "${CORTEX_API_KEY}" \
                --api-key-id "${CORTEX_API_KEY_ID}" \
                code scan \
                --directory "${{github.workspace}}" \
                --repo-id "${{github.repository}}" \
                --branch "${{github.ref_name}}" \
                --source "GITHUB_ACTIONS" \
                --create-repo-if-missing

##### GitLab Runner

- For AMD architecture

<!-- -->

- stages: [scan]
      variables:
        CORTEX_API_URL: "https://api-viso-8vocygkchsephm7mczadnc.xdr-qa2-uat.us.paloaltonetworks.com"
      cortex_code_scan:
        image: node:22-bookworm@sha256:bb6834c0669aa71cbc8d94606561a721adf489f6b93d7b8b825f0cf1b498c2c4
        tags: ["amd64"]
        stage: scan
        rules:
          - when: on_success
        before_script:
          - uname -m
          - set -euo pipefail
          - apt-get update
          - apt-get install -y --no-install-recommends curl jq ca-certificates tar gzip file
          - export CORTEXCLI_HOME="/root/.cortexcli"; rm -rf "$CORTEXCLI_HOME" || true; mkdir -p "$CORTEXCLI_HOME"
          - |
            # avoid leaking secrets in logs
            set +x
            CRTX_URL=$(curl -fsSL "${CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=amd64" \
              -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
              -H "Authorization: ${CORTEX_API_KEY}" | jq -r '.signed_url')
            set -x
            curl -fsSL -o cortexcli "$CRTX_URL"
            chmod +x cortexcli
            ./cortexcli --version
        script:
          - |
            ./cortexcli \
              --api-base-url "${CORTEX_API_URL}" \
              --api-key "${CORTEX_API_KEY}" \
              --api-key-id "${CORTEX_API_KEY_ID}" \
              code scan \
              --directory "${CI_PROJECT_DIR}" \
              --repo-id "${CI_PROJECT_PATH}" \
              --branch "${CI_COMMIT_REF_NAME}" \
              --source "CORTEX_CLI" \
              --upload-mode no-upload \
              --create-repo-if-missing
        artifacts:
          when: always
          paths: [cortexcli]
          expire_in: 1 day

<!-- -->

- For ARM architecture

<!-- -->

- stages: [scan]
      variables:
        CORTEX_API_URL: "https://api-viso-8vocygkchsephm7mczadnc.xdr-qa2-uat.us.paloaltonetworks.com"
      cortex_code_scan:
        image: node:22-bookworm
        stage: scan
        rules:
          - when: on_success
        before_script:
          - set -euo pipefail
          - apt-get update
          - apt-get install -y --no-install-recommends curl jq ca-certificates tar gzip file
          - export CORTEXCLI_HOME="/root/.cortexcli"; rm -rf "$CORTEXCLI_HOME" || true; mkdir -p "$CORTEXCLI_HOME"
          - |
            # avoid leaking secrets in logs
            set +x
            CRTX_URL=$(curl -fsSL "${CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=arm64" \
              -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
              -H "Authorization: ${CORTEX_API_KEY}" | jq -r '.signed_url')
            set -x
            curl -fsSL -o cortexcli "$CRTX_URL"
            chmod +x cortexcli
            ./cortexcli --version
        script:
          - |
            ./cortexcli \
              --api-base-url "${CORTEX_API_URL}" \
              --api-key "${CORTEX_API_KEY}" \
              --api-key-id "${CORTEX_API_KEY_ID}" \
              code scan \
              --directory "${CI_PROJECT_DIR}" \
              --repo-id "${CI_PROJECT_PATH}" \
              --branch "${CI_COMMIT_REF_NAME}" \
              --source "CORTEX_CLI" \
              --upload-mode no-upload \
              --create-repo-if-missing
        artifacts:
          when: always
          paths: [cortexcli]
          expire_in: 1 day

##### Jenkins

- For AMD architecture

<!-- -->

- pipeline {
          agent {
              docker {
                  image 'cimg/node:22.17.0' // Replace with a suitable image or executor
                  args '-u root'
              }
          }
          environment {
              CORTEX_API_KEY = credentials('CORTEX_API_KEY')
              CORTEX_API_KEY_ID = credentials('CORTEX_API_KEY_ID')
              CORTEX_API_URL = 'https://api-viso-cq3sdpg7uyd6vqk66ccjyv.xdr-qa2-uat.us.paloaltonetworks.com'
          }
          stages {
              stage('Checkout Repository') {
                  steps {
                        git branch: 'main', url: 'this-is-repository-url-example'
                        stash includes: '**/*', name: 'source'
                  }
              }
              stage('Install Dependencies') {
                  steps {
                      sh '''
                      apt update
                      apt install -y curl jq git
                      '''
                  }
              }
              stage('Download cortexcli') {
                  steps {
                      script {
                          def response = sh(script: """
                              curl --location '${env.CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=amd64' \
                                --header 'Authorization: ${env.CORTEX_API_KEY}' \
                                --header 'x-xdr-auth-id: ${env.CORTEX_API_KEY_ID}' \
                                --silent
                          """, returnStdout: true).trim()
                          def downloadUrl = sh(script: """echo '${response}' | jq -r '.signed_url'""", returnStdout: true).trim()
                          sh """
                              curl -o cortexcli '${downloadUrl}'
                              chmod +x cortexcli
                              ./cortexcli --version
                          """
                      }
                  }
              }
              stage('Run Scan') {
              // Replace the repo-id with your repository like: owner/repo
                  steps {
                      script {
                          unstash 'source'
                          sh """
                          ./cortexcli \
                            --api-base-url "${env.CORTEX_API_URL}" \
                            --api-key "${env.CORTEX_API_KEY}" \
                            --api-key-id "${env.CORTEX_API_KEY_ID}" \
                            code scan \
                            --directory "\$(pwd)" \
                            --repo-id <REPLACE WITH REPO_OWNER/REPO_NAME> \
                            --branch <REPLACE WITH BRANCH> \
                            --source "JENKINS" \
                            --create-repo-if-missing
                          """
                      }
                  }
              }
          }
      }

<!-- -->

- For ARM architecture

<!-- -->

- pipeline {
          agent {
              docker {
                  image 'cimg/node:22.17.0' // Replace with a suitable image or executor
                  args '-u root'
              }
          }
          environment {
              CORTEX_API_KEY = credentials('CORTEX_API_KEY')
              CORTEX_API_KEY_ID = credentials('CORTEX_API_KEY_ID')
              CORTEX_API_URL = 'https://api-viso-89wjoyyvubntuqjnq8mfub.xdr-qa2-uat.us.paloaltonetworks.com'
          }
          stages {
              stage('Checkout Repository') {
                  steps {
                        git branch: 'main', url: 'this-is-repository-url-example'
                        stash includes: '**/*', name: 'source'
                  }
              }
              stage('Install Dependencies') {
                  steps {
                      sh '''
                      apt update
                      apt install -y curl jq git
                      '''
                  }
              }
              stage('Download cortexcli') {
                  steps {
                      script {
                          def response = sh(script: """
                              curl --location '${env.CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=arm64' \
                                --header 'Authorization: ${env.CORTEX_API_KEY}' \
                                --header 'x-xdr-auth-id: ${env.CORTEX_API_KEY_ID}' \
                                --silent
                          """, returnStdout: true).trim()
                          def downloadUrl = sh(script: """echo '${response}' | jq -r '.signed_url'""", returnStdout: true).trim()
                          sh """
                              curl -o cortexcli '${downloadUrl}'
                              chmod +x cortexcli
                              ./cortexcli --version
                          """
                      }
                  }
              }
              stage('Run Scan') {
              // Replace the repo-id with your repository like: owner/repo
                  steps {
                      script {
                          unstash 'source'
                          sh """
                          ./cortexcli \
                            --api-base-url "${env.CORTEX_API_URL}" \
                            --api-key "${env.CORTEX_API_KEY}" \
                            --api-key-id "${env.CORTEX_API_KEY_ID}" \
                            code scan \
                            --directory "\$(pwd)" \
                            --repo-id <REPLACE WITH REPO_OWNER/REPO_NAME> \
                            --branch <REPLACE WITH BRANCH> \
                            --source "JENKINS" \
                            --create-repo-if-missing
                          """
                      }
                  }
              }
          }
      }

### Migrate Cortex CLI

As part of the transition from Prisma Cloud to Cortex Cloud, you are
required to migrate your workflows from the Checkov and TwistCLI
command-line tools to the unified Cortex CLI. The Cortex CLI
consolidates the multiple legacy tools, Checkov (for vulnerabilities,
secrets and Infrastructure as Code (IaC) scanning), and TwistCLI (for
container image scanning), into a single, powerful interface,
simplifying your security workflows and creating a more consistent
developer experience. The Cortex CLI is now your single point of entry
for all programmatic security tasks, including code, container image,
and API security scanning.

You can find the Cortex CLI documentation
[here](#UUID479c01b6c5644b12c22da36a823a69af).

> **Prerequisites**
>
> Before you begin, ensure you have the following:

- > Ensure you have an active API key for your Cortex Cloud tenant with
  > associated CLI role permissions. Refer to [Manage API
  > keys](#UUID53429804098d70e4f8c0ac853b973a2b) for more information

- > **Install the Cortex CLI**. You can find the installation
  > instructions [here](#UUID59cee18ae22f148ccf044146d29512bb)

#### Key changes: commands and functionality

The fundamental change is the command you use to initiate a scan.
Instead of using `checkov` or `twistcli`, you must now use the `cortex`
command with its subcommands.

  -------------------------------------------------------------------------
  Prisma Cloud command     Cortex CLI command       Description
  ------------------------ ------------------------ -----------------------
  `checkov`                `cortexcli code scan`    The base command for
                                                    all scanning operations

  `twistcli images scan`   `cortexcli image scan`   The base command for
                                                    all container image
                                                    scanning operations
  -------------------------------------------------------------------------

#### Migrate Checkov use cases

Here is how to map your most common `checkov` workflows to the Cortex
CLI.

- `checkov` flags: Refer to the [CLI Command
  Reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html)

- `cortexcli` flags: Refer to [Cortex CLI common command line reference
  guide](#UUID692df6034f88296f74eba572bb9ff237) for flags common to all
  Cortex CLI, and [Cortex CLI Application Security command line
  reference](#UUID1f7b753f144f4db8dd3f589b8832d66d) for specific
  Application Security flags

#### Use case: Scan a local directory

Running a scan on your local files remains a simple and easy process.

- **Legacy **`checkov`** command**

<!-- -->

- checkov --directory  

<!-- -->

- **Cortex CLI command**

<!-- -->

- cortexcli code scan --directory

#### Use case: CI/CD pipeline integration

When updating your CI/CD pipeline, replace the legacy `checkov` step
with the new `cortex scan` command. The key difference is how you handle
authentication using your CI tool secrets management.

You can integrate the Cortex CLI directly into your CI/CD pipelines to
enable automated code scans by adding code snippets to your build script
or pipeline configuration, such as a YAML file. See
[here](#UUID5830ae85d09425056be82342bd3d52eb) for Cortex CLI snippets
(GitHub Actions, Jenkins and more).

The Cortex CLI Docker image does not support SCA scans. Therefore, if
your current workflow relies on a Dockerized version of Checkov,
you must update your pipelines to download the `cortexcli` binary
directly instead of using the Docker image.

Example: GitHub Actions workflow

These examples demonstrate a GitHub Actions workflow in both legacy and
the new Cortex CLI environments.

- **Checkov YAML step**

<!-- -->

- This example shows a typical step using `checkov-action`.

      - name: Run Checkov scan
        uses: bridgecrewio/checkov-action@v12
        with:
          directory: ./terraform
          framework: terraform
          quiet: true # Don't output results to stdout

<!-- -->

- **Cortex CLI YAML step**

<!-- -->

- This new step calls the **Cortex CLI** directly. It uses GitHub
  secrets to securely provide API credentials. This indicates a shift in
  the method of authentication, moving from a tool-specific input method
  to a more standard environment variable approach.

       name: Cortex CLI Code Scan
      on:
        push:
          branches:
            - main
        workflow_dispatch:
      env:
        CORTEX_API_KEY: ${{secrets.CORTEX_API_KEY}}
        CORTEX_API_KEY_ID: ${{secrets.CORTEX_API_KEY_ID}}
        CORTEX_API_URL: https://api-viso-cq3sdpg7uyd6vqk66ccjyv.xdr-qa2-uat.us.paloaltonetworks.com
        
      jobs:
        cortex-code-scan:
          runs-on: ubuntu-latest
          steps:
          - name: Checkout Repository
            uses: actions/checkout@v2
          
          - name: Set up Node.js
            uses: actions/setup-node@v4
            with:
              node-version: 22
          - name: Verify Node.js Version
            run: node -v
          - name: Download cortexcli
            run: |
              set -x
              crtx_resp=$(curl "${CORTEX_API_URL}/public_api/v1/unified-cli/releases/download-link?os=linux&architecture=amd64" \
                -H "x-xdr-auth-id: ${CORTEX_API_KEY_ID}" \
                -H "Authorization: ${CORTEX_API_KEY}")
              crtx_url=$(echo $crtx_resp | jq -r ".signed_url")
              curl -o cortexcli $crtx_url
              chmod +x cortexcli
              ./cortexcli --version
          - name: Run Cortex CLI Code Scan
            run: |
              ./cortexcli \
                --api-base-url "${CORTEX_API_URL}" \
                --api-key "${CORTEX_API_KEY}" \
                --api-key-id "${CORTEX_API_KEY_ID}" \
                code scan \
                --directory "${{github.workspace}}" \
                --repo-id "${{github.repository}}" \
                --branch "${{github.ref_name}}" \
                --source "GITHUB_ACTIONS" \
                --create-repo-if-missing

##### Migrate twistCLI to the Cortex CLI

Currently, only the container image scanning functions have been
migrated from twistCLI to the Cortex CLI.

Here is how to map your most common `twistcli` workflows to the Cortex
CLI.

- twistCLI flags. Refer to [Scan Images with
  twistcli](https://docs.prismacloud.io/en/enterprise-edition/content-collections/runtime-security/tools/twistcli-scan-images)

- `cortexcli` flags: Refer to [Cortex CLI common command line reference
  guide](#UUID692df6034f88296f74eba572bb9ff237) for flags common to all
  Cortex CLI, and [Cloud Workload Protection command line
  reference](#UUID8b84e152d09bf8f00504cab4f783bea0) for specific Cloud
  Workload Protection (CWP) flags

###### Use case: Scan a container image

Here is how you can map your twistCLI image scan command to the Cortex
CLI.

- **Legacy twistcli command**

<!-- -->

- ./twistcli images scan \
        --address "your Prisma Cloud Console URL" \
        --user "your_access_key_id" \
        --password "your_secret_key" \
        ubuntu:latest

<!-- -->

- **Cortex CLI command**

<!-- -->

- cortexcli image scan <container image path>

