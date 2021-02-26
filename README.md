# Hybrid_Framework_Pytest_CI 
### A hybrid framework setup in Selenium with Python implemented using pytest and continuous integration using GitHub and Jenkins

**Setup:**
1. Create a batch file
2. Push code to remote repository
3. Setup Java
4. Download Jenkins War & Setup Jenkins
5. Configure paths on jenkins
6. Setup Allure reporting options

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
