# Assignment 2

## APP
Here is the link to my [APP](https://hafizbackpack.adaptable.app/main/)

## Questions
### 1. How do you implement the tasks in the checklist? Explain in a step-by-step manner (not just copy-paste from the tutorial).

1. Create a new Django Project.

    - first i created the repository on github, corresponding to my local directory for the project.
    - To create a new Django Project first we need to create a virtual environment in command prompt.
    ```
    python -m venv env
    ```
    - Then activate the virtual environment.
    ```
    env\Scripts\activate
    ```
    - then i added a txt files containing some required dependecies with the name requirements.txt.
    - while the environment is still active, i ran the comment.
    ```
    pip install -r requirements.txt
    ```
    - then i created the django project with the command:
    ```
    django-admin startproject HafizBackpack .
    ```
    - a `main` folder will appear.
    - then go into the `settings.py` file, and added "*" in the `ALLOWED_HOSTS`, which is a security measure to prevent HTTP Host header attacks.
    - and lastly added a .gitignore file.
2. Create an app with the name `main`.
    - i ran this comment so that the initial structure appear.
    ```
    python manage.py startapp main
    ```
    - in `settings.py` i added 'main' in the `INSTALLED_APPS` section.
    - then i created a folder named `templates` inside the `main` directory and added `main.html` inside the folder.
4. Create a URL routing configuration to access the `main` app.
    - in `urls.py`file, i added `path('main/', include('main.urls'))` to connect it to the main view.
5. Create a model on the `main` app with name `Item` and add some mandatory attributes.
    - Inside `models.py` i added extra attributes such as:
        - `name`
        - `date_added`
        - `amount`
        - `description`
        - `fruit_type`
6. Create a function in `views.py` that returns an HTML template containing my application name, your name, and your class.
    - i added all the required description corresponding to the checklist in the show_main function.
    - with this line to returns the main.html.
    ```
    return render(request, 'main.html', context)
    ```
7. Create a routing in `urls.py` to map the function in `views.py` to an URL.
    - inside the `urls.py` in my HafizBackpack directory, i added the url pattern.
    ```
    path('main/', include('main.urls'))
    ```
8. Deploy the app to adaptable.
    - Add, commit, push the project to my repo in github.
    - in Adaptable, i choose my repo to be deployed.
    - using Python App template as the template, Postgresql as the databse type and added the command .
    ```
    python manage.py migrate && gunicorn shopping_list.wsgi
    ```
    - before deploying the app.
### 2. Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).
<img src="/flowchart.png">

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

# Assignment 3

## Answers

### What is the difference between POST form and GET form? 
- we use GET when you want to retrieve data from the server without modifying it, on the other hand we use POST when you want to send data to the server to create, update, or perform other actions that may have side effects.

### What are the main differences between XML, JSON, and HTML in the context of data delivery?
- HTML serves as the foundational language for web development, primarily responsible for defining the structure and content of web pages. On the other hand, JSON and XML are both used for data transport between servers, but they each have distinct characteristics. JSON is ideal for lightweight data interchange and JavaScript integration, while XML is better suited for structured and self-describing data with custom tags and attributes.

### Why is JSON often used in data exchange between modern web applications?
- JSON is frequently employed in data exchange between modern web applications because of its efficiency, simplicity, and seamless integration with JavaScript, which is a fundamental language for web development.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
1. Create a form input to add a model object to the previous app.
    - First i create a new file inside the `main` folder named `forms.py`, where fields from the `models.py` will be accepted
2. Create a function to accepts `request` parameter
    - i named the function as `create_product` where it checks if the form submitted is valid then saved and add the new product
      ```python
      def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)
      ```
4. Modify the `show_main` function in `views.py`
    - i Added `Products.objects.all` and added a `counter` to count how many items has been added later on in the interface
5. Creating multiple lines in to view the added objects in `views.py`. 
    - in `views.py` i added 4 function named `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id`, which each function is used to translate an object to a different format corresponding to the function.
6. Adding urls path in `urls.py` including the `create_product`  function.
    - in the `urlpatterns` i added 5 new path for xml, json, xml by id, json by id and the `create_product` function
    ```python
     path('json/', show_json, name='show_json'),
    ```

### Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
<img src="/Assets/json.PNG">
<img src="/Assets/jsonbyid.PNG">
<img src="/Assets/XML.PNG">
<img src="/Assets/xmlbyid.PNG">
<img src="/Assets/main.PNG">
