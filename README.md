# Assignment 2

## APP
Here is the link to my [APP](https://hafizbackpack.adaptable.app/main/)

## Questions
### 1. How do you implement the tasks in the checklist? Explain in a step-by-step manner (not just copy-paste from the tutorial).

[x] Create a new Django Project
    - first i created the repository on github, corresponding to my local directory for the project
    - To create a new Django Project first we need to create a virtual environment in command prompt
    ```
    python -m venv env
    ```
    - Then activate the virtual environment
    ```
    env\Scripts\activate
    ```
    - then i added a txt files containing some required dependecies with the name requirements.txt
    - while the environment is still active, i ran the comment
    ```
    pip install -r requirements.txt
    ```
    - then i created the django project with the command:
    ```
    django-admin startproject HafizBackpack .
    ```
    - a `main` folder will appear
    - then go into the `settings.py` file, and added "*" in the `ALLOWED_HOSTS`, which is a security measure to prevent HTTP Host header attacks
    - and lastly added a .gitignore file
[x] Create an app with the name `main`.
    - i ran this comment so that the initial structure appear
    ```
    python manage.py startapp main
    ```
    - in `settings.py` i added 'main' in the `INSTALLED_APPS` section
    - then i created a folder named `templates` inside the `main` directory and added `main.html` inside the folder
4. Create a URL routing configuration to access the `main` app.
    - in `urls.py`file, i added `path('main/', include('main.urls'))` to connect it to the main view.
5. Create a model on the `main` app with name `Item` and add some mandatory attributes
    - Inside `models.py` i added extra attributes such as:
        - `name`
        - `date_added`
        - `amount`
        - `description`
        - `fruit_type`
6. Create a function in `views.py` that returns an HTML template containing my application name, your name, and your class.
    - i added all the required description corresponding to the checklist in the show_main function
    - with this line to returns the main.html
    ```
    return render(request, 'main.html', context)
    ```
7. Create a routing in `urls.py` to map the function in `views.py` to an URL
    - inside the `urls.py` in my HafizBackpack directory, i added the url pattern
    ```
    path('main/', include('main.urls'))
    ```
8. Deploy the app to adaptable
    - Add, commit, push the project to my repo in github
    - in Adaptable, i choose my repo to be deployed
    - using Python App template as the template, Postgresql as the databse type and added the command 
    ```
    python manage.py migrate && gunicorn shopping_list.wsgi
    ```
    - before deployinh the app
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
