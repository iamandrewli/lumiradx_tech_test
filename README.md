[Introduction](#introduction) | [Test plan](#test-plan) | [Test completion report](#test-completion-report) | [Defects](#defects) | [Automated test set up](#automated-test-set-up) |[Manual test set up](#manual-test-set-up) |

---

Introduction
-----
This is my submission for the LumiraDX technical task.  Here you will find a guide on tests plan that I created, my testing results and instructions on how to view them and a list of bugs raised.


Test plan
-----
A high level test plan was created an can be reviewed here:
https://github.com/iamandrewli/lumiradx_tech_test/blob/master/LumiraDX%20Technical%20Test%20–%20High%20Level%20Test%20Plan.docx


Test completion report
-----
The test completion report can be found here:
https://github.com/iamandrewli/lumiradx_tech_test/blob/master/LumiraDX%20Technical%20Test%20–%20Test%20completion%20report.docx


Defects
-----

A list of defects can be found here:
https://github.com/iamandrewli/lumiradx_tech_test/issues


Automated test set up
-----

Download the tests from:
https://github.com/iamandrewli/lumiradx_tech_test/tree/master/automated_integration_tests

* Use the same venv that you created for the lumiradx tech test found here:
https://github.com/amaccormack-lumira/rest_api_demo/blob/master/README.md

From the same venv
* pip install requests
* pip install pytest
* run tests by going to the *automated_integration_test* directory and run the command 'pytest TESTNAME' e.g. pytest put_test.py 


Manual test set up
-----
Manual test were created and executed with the use of Postman.

These steps will walk you through how to set up and access the test scenarios.

Firstly, download the postman app from:
https://www.postman.com/downloads/

Access the manual test scenarios from:
https://github.com/iamandrewli/lumiradx_tech_test/blob/master/Lumiradx.postman_collection.json

Once downloaded, open the postman app.  Click the import button from the top left hand corner.  Find the Lumiradx.postman_collection.json and expand the LumiraDX folder.
