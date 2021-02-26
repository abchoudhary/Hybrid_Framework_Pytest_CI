# Hybrid_Framework_Pytest_CI 
### A hybrid framework setup in Selenium with Python implemented using pytest and continuous integration using GitHub and Jenkins

**Setup:**
1. Create batch files:
   * **Install_Library.bat:** To install the required libraries
   * **Run.bat:** To execute the test cases
    

2. Push code to remote repository
   * Add a .gitkeep file in empty folders like Logs, Reports and Screenshots to push them to remote repository
   

3. Setup Java
   * Download and install java jdk supported by jenkins. Add jdk and bin path to system environment variables
    

4. Download Jenkins War & Setup Jenkins
   * Download jenkins.war file and install using ``` java -jar jenkins.war ```
   * Unlock jenkins using administrator password
   * Install suggested plugins
   * Create first admin user and start
   

5. Configure paths on jenkins
   * Configure Java path:
     
     ```Manage Jenkins --> Global Tool Configuration --> JDK --> Add path of JAVA_HOME```
   * Configure GIT path:
     
     ```Manage Jenkins --> Global Tool Configuration --> Git --> Add path of git.exe file```
   * Configure Python path:
     
     ```Manage Jenkins --> Configure System --> Global Properties --> Environment Variables --> Add Python_Home and Python_Scripts path```
   * Setup Allure reporting :
     
     ```Manage Jenkins --> Manage Plugins --> Search and Install Allure Plugin```
   * Allure command line tool:
     
     ```Manage Jenkins --> Global Tool Configuration --> Allure Commandline --> Install automatically from maven or install locally using npm (Java 8+ & nodejs required) and provide path```


6. Configure and execution on jenkins
   * Create a new freestyle project
   * Provide GitHub repository URL in Source Code Management
   * Set Environment variable:
     
     Configure --> Build --> Execute windows batch command
     ```
     set Path=%Python_Home%;%Path%
     rmdir /s /q Reports
     rmdir /s /q allure-report
     Install_Libraries.bat
     
     ```
   * Run project using pytest:
     
      Configure --> Build --> Execute windows batch command --> Run.bat (This file contains pytest commands for execution)


7. Integrating Allure reporting:
   
   ```Configure --> Post-build Actions --> Allure Report --> Path of folder where json results are generated```
   

   * Add the below line in pytest command for allure reports:
     ```--alluredir=./Reports```
