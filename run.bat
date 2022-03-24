cd S:/SoftwareTesting_project/EcommerceApplication/
.\stest\Scripts\activate.bat
pytest -v -m "sanity" --html=reports/report_sanity_test.html testCases/ --browser chrome

rem pytest -v -m "regression" --html=reports/report_regression_test.html testCases/ --browser chrome
rem pytest -v -m "sanity and regression" --html=reports/report_sanity_regression.html testCases/ --browser chrome
rem pytest -v -m "sanity or regression" --html=reports/report_sanity_or_regression.html testCases/ --browser chrome