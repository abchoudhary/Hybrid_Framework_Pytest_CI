# Hybrid_Framework_Pytest_CI 
### A hybrid framework setup in Selenium with Python implemented using pytest and continuous integration using GitHub and Jenkins

**Setup:**
1. Create batch files:
   * "Install_Library.bat" - To install required libraries
   * "Run.bat" - To execute the test cases
    

2. Push code to remote repository
   

3. Setup Java
   * Download and install java jdk supported by jenkins. Add jdk and bin path to environment variables
    

4. Download Jenkins War & Setup Jenkins
   * Download jenkins.war file and install using ``` java -jar jenkins.war ```
   * Unlock jenkins using administrator password
   * Install suggested plugins
   * Create first admin user and start
   

5. Configure paths on jenkins
   * Configure Java path : Manage Jenkins -> Global Tool Configuration -> JDK
   * Configure GIT path : Manage Jenkins -> Global Tool Configuration -> Git
   * Configure Python path : Manage Jenkins -> Configure System -> Global Properties -> Environment Variable -> add python home and python scripts path
   * Setup Allure reporting : Manage Jenkins -> Manage Plugins -> Search and Install Allure Plugin
   * Allure command line tool: Download allure command line tool zip file and extract it, In Jenkins goto Manage Jenkins -> Global Tool Configuration -> Allure Commandline and provide the path

6. Configure and execution on jenkins
   * Create a new freestyle project
   * Provide GitHub repository url in source code management
   * Set Environment variable : Build -> Execute windows batch command -> set Path=%Python_Home%;%Path%
   * Run batch file to install libraries -> Install_Libraries.bat
   * Run test cases using pytest: Build -> Execute windows batch command -> Run.bat (the bat file has the pytest execution command)
   Note: In order to push the empty folders like Logs, Reports and Screenshots to remote repository, add a .gitkeep file


7. Generating Allure reports

**Folder Structure:**
```
Project
├── Configurations
│   ├── config.ini (to store common info like application URL)
|
├── pageObjects(package)
|   ├── page_object_file.py (contains webelements, getter and setter methods)
|
├── testCases(package)
|   ├── conftest.py (contains pytest fixtures for browser and reports etc.)
|   ├── pytest.ini (to store custom pytest markers)
|   ├── test_filename.py (contains test methods)
|    
├── utilities(package)
|   ├── custom_logger.py (contains logging setup)
|   ├── read_properties.py (to read data from config.ini by using configparser)
|   ├── excelUtils.py (to read test data from excel file for data driven testing) 
|
├── Logs
├── Reports
├── Screenshots
├── TestData
├── README.md
└── Run.bat (To execute test cases)
```
