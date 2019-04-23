## Export MySQL query data to GoogleSheets using Python

### Description
Executes a query on MySQL database, gets the data, creates a tab in a Google Sheet and dumps the data there

#### Prerequisites
To run this package, you'll need:

1. Python 2.6 or greater
2. The pip package management tool
3. MySQL connector for python   
    You can install it by executing below command
    ```
    pip install mysql-connector-python
    ```
4. A Google account which has edit access to the sheet you are trying to modify
5. Google Client Library    
    You can install it by executing below command
    ```
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```
6. Client secret JSON file   
    You will need this file to access your Google Sheet   
    In order to get one, Follow below mentioned steps
    1. Go to the [API Console](https://console.developers.google.com/).
    2. From the projects list, select a project or create a new one.
    3. If the APIs & services page isn't already open, open the console left side menu and select **APIs & services**.
    4. On the left, click **Credentials**.
    5. Click **New Credentials**, then select **OAuth client ID**. 
    6. Select **Web application** as application type for your project 
    7. If this is your first time creating a client ID, you can also configure your consent screen by clicking **Consent Screen**. You won't be prompted to configure the consent screen after you do it the first time.
    8. Click **Create client ID**
    9. Download the newly created oAuth2.0 client id as JSON
    10. Put the json file in src folder with name **credentials.json**  
 
    Refer [this](https://support.google.com/googleapi/answer/6158849?hl=en) for more help.

### How to use this script

1. Follow instructions in **[automate.py](src/automate.py)**
2. After you have made all the required changes
3. Open terminal in the project directory and execute below command
    ```
    python automate.py
    ```

#### If you are facing any issues with the script, you can email me at [contact@tirth.dev](mailto:contact@tirth.dev)

