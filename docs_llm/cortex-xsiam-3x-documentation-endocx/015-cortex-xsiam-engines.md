## Cortex XSIAM engines

Engines are installed in a remote network and allow communication
between the remote network and Cortex XSIAM. You can run integration
commands on an engine. It is possible to install a single engine or
multiple engines.

You can install multiple engines on the same machine (Shell installation
only) which is useful in a dev-prod environment where you do not want to
have numerous engines in different environments, and to manage those
machines.

### Engine requirements

You can install engines on all Linux environments. Docker/Podman needs
to be installed before installing an engine. If you are using the shell
installer for an engine, Docker/Podman is installed automatically.

> **Note**
>
> The Cron package is required to install engines on a Linux machine.

**Engine hardware requirements**

If your hard drive is partitioned, we recommend a minimum of 50 GB for
the `/var` partition.

  -----------------------------------------------------------------------
  Component               Dev Environment Minimum Production Minimum
  ----------------------- ----------------------- -----------------------
  CPU                     8 CPU cores             16 CPU cores

  Memory                  16 GB RAM               32 GB RAM

  Storage                 100 GB                  100 GB
  -----------------------------------------------------------------------

**Operating system requirements**

You can deploy a Cortex XSIAM engine on the following operating systems:

+-----------------------------------+-----------------------------------+
| Operating System                  | Supported Versions                |
+===================================+===================================+
| Ubuntu                            | 18.04, 20.04, 22.04               |
+-----------------------------------+-----------------------------------+
| RHEL                              | 8.x, 9.x                          |
|                                   |                                   |
|                                   | Includes all minor versions.      |
+-----------------------------------+-----------------------------------+
| Oracle Linux                      | 7.x, 8.9, 9.3, 9.4                |
+-----------------------------------+-----------------------------------+
| Amazon Linux                      | 2, Amazon Linux 2023              |
+-----------------------------------+-----------------------------------+
| Rocky Linux                       | 9.5                               |
+-----------------------------------+-----------------------------------+

> **Note**
>
> CentOS 8.x reached End of Life (EOL) on December 31, 2021, and is no
> longer supported as an operating system.
>
> CentOS 7.x reached End of Life (EOL) on June 30, 2024, and is no
> longer supported as an operating system.

**Engine required URLs**

You need to allow the following in the URLs for Cortex XSIAM engines to
operate properly. The URLs are needed to pull container images from
public Docker registries.

The endpoint URL
is: `wss://api-<tenant domain>.xdr.<region>.paloaltonetworks.com/xsoar/d1ws`.
For example,
`wss://api-my-tenant.xdr.us.paloaltonetworks.com/xsoar/d1ws`

+-----------------+--------------------------------------------+----------------------+-----------------+
| FUNCTION        | SERVICE                                    | PORT                 | DIRECTION       |
+=================+============================================+======================+=================+
| Integrations    |                                            | Integration-specific | Outbound        |
|                 |                                            | ports                |                 |
+-----------------+--------------------------------------------+----------------------+-----------------+
| Engine          | HTTPS                                      | 443 (configurable)   | Outbound        |
| connectivity    |                                            |                      |                 |
+-----------------+--------------------------------------------+----------------------+-----------------+
| Docker          | - https://registry-1.docker.io             | 443                  | Outbound        |
|                 |                                            |                      |                 |
|                 | - https://registry.fedoraproject.org       |                      |                 |
|                 |                                            |                      |                 |
|                 | - https://registry.access.redhat.com       |                      |                 |
|                 |                                            |                      |                 |
|                 | - https://docker.io                        |                      |                 |
|                 |                                            |                      |                 |
|                 | - https://registry.docker.io               |                      |                 |
|                 |                                            |                      |                 |
|                 | - https://auth.docker.io                   |                      |                 |
|                 |                                            |                      |                 |
|                 | <!-- -->                                   |                      |                 |
|                 |                                            |                      |                 |
|                 | - This URL may change at Docker's          |                      |                 |
|                 |   discretion.                              |                      |                 |
|                 |                                            |                      |                 |
|                 | <!-- -->                                   |                      |                 |
|                 |                                            |                      |                 |
|                 | - https://production.cloudflare.docker.com |                      |                 |
|                 |                                            |                      |                 |
|                 | <!-- -->                                   |                      |                 |
|                 |                                            |                      |                 |
|                 | - This URL may change at Docker's          |                      |                 |
|                 |   discretion.                              |                      |                 |
+-----------------+--------------------------------------------+----------------------+-----------------+

### Install an engine

When you install the engine, the `d1.conf` is installed on the engine
machine, which contains engine properties such as proxy, log level, and
log files. If Docker/Podman is already installed, the
`python.engine.docker` and `powershell.engine.docker` keys are set to
`true`. If Docker or Podman is not available when the engine is
installed, the key is set to `false`. If so, you need to set the key to
`true` after installing Docker and Podman. Verify that
`python.engine.docker` and `powershell.engine.docker` configuration keys
are present in the `d1.conf` file.

> **Note**
>
> If you are using DEB, RPM, or Zip installation, install Docker or
> Podman.
>
> Natively running Python or PowerShell integrations/scripts on Windows
> or Linux is not supported on Cortex XSIAM engines.

#### Installation types

Cortex XSIAM supports the following file types for installation on the
engine machine:

- **Shell:** For all Linux deployments, including Ubuntu and SUSE.
  Automatically installs Docker/Podman, downloads Docker/Podman images,
  enables remote engine upgrade, and allows installation of multiple
  engines on the same machine.

<!-- -->

- The installation file is selected for you. Shell installation supports
  the purge flag, which by default is false. To uninstall an engine, run
  the installer with the purge flag enabled.

  > **Note**

  > When upgrading an engine that was installed using the Shell
  > installation, you can use the **Upgrade Engine** feature in the
  > **Engines** page. For Amazon Linux 2 type engines, you need to
  > upgrade these engine types using a zip-type engine and not use the
  > **Upgrade Engine** feature.

  > If you use the shell installer, Docker/Podman is automatically
  > installed. We recommend using Linux and not Windows to be able to
  > use the shell installer, which installs all dependencies.

<!-- -->

- **DEB:** For Ubuntu operating systems.

- **RPM:** RHEL operating systems.

<!-- -->

- > **Note**

  > Use DEB and RPM installation when the shell installation is not
  > available. You need to manually install
  > [Docker](#UUIDc2a4633cc8904adf2a1322b040573124) or
  > [Podman](#UUIDe52020e8425c72ad475a16b5073ca96c) and any
  > dependencies.

<!-- -->

- **Zip:** Used for Amazon Linux 2 machines.

- **Configuration:** Configuration file for download. When you install
  one of the other options, this configuration file (`d1.conf` ) is
  installed on the engine machine.

> **Important**
>
> For DEB/RPM engines, Python (including 3.x) and the containerization
> platform (Docker/Podman) must be installed and configured. For Docker
> or Podman to work correctly on an engine, [IPv4
> forwarding](https://docs.docker.com/network/bridge/#enable-forwarding-from-docker-containers-to-the-outside-world)
> must be enabled.

#### How to install an engine

1.  Create an engine.

    a.  Select Settings \> Configurations \> Data Broker \> Engines \>
        Create New Engine.

    b.  In the **Engine Name** field, add a meaningful name for the
        engine.

    c.  Select one of the installer types from the list.

    d.  (*Optional*) (*Shell only*) Select the checkbox to enable
        multiple engines to run on the same machine.

    - If you have an existing engine, and you did not select the
      checkbox, and now you want to install another engine on the same
      machine, you need to delete the existing engine.

    e.  (*Optional*) Add any required configuration in JSON format.

    f.  Click **OK** to create the engine.

2.  For shell installation, do the following:

- > **Tip**

  > For Linux systems, we recommend using the shell installer. If using
  > Amazon Linux 2, use the zip installer (see step
  > [4](#N1716185281356)).

  a.  Move the `.sh` file to the engine machine using a tool such as SSH
      or PuTTY.

  b.  On the engine machine, grant execution permission by running the
      following command:

  - `chmod +x /<engine-file-path>`

  c.  Install the engine by typing one of the following commands:

  - With tools: `sudo <engine-file-path>`

    Without tools: `sudo <engine-file-path> -- -tools=false`

    > **Note**

    > If you receive a `permissions denied` error, it is likely that you
    > do not have permission to access the `/tmp` directory.

    > If the installer fails to start due to a permissions issue, even
    > if running as root, add one of the following two arguments when
    > running the installer:

    - > `--target <path>` - Extracts the installer files into the
      > specified custom path.

    - > `--keep` - Extracts the installer files into the current working
      > directory (without cleaning at the end).

    > If using installer options such as `-- -tools=false`, the option
    > should come after the `--target` or `--keep` arguments. For
    > example:

    > `sudo ./d1-installer.sh --target /some/temp/dir -- -tools=false`

    > If you set a custom path when you run the installer, you must also
    > set a custom path for upgrading your engine or the upgrade will
    > fail. For more information, see
    > [/document/preview/1199417#UUID-3a9e655c-6f7e-2566-d416-29991d7d1d3b](/document/preview/1199417#UUID-3a9e655c-6f7e-2566-d416-29991d7d1d3b).

3.  For RPM/DEB installation, do the following:

    a.  Move the file to the required machine using a tool such as SSH
        or PuTTY.

    b.  Type one of the following installation commands:

  -------------------------------------------------------------------------------
  Machine Type                        Install Command
  ----------------------------------- -------------------------------------------
  RHEL (RPM)                          `sudo rpm -Uvh d1-2.5_15418-1.x86_64.rpm`

  Ubuntu (DEB)                        `sudo dpkg --install d1_xxx_amd64.deb`
  -------------------------------------------------------------------------------

c.  Start the engine by running one of the following commands:

  -----------------------------------------------------------------------
  Machine Type                        Start Command
  ----------------------------------- -----------------------------------
  RHEL (RPM)                          `sudo systemctl start d1`

  Ubuntu (DEB)                        `sudo service d1 restart`
  -----------------------------------------------------------------------

4.  For Zip installation on Amazon Linux 2, run the following commands:

    a.  Create the engine folder.

    - `mkdir /usr/local/demisto`

    b.  Unzip the engine files to the folder created in the previous
        step.

    - `unzip ./d1.zip -d /usr/local/demisto`

    c.  Allow the process to bind to low-numbered ports.

    - `setcap CAP_NET_BIND_SERVICE=+eip /usr/local/demisto/d1_linux_amd64`

    d.  Change the owner of `/usr/local/demisto` to the demisto user.

    - `chown -R demisto:demisto /usr/local/demisto`

    e.  In `/etc/systemd/system` edit the `d1.service` file as follows
        (adjust the directory and the name of the binary file if
        needed).

    -  [Unit]
          Description=Demisto Engine Service
          After=network.target
          [Service]
          Type=simple
          User=demisto
          WorkingDirectory=/usr/local/demisto
          ExecStart=/usr/local/demisto/d1_linux_amd64
          EnvironmentFile=/etc/environment
          Restart=always
          [Install]
          WantedBy=multi-user.target

    f.  Run the following commands:

    - `chown root:root /etc/systemd/system/d1.service`

      `chmod 644 /etc/systemd/system/d1.service`

    g.  Run the engine process.

    - `systemctl start d1`

    h.  Verify that the engine is running.

    - `systemctl status d1`

5.  Verify that the engine you created is connected.

    a.  Select Settings \> Configurations \> Data Broker \> Engines.

    b.  Locate your engine on the **Engines** page and check that it is
        connected.

6.  When the engine is connected, you can add the engine to a
    load-balancing group by clicking **Load-Balancing Group** on the
    Engines page.

- If you want to add the engine to a new group, click
  **Add to new group** from the list.

  When the engine is in the load-balancing group, it cannot be used as
  an individual engine and does not appear when configuring an engine
  from the list.

7.  (Optional) After installing the engine, you may want to set up a
    proxy, set up Docker hardening, configure the number of workers for
    the engine, or perform other related engine configurations. For more
    information, see [Configure
    Engines](#UUIDea7bc684741f4281cb5dab7fed8d5acb). You can also
    configure an integration instance to run on the engine you created.

