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
<img src="/Assets/flowchart.png">

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

# Assignment 4

## Answers

### What is UserCreationForm in Django? Explain its advantages and disadvantages.
- Django UserCreationForm is used to create a new user that can use our web applicant. it has three fields, username, password1, and password2(which is basically used for password confirmation). In summary, UserCreationForm is a powerful tool for quickly implementing user registration and authentication in Django applications. It provides a solid foundation for user management but may require customization and additional development to meet the specific needs of your application, especially if it involves complex registration workflows or additional user data.

### What is the difference between authentication and authorization in Django application? Why are both important?
-  authentication focuses on verifying user identity, while authorization focuses on controlling what authenticated users can do within the application. Together, they form a comprehensive security framework that protects both user data and the application itself. Neglecting either authentication or authorization can lead to security vulnerabilities, data breaches, and legal liabilities, making it crucial to implement both effectively in any web application.

### What are cookies in website? How does Django use cookies to manage user session data?
-  Cookies are small pieces of data that websites store on a user's web browser. Django uses cookies to manage user session data by storing a unique session ID in the user's browser. This session ID allows Django to associate the user's requests with their specific session data securely stored on the server.

### Are cookies secure to use? Is there potential risk to be aware of?
- Cookies themselves are generally secure as they are small pieces of data stored on a user's device by websites to improve user experience. However, there are potential risks associated with cookies, such as privacy concerns when they are used for tracking user behavior without consent, or the possibility of being exploited in certain types of attacks, like cross-site scripting (XSS) or cross-site request forgery (CSRF).

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
1. Implement registration, login, and logout functions to allow users to access the previous application.
    - To implement registration, we need first to make a register function inside `views.py`, this functiona automatically creates a registration form for creating an account
    ```
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
    ```
    - next we need to create a login function, that will authenticate a user after an account has been created
    ```
    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
    ```
    - And finally, we create a logout function, that will log out a user
    ```
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```
    - Lastly dont forget to add them to the `main.html` and `urls.py`

2. Create two user accounts with three dummy data entries for each account using the model previously created in the application.
    - To create the users and the data, first we need to run the server,`python manage.py runserver`, and access it with http://localhost:8000/login, after creating the account and logged in, we then can make the dummy data

3. Connect Item model with User.
    - In `models.py` modified the user variables into
    ```
    class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```
    where it will make a connection from product to a user'
    - then modify the `create_product` method 
    ```
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    ```
    this associates the product with the current logged in user, then saves it into the database. `Commit = False` allows for additional costumization of object before saving

4. Display the information of the logged-in user, such as their username, and applying cookies, such as last login, on the main application page.
    - modify the `login_user` and `logout_user` function in `views.py`
    ```
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ```
    thiw will set a cookie indicating their last login time
    ```
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
    this will delete a specific cookie related to their login time

    - add it to the `show_main` function, inside `context`
    ```
    'last_login': request.COOKIES['last_login'],
    ```
    where will be used to diplay on the webpage

5.  Create two user accounts with three dummy data entries for each account using the model previously created in the application.
<img src="/Assets/Robert.PNG">
<img src="/Assets/hubert.PNG">