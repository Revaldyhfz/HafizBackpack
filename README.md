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

# Assignment 4

## Answers

### Explain the purpose of some CSS element selector and when to use it.
- The element selector in CSS is used to select and style HTML elements based on their tag names. For example, to style all `<p>` elements on a webpage, you can use the p selector in your CSS. Element selectors are useful when you want to apply a consistent style to a specific type of HTML element throughout your website.

### Explain some of the HTML5 tags that you know.
- `<a>` Defines a hyperlink.
- `<b>` Displays text in a bold style.
- `<div>` Specifies a division or a section in a document.
- `<form>` Defines an HTML form for user input.
- `<head>` Defines the head portion of the document that contains information about the document such as title.
- `<nav>` Defines a section of navigation links

### What are the differences between margin and padding?
#### Margin: 
- Margin is the space outside an element's border. It creates space between the element and other elements around it. Margin affects the spacing between elements but does not impact the element's background or border.

#### Padding: 
- Padding is the space inside an element's border. It creates space between the element's content and its border. Padding affects the element's background and content but does not impact its position relative to other elements.

### What are the differences between the CSS framework Tailwind and Bootstrap? When should we use Bootstrap rather than Tailwind, and vice versa?
#### Tailwind CSS:
- Tailwind is a utility-first CSS framework. It provides a large set of utility classes that allow you to style elements by applying classes directly in your HTML markup. Tailwind is highly customizable and suitable for projects where you want complete control over the styling.

#### Bootstrap: 
- Bootstrap is a more opinionated CSS framework that comes with pre-designed components and a responsive grid system. It requires less custom styling and is great for quickly prototyping or building consistent-looking websites.

#### When to use Bootstrap or Tailwind depends on the project:
- Bootstrap: Use Bootstrap when you want to rapidly develop a responsive website with a predefined look and feel. It's great for projects with tight deadlines or when you don't want to write much custom CSS.

- Tailwind CSS: Use Tailwind when you want full control over your styling and prefer to design your components using utility classes. It's ideal for projects where customization and a unique design are a priority.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).

1. Customize the HTML templates that you have created in Assignment 4 using CSS or any CSS framework (Bootstrap, Tailwind, Bulma, etc.):
- i chose Tailwind since ive had experienced with it beforehand
- here are the Templates i modified using Tailwind
- i did use a few tools to help me design my page which is [Flowbite](https://flowbite.com/) & [Tailwind](https://tailwindcss.com/), where both websites help me to understand and get ideas to design it
- here's an example of one of my modified templates
- `main.html`
```
{% extends 'base.html' %}

{% block content %}
{% include 'navbar.html' %}

<h1 class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">Welcome 
    <span class="underline underline-offset-3 decoration-8 decoration-blue-400 dark:decoration-blue-600 text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-400">
        {{name}}
    </span>
</h1>
    
<p class="text-gray-500 dark:text-gray-400">You have saved <a href="#" class="font-semibold text-gray-900 underline dark:text-white decoration-indigo-500">{{counter}}</a> Fruits in your Backpack
</p>

<h5 class="text-gray-500 dark:text-gray-400">Last login session: {{ last_login }}</h5>
<br/>

<div class="relative flex justify-center space-x-4">
    <a href="{% url 'main:create_product' %}">
        <button type="button" class="flex items-center text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 shadow-lg shadow-blue-500/50 dark:shadow-lg dark:shadow-blue-800/80 font-medium rounded-lg text-sm px-6 py-2.5 text-center">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mr-2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Add New Product
        </button>
    </a>  
</div>
<br />
<div class="relative overflow-x-auto rounded-lg shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th scope="col" class="px-6 py-3">Name</th>
                <th scope="col" class="px-6 py-3">Amount</th>
                <th scope="col" class="px-6 py-3">Description</th>
                <th scope="col" class="px-6 py-3">Date Added</th>
                <th scope="col" class="px-6 py-3">Fruit Type</th>
                <th scope="col" class="px-6 py-3">Modify</th>
            </tr>
        </thead>

        {% comment %} Below is how to show the product data {% endcomment %}
        <tbody>
        {% for product in products %}
            <tr class="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
                <td  scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    {{product.name}}
                </td>
                <td class="px-6 py-4">
                    <div class="relative flex items-center">
                        <form method="post">
                            {% csrf_token %}
                            <button class="inline-flex items-center justify-center p-1 text-sm font-medium h-6 w-6 text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700" type="submit" value="{{ product.id }}" name="increment">
                                
                                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
                                </svg>
                            </button>
                            <div class="mx-2">
                                {{product.amount}}
                            </div>
                            <button class="inline-flex items-center justify-center h-6 w-6 p-1 text-sm font-medium text-gray-500 bg-white border border-gray-300 rounded-full focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700" type="submit" value="{{ product.id }}" name="decrement">
                            
                                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 2">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h16"/>
                                </svg>
                            </button>
                        </form>
                    </div>
                </td>
                <td class="px-6 py-4">{{product.description}}</td>
                <td class="px-6 py-4">{{product.date_added}}</td>
                <td class="px-6 py-4">{{product.fruit_type}}</td>
                <td> 
                    <a href="{% url 'main:delete_product' product.pk %}">
                        <button class="text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 shadow-lg shadow-red-500/50 dark:shadow-lg dark:shadow-red-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
                            Remove
                        </button>   
                    </a>
                    
                    <a href="{% url 'main:edit_product' product.pk %}">
                        <button class="text-white bg-gradient-to-r from-green-400 via-green-500 to-green-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-green-300 dark:focus:ring-green-800 shadow-lg shadow-green-500/50 dark:shadow-lg dark:shadow-green-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
                            Edit
                        </button>
                    </a>
                </td>
            </tr>
        {% endfor %}
        </tbody>
    </table>
</div>

<div class="relative flex justify-center space-x-4">
    <a href="{% url 'main:logout' %}">
        <button type="button" class="flex items-center text-white bg-black hover:bg-gradient-to-r from-teal-400 via-teal-500 to-teal-600 focus:ring-4 focus:outline-none focus:ring-teal-300 dark:focus:ring-teal-800 shadow-lg shadow-teal-500/50 dark:shadow-lg dark:shadow-teal-800/80 font-medium rounded-lg text-sm px-6 py-2.5 text-center border border-gray-800 dark:border-gray-600">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mr-2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15m3 0l3-3m0 0l-3-3m3 3H9" />
            </svg>
            Logout
        </button>
    </a>
</div>
    
{% endblock content %}

```
- i added `<div>` to all the elements including the heading, texts and buttons
- from flowbite, i searched up some templates, and adapt them to my page using resources from tailwind.css

