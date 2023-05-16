# PythonBehaveVenvApi

Project using Python, Behave, and Pipenv

Steps after cloning the project

Install python : python_version = "3.11" 
Install pipenv : pipenv, version 2023.4.29 
pipenv install : Install dependencies 
pipenv shell : Activate virtual environment

How to run the tests? behave features/ --tags=regression

We have two options to generate the report that Behave provides: 
behave features/ --tags=regression --junit --junit-directory reports (Genera reporte en foramto XML) 
behave features/ --tags=regression -f json (Genera rerporte en formato json)

To debug the code, we use the command: behave features/bcncgroup/verify_paragraphs_who_we_are.feature --no-logcapture --no-capture , 
remember that you need to have a breakpoint in your code like this: import pdb; pdb.set_trace()
