# Assignment 2

## APP
Here is the link to my [APP](https://hafizbackpack.adaptable.app/main/)

## Questions
### 1. How do you implement the tasks in the checklist? Explain in a step-by-step manner (not just copy-paste from the tutorial).

#### 1. Create a new Django project
  - first i create a new Django Project by creating the virtual environment
  ---
  python -m venv env
  ---
  - to activate virtual environment
  ---
  env\Scripts\activate
  ---
  - then i added a file which contains some dependecies named 'requirements.txt'
  - i then run the the command
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
