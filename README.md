# Assignment 2

## APP
Here is the link to my [APP](https://hafizbackpack.adaptable.app/main/)

## Questions
### 1. How do you implement the tasks in the checklist? Explain in a step-by-step manner (not just copy-paste from the tutorial).

[x] Create a new Django project.
  - First i created the directory for the project in my local folder the same name as the repository in my github
  - then i created the environment
    '''python -m venv env'''
 Create an app with the name main on that project.
 Create a URL routing configuration to access the main app.
 Create a model on the main app with name Item and these mandatory attributes:
name as the name of the item, with type CharField.
amount as the amount/count of the item, with type IntegerField.
description as the description of the item, with type TextField.
 Create a function in views.py that returns an HTML template containing your application name, your name, and your class.
 Create a routing in urls.py to map the function inviews.py to an URL.
 Deploy your app to Adaptable so it can be accessed through the internet.
### 2. Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).


### 3. What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?
  The main goal of an environment is to guarantee that dependencies, between Python projects are kept separate. This allows Python developers to have isolated environments, for each project making the development process more seamless. Technically it is possible to develop a Django web application without using an environment. However this practice is strongly discouraged, especially when working on projects that have dependencies, such, as various versions of Django. It is highly recommended to utilize environments in order to keep projects separate and avoid conflicts. This ensures development without any compatibility issues.
  
### 4. What is MVC, MVT, and MVVM? Explain the differences between the three.
#### MVC (Model-View-Controller):
Divides an app into Model (data and logic), View (user interface), and Controller (handles user input and updates Model and View).

#### MVT (Model-View-Template):
Similar to MVC but used in web frameworks like Django.
Template defines how data is shown, while Model holds data and logic.

#### MVVM (Model-View-ViewModel):
Used in front-end development.
Model stores data, View displays data, and ViewModel connects them, handling data formatting and user input.

#### Key Differences:
MVC and MVT have a Controller or Template for user input, while MVVM uses a ViewModel.
MVVM often involves data-binding for seamless UI updates.
MVT is specific to web frameworks like Django, whereas MVC and MVVM are more general architectural patterns.
