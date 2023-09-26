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


