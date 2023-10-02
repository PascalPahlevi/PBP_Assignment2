# PBP_Assignment2

"DISCLAIMER: This is an academic assignment. Use of copyrighted materials are all owned by the respective companies and media responsible for its products and/or intellectual property."

URL:

1. To begin with this assignment, I started by creating a Django project first, in order to do so making sure I installed the right dependencies, I created a new directory as well as initialized a new virtual environment. Afterwards, I created a text file with all the dependencies I needed and installed them before eventually creating the Django project. Once I did all those, I made sure first that I was able to run the server and once I had done that, I uploadaed the files into a newly created github repository. <br>

   After finishing with the intial setup, I started working on the html file which I named as "main". This file would then be inserted a new folder named "template" and in doing so made it easier to separate the main.html with the other files. With the html file created, I was then able to make and add changes which I see fit the theme of my app and further proceeded with the URl routing. In doing so, I was able to make sure that the "main.html" would be displayed when the url is visited. Finally, I finished everything by deploying the app using Adaptable.

2.
   ![image](https://github.com/PascalPahlevi/PBP_Assignment2/assets/143638456/a2031cb2-5a30-4533-8f64-53b6e78f3119)

3. <img width="1280" alt="image" src="https://github.com/PascalPahlevi/PBP_Assignment2/assets/143638456/ef1dc1d1-c81b-4a48-a5d8-ae43a7b6c6b3">
<img width="1280" alt="image" src="https://github.com/PascalPahlevi/PBP_Assignment2/assets/143638456/dbbd92c8-a505-42a5-a631-eb1dd9e71dfe">
<img width="1280" alt="image" src="https://github.com/PascalPahlevi/PBP_Assignment2/assets/143638456/686fe912-ec24-4349-9547-c246f98a2840">
<img width="1280" alt="image" src="https://github.com/PascalPahlevi/PBP_Assignment2/assets/143638456/39f1ab71-4612-4d90-8512-7baa782a78f2">
<img width="1280" alt="image" src="https://github.com/PascalPahlevi/PBP_Assignment2/assets/143638456/f3182564-5df6-4531-aa6a-baf7a4ca1f45">

4. The purpose of a virtual environment is to help install the required packages for different projects and isolating them in different environments. Since a Django web app requires multiple packages and dependencies, a virtual environment must be used to create one.

5. MVC, MVT, and MVVM are all frequently used design templates. The MVC framework can be separated into three main components: Model, View, Controller. This framework provides a separation between UI logic, input logic, and business logic and is one of the most frequently used web development frameworks currently. The MVT framework is a design pattern for web development which is separated into three main components: Model, View, Template. This structure is typically used for Django projects. The MVVM is a framework that solves all the problems that the MVT and MVC have. This framework can be separated into three layers: Model, View, ViewModel. 

6. In DJANGO, the GET method is used to compose a URL which is done by using the submitted data to form a string. On the other hand, the POST method allows clients to send out data and afterwards the browser bundles up the data and processes it.

7. In terms of data delivery, XML, JSON, and HTML all have different uses. XML (Extensible Markup Language) is mainly used in structuring and describing data in a format that allows both humans and machines to read them. JSON (JavaScript Object Notation) can be said to be an alternative to XML and is generally used to transmit data between a web application and the server. HTML (HyperText Markup Language) is used to create and organize the structure of the web pages. In short, a way to display the data for others to see.

8. A few reasons as to why JSON is often used in data exchange between modern web application is because its easy to read and write. JSON is human-readable thus giving developers a much easier time to understand the code written, especially for debugging. Apart from that, JSON is also really lightweight and efficient.

9. d

# Assignment 4

## Display the information of the logged-in user, such as their username, and applying cookies, such as last login, on the main application page.
<img width="1280" alt="image" src="https://github.com/PascalPahlevi/PBP_Assignment2/assets/143638456/d59563d6-1afa-4748-81c1-b488d082622e">
<img width="1280" alt="image" src="https://github.com/PascalPahlevi/PBP_Assignment2/assets/143638456/11e1f878-2706-4d11-8d78-0d638f1ff1ca">

## What is UserCreationForm in Django? Explain its advantages and disadvantages.
  In Django, UserCreationForm is built-in form that can be used through the Django framework to enable the handling of user registration and creation. Among others, a few of its advantages are convenience and security. Since the form is directly built-in through the Django framework, creating a user registration is as simple as a few lines of code. Apart from that, the UserCreationForm also has built-in validation fields for username and password, also making checks on whether the username and password are appropriate. However, one of its disadvantages also come from the fact that it may be too simple for more complex requirements.

##  What is the difference between authentication and authorization in Django application? Why are both important
   Authentication refers to the process of verifying the identity of the user whereas Authorization is the process whether said user has the necessary privileges to access certain resources. Both authentication and authorization are important in their own ways. For example, in the case of security, authenticatiojn is used to ensure that authorized users can access certain parts of the website. On the other hand, authorization is also important for security because it ensures that users are only given access to parts of the website that they are given permission to access. When both authentication and authorization are both combined, it would then increase the overall security.

## What are cookies in website? How does Django use cookies to manage user session data?
   Cookies are essentially pieces of data that are sent to a user's browser to be stored on their device by a website. Typically they are used in order to maintain information how the user has been interacting with the website. On Django, the way cookies work is that a request is initially sent to the server by the browser, then the servers conveys the response to the browser, afterwards the cookie that the browser initially received from the server is saved. With this, the browser will always send that cookie to the server upon receiving a request up until the cookie expires. Finally, when the cookie does expire, it will ultimately be removed from the browser.

## Are cookies secure to use? Is there potential risk to be aware of? 
   Since cookies are essential to web development, with the proper implementation and management they are most definitely secure, however, there are still some potential risks to look out for when it comes to cookies. Among those, a concerning issue when it comes to cookies would be the the risk of data exposure, Since in the first place, cookies may potentially store sensitive user information, if a browser's cookies are not managed properly it could potentially lead to the exposure of the user's data thus also violating their privacy.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).

__Implement registration, login, and logout functions to allow users to access the previous application.__<br>

To begin with, I started by making changes to the `views.py` file which were to make the necessary imports that being `redirect`, `UserCreationForm`, and `messages`. Once I finished with this, I then created a new function called `register` which can be seen below:

```py
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

Once implementing the wesbite's registration, I went ahead and continued in creating a login function and to do this I went back and added more imports to `views.py` which were `authenticate` and `login`. Then, I created a new function called `login_user` which can be seen below:

```py
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

To finish it all off, I then imported `logout` into `views.py` to start adding the logout function to the website. I created another function called `logout_user` as shown below:

```py
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

__Create two user accounts with three dummy data entries for each account using the model previously created in the application.__ <br>

Doing this was quite simple, I simply connected to the local host after running `python manage.py runserver` then registered two new accounts into the website. After doing so, I added three different products on each account.

__Connect Item model with User__ <br>

To connect the item model with user, I first went to `models.py` and imported `User`. Once I did, I went to the `create_product` function and made changes to the existing code as shown below:

```py
def create_product(request):
form = ProductForm(request.POST or None)

if form.is_valid() and request.method == "POST":
    product = form.save(commit=False)
    product.user = request.user
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))
```

# Assignment 5

## Explain the purpose of some CSS element selector and when to use it.

The CSS element selector is typically used to allow us to manually select the HTML elements within our web pages which makes it much easier to design and style them. Some ways in which it can be used is for example to change the websites background color, background images or in some more complex cases add buttons, navigation bars, etc.

## Explain some of the HTML5 tags that you know.

Among the many HTML5 tags that exist, the ones I am most familiar with are <h1> to <h6> tags, the <table> tag, and the <title> tag. To begin with, the <h1> to <h6> tag can be used to define HTML headings. These tags allow us to change the size of the text, whether we want it larger or smaller. For the <table> tag, it can be used to define and create tables within the website. This can be useful in listing data sets or if we want a way in presenting data cleanly within the website. Finally, we have the <title> tag which, to put simply, defines the title of the document.

## What are the differences between margin and padding?

Padding can be referred to as the amount of space an element has inside whereas a margin is the space surrounding the element.

## What are the differences between the CSS framework Tailwind and Bootstrap? When should we use Bootstrap rather than Tailwind, and vice versa?

Both Tailwind and Bootstrap are popoular CSS frameworks however they offer different approaches in creating attractive and responsive websites. To begin with, Tailwind offers a utility-first approach meaning that the styes are directly implemented into the HTML. On the other hand, Bootstrap works with a component-based approach that comes with pre-styled components like buttons and navigation bars that can be directly customized. Apart from that, Tailwind allows for more customization and flexibility which allows us to style our websites with unique designs freely without the need for custom CSS whereas Bootstrap has a more straightforward customization in which users simply need to pick the styles they want and then further customize them if they wish to do so.

When it comes to which one to use, it is more towards the developer's preference and choosing the more suitable framework depending on the needs and requirements of the websites design.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).

__Customize login, register, and add item page as creative as possible.__ <br>

For my assignment, I decided to use Bootstrap mainly because of its simplicity. I first decided to make changes to the login page and my idea for this page was to center the login form itself, while also adding buttons and a placeholder stock image just to make things cleaner. The code for this can be seen below:

```py
<div class = "login text-center">
    <form method="POST" action="" style="max-width: 350px;margin: auto;">
        {% csrf_token %}
        <img class ="mt-5 mb-3" src="https://cdn.pixabay.com/photo/2019/06/10/15/11/basketball-4264543_1280.png" height="75">
        <h1>Login</h1>
        <label for="username"class="visually-hidden">Username</label>
        <input type="text" name="username" placeholder="Username" class="form-control mt-3 mb-3">
        <label for="password" class="visually-hidden">Password</label>
        <input type="password" name="password" placeholder="Password" class="form-control">
        <div class="mt-3 mb-3">
            <button class="btn login_btn btn-block btn-dark" type="submit" value="login">Login</button>
        </div>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>
```

Once done with the login page, I worked on the register page. For this page, I decided to not complicate things too much and simply implemented a card design and changing the background colour to grey. The code for this is shown below:

```py
<div class = "text-center">
        <form method="POST" style="max-width: 350px; margin: auto;" >  
            <h1 class="mt-5 mb-3">Create Account</h1>  
            {% csrf_token %}  
            <table class="card" style="padding: 15px; background: darkgrey;">  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input class= "mt-3" type="submit" name="submit" value="Register"/></td>                  </tr>  
            </table>  

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

{% endblock content %}
```

Finally, I went on to customize the add item page. For this page, I basically implemented the same idea as I did with the register page as shown in the code below:

```py
<form method="POST" class="card" style="width: 500px; padding: 20px; margin: auto;">
    {% csrf_token %}
    <table style="margin: auto; padding: 20px;">
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input class="mt-2" type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>
```

__Customize the inventory list page so it becomes more attractive, either by adding colors or using another approach (such as Cards) to show the items, or both.__ <br>

When it came to customizing the inventory list page, there was quite a few things that I did to make the page look much cleaner than it initially was. First off, I decided to add a navbar which showed the username, the page name, and some other miscellaneous features such as contacts. In addition to that, I also wanted to continue with the card design and managed to do so for each item in the inventory list, making sure that it was also responsive and worked when adding more items, editing items, and deleting items. The code for this can be seen below:

```py
    {% for item in items %}

    <div class="card mb-3 mt-5 border border-dark" style="max-width: 1000px; margin: auto;">
        <div class="row g-0">
          <div class="col-md-4">
            <img src="https://cdn.pixabay.com/photo/2020/02/10/11/09/smiley-4836178_1280.png" class="img-fluid rounded-start">
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">{{item.name}}</h5>
              <p class="card-text">Price: {{item.price}}</p>
              <p class="card-text">Description {{item.description}}</p>
              <a href="{% url 'main:edit_product' id=item.pk %}">
                <button class="rounded-pill mt-3">
                  Edit
                </button>
              </a>
              <a href="{% url 'main:delete_product' id=item.pk %}">
                <button class="rounded-pill mt-3">
                  Delete
                </button>
              </a>
              <p class="card-text mt-5"><small class="text-muted">Item added on {{item.date_added}}</small></p>
            </div>
          </div>
        </div>
      </div>
    {% endfor %}

    <h5>Last login session: {{ last_login }}</h5>

{% endblock content %}
```






