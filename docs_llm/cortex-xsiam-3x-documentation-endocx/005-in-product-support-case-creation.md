## In-product support case creation

To simplify the process of creating a support case, you can open a
support case directly in Cortex XSIAM. Opening the case in Cortex XSIAM
allows all of the relevant context to be included, such as the option to
record the console and upload relevant logs. When relevant, Cortex XSIAM
will create and send the agent tech support file (TSF) for the endpoint
you select. All relevant data about your tenant is logged and included
in the support case, including license details. Using the Cortex XSIAM
**Create Support Case Wizard** makes it easier for you to include all of
the necessary details and log files while first submitting your support
case, thereby enabling the support team to solve it more quickly and
easily.

To use the embedded support case feature, you must have a user account
in the Customer Support Portal, and your Cortex XSIAM user must be
granted the **Help** permission in Cortex Gateway.

1.  From Cortex XSIAM, select Help \> Submit a Support Case.

2.  In the **Submit Support Case** wizard, enter the requested case
    information. Be precise when indicating the impact of the issue.
    When an issue is critical, you will be asked to input the most
    critical information so that support can understand the issue and
    start addressing it immediately.

- > **Note**

  > When opening a support case through the Customer Support Portal, you
  > need to manually select Cortex XSIAM as the product. While there may
  > be discrepancies between the categories in this wizard and the
  > Customer Support Portal process, that\'s because this wizard is
  > designed specifically to focus on options relevant to Cortex XSIAM.

3.  When the issue you are opening a support case for is related to the
    agent, you can select the relevant endpoint. If you select the
    endpoint, Cortex XSIAM will create and send the TSF for the agent
    you selected, when possible.

- > **Note**

  > Selecting an endpoint from the endpoint table and retrieving TSF
  > requires full **Retrieve Endpoint Data** permissions
  > under **Endpoint Administration**.

4.  To provide more context for your support case, you can record the
    Cortex XSIAM console directly from the support case wizard. If you
    choose to record the console, you can also opt to have the HAR file
    generated and sent to further assist support in solving the case. To
    record the console, select **Record Console**. To submit your
    support case without recording the console, select **Skip**.

5.  If you choose to record the console, your browser may prompt you for
    permission for Cortex XSIAM to see the contents of the tab. To allow
    recording, select **Allow**. You can now recreate the issue in your
    Cortex XSIAM environment and all of your actions are recorded. The
    console recording and HAR file generation only take place within the
    context of the browser tab that Cortex XSIAM is running in. When you
    are ready to stop recording, select **Stop Sharing**.

- If you wish to recreate the recording, you must first delete the
  existing console recording by clicking the **x** symbol next to the
  **Console Recording**. Then select **Record Console**.

  > **Note**

  > Console recordings cannot exceed 10 minutes. The current recording
  > time is displayed at the top of the window.

6.  To submit the support case, click **Submit Support Case**.

- While the case attachments are uploading, do not refresh or navigate
  away from Cortex XSIAM until you get a notification in the
  Notification Center that uploading is complete. In the meantime, you
  can close this wizard and continue working in Cortex XSIAM.

  Once the support case is created successfully, the support case number
  is displayed and you will receive an email notification from Palo Alto
  Networks Support. You can manage the support case and monitor its
  progress in the Customer Support Portal.

