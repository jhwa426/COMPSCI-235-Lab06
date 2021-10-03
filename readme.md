# COMPSCI-235-Lab-6-People-with-DB

## Description

This is the repository for Lab 6 (Week 9) of COMPSCI 235 at the University of Auckland.

In this weeks lab we will develop this simple web application further by using SQLAlchemy to integrate an SQLite Database to persist data.

<a href="https://canvas.auckland.ac.nz/courses/60516/pages/lab-6-week-9-sqlalchemy-flask-databases">Further description and instructions for the lab can be found on the canvas page.</a>

## Installation

**Installation via requirements.txt**

```shell
$ cd COMPSCI-235
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm, set the virtual environment using 'File'->'Settings' and select 'Project:COMPSCI-235' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 

## Execution

**Running the application**

From the *COMPSCI-235* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
```` 

The homepage can be accessed from a Web browser:

http://127.0.0.1:5000/

 
