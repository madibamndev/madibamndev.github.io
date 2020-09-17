# Sheng Jargon 

![Sheng Jargon Logo](static/images/logo/sheng-jargon-img-logo.svg)

This is a digital *Sheng Jargon*. An app that is aimed at helping you understand words and expressions that are commonly used by sheng speakers.

The site can be navigated using the following navigation links:
```
 Quick Search
 Advanced Search
 Jargon
 Browse by alphabet
 Categories
 Contact 
```

## UX

As a user I want to my *Sheng Jargon* to be easy to navigate, clearly labelled and intuitive so as to be able to have a pleasant experience while navigating the site.

This is the [Sheng Jargon Site PDF Mockup](static/images/screenshots/sheng-jargon-screenshot-site-layout.pdf) of how the site looks. 


## Features

### The Colour palettes and Font Families for this site are as shown below:

```
h1, h2, h3, h4, h5, h6 {
    font-family: 'Jost', sans-serif;
    color: #311b92;
}

a {
    font-family: 'Jost', sans-serif;
}

p {
    font-family: 'Josefin Sans', sans-serif;
    color: #311b92;
}

i {
    color: #fff59d;
}

body {
    background-color: #fff59d;
    font-family: 'Josefin Sans', sans-serif;
}

```

### Google Fonts

[Google Fonts](https://fonts.google.com/?query=jost&sidebar.open=true&selection.family=Josefin+Sans|Jost:wght@500)

```
Fonts Families:
    - Josefin Sans
    - Jost
```

#### General Page Layout

Below is the General Page Layout:

```
 <!DOCTYPE html>
<html lang="en">

<head>
    <!-- Title content -->
    <title>Sheng Jargon - {% block title %}{% endblock title %}</title>
    <!-- Import Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&family=Jost:wght@300;500&display=swap" rel="stylesheet">
    <!--Import Google Icon Font -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!-- Bootstrapcdn Fontawesome CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" type="text/css">
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" media="screen,projection">
    <!-- Meta links -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- style.css -->
    <link rel="stylesheet" href="{{url_for('static', filename='css/style.css')}}" type="text/css">
</head>

<body>
    <!-- Nav content starts here -->
    {% block nav %}
        <nav class="deep-purple darken-4">
            <div class="container">
                <div class="nav-wrapper">
                    <a href="{{url_for('quick_jargon_search')}}" class="brand-logo">SJ</a>
                    <a href="#" data-target="mobile-nav" class="sidenav-trigger">
                        <i class="large material-icons right" style="color: #fff59d;">menu</i>
                    </a>
                    <ul class="right hide-on-med-and-down">
                        <li><a href="{{url_for('quick_jargon_search')}}">Quick Search</a></li>
                        <li><a href="{{url_for('advanced_jargon_search')}}" target="_blank">Advanced Search</a></li>
                        <li><a href="{{url_for('browse_jargon')}}">Jargon</a></li>
                        <li><a href="{{url_for('browse_jargon_by_alphabet')}}" target="_blank">Browse by alphabet</a></li>
                        <li><a href="{{url_for('categories')}}" target="_blank">Categories</a></li>
                        <li><a href="{{url_for('contact')}}">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <!-- Mobile version Navigation -->
        <ul class="sidenav deep-purple darken-4" id="mobile-nav">
            <li>
                <div class="background">
                    <img src="{{url_for('static', filename='images/logo/sheng-jargon-img-logo.svg')}}"
                        alt="Sheng Jargon Pill shaped logo">
                </div>
            </li>
            <hr class="yellow lighten-3">
            <li><a href="{{url_for('quick_jargon_search')}}"><i class="material-icons"
                        style="color: #fff59d;">search</i>Quick Word Search</a></li>
            <li><a href="{{url_for('advanced_jargon_search')}}"><i class="material-icons"
                        style="color: #fff59d;">search</i>Advanced Word Search</a></li>
            <li><a href="{{url_for('browse_jargon')}}"><i class="material-icons"
                        style="color: #fff59d;">book</i>Jargon</a></li>
            <li><a href="{{url_for('browse_jargon_by_alphabet')}}"><i class="material-icons"
                        style="color: #fff59d;">book</i>Browse by alphabet</a></li>
            <li><a href="{{url_for('categories')}}"><i class="material-icons"
                        style="color: #fff59d;">format_list_bulleted</i>Categories</a></li>
            <li><a href="{{url_for('contact')}}"><i class="material-icons"
                        style="color: #fff59d;">message</i>Contact</a></li>
        </ul>
    {% endblock nav %}
    <!-- Nav content ends here -->
    <!-- Base Layout page container content starts here -->
    <div class="container yellow lighten-3">
        <!-- Block Content starts here -->
        {% block content %}
            <!-- Header content starts here -->
            <header>
                <div class="row">
                    <div class="col s12">
                        {% block header %}{% endblock header %}
                    </div>
                </div>
            </header>
            <!-- Header content ends here -->
            <!-- Main content starts here -->
            <main>
                {% block main %}{% endblock main %}
            </main>
            <!-- Main content ends here -->
        {% endblock %}
        <!-- Block content ends here -->
        <!-- Footer content starts here -->
        <footer>
            <div class="row">
                <div class="col s12">
                    <p class="flow-text center-align">
                        <!-- copyright content starts here -->
                        <small>© Copyright 2020. All rights Reserved<br>Sheng Jargon</small>
                        <!-- copyright content ends here -->
                    </p>
                </div>
            </div>
        </footer>
    <!-- Footer content ends here -->
    </div>
    <!-- Base Layout page container content ends here -->
    <!-- Compiled and minified JavaScript at end of body for optimized loading -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <!-- Main.js -->
    <script type="text/javascript" src="{{url_for('static', filename='js/main.js')}}"></script>
</body>
</html>
```

### Existing Features


#### Home Page

Feature 1 (Quick Word Search) &mdash; *allows the user to enter a simple quick word search.*

```
 <form action="#" method="#">
    <fieldset>
        <legend>Quick Word Search Form</legend>
        <div class="row">
            <div class="input-field col s12">
                <input id="quick-word-search" type="text" class="validate">
                <label for="quick-word-search">Quick Word Search</label>
                <span class="helper-text" data-error="wrong" data-success="right">One Word or an expression</span>
            </div>
        </div>
        <a class="waves-effect waves-light btn deep-purple darken-4">Search</a>
    </fieldset>
</form> 
```

Feature 2 (Advanced Word Search) &mdash; *allows the user to add more options in their word search.*

```
<form action="#" method="#">
    <fieldset>
        <legend>Advanced Word Search Form</legend>
        <div class="row">
            <div class="input-field col s12 m6 l4 xl3">
                <select>
                    <option value="" disabled selected>Choose your option</option>
                    <option value="adjective">Adjective</option>
                    <option value="adverb">Adverb</option>
                    <option value="conjunction">Conjunction</option>
                    <option value="determiner">Determiner</option>
                    <option value="interjection">Interjection</option>
                    <option value="noun">Noun</option>
                    <option value="Preposition">Preposition</option>
                    <option value="pronoun">Pronoun</option>
                    <option value="verb">Verb</option>
                </select>
                <label>Part Of Speech</label>
            </div>
            <div class="input-field col s12 m6 l4 xl3 offset-xl1">
                <select>
                    <option value="" disabled selected>Choose your option</option>
                    <option value="meaning">Meaning</option>
                    <option value="definition">Definition</option>
                </select>
                <label>Meaning or Definition</label>
            </div>
            <div class="input-field col s12 m6 l4 xl3 offset-xl1">
                <select>
                    <option value="" disabled selected>Choose your option</option>
                    <option value="synonym">Synonym</option>
                    <option value="opposite">Opposite</option>
                </select>
                <label>Synonym or Antonym</label>
            </div>
        </div>
        <div class="row">
            <div class="input-field col s12">
                <input id="advanced-word-search" type="text" class="validate">
                <label for="advanced-word-search">Advanced Word Search</label>
                <span class="helper-text" data-error="wrong" data-success="right">One Word or an expression</span>
            </div>
        </div>
        <a class="waves-effect waves-light btn deep-purple darken-4">Search<a>
    </fieldset>
</form>
```

#### Jargon Page

Feature 3 (browse Jargon) &mdash; *allows the user to view the jargon as well as add, edit and delete.*
```
 Category Name
 Word
 Definition
 Meaning
 Synonyms
 Opposites
 Part Of Speech
 Alphabet
 Date Added
```

Feature 4 (Browse Jargon by Alphabet) &mdash; *allows the user to browse through the words and expressions by selecting an alphabet.*
```
 Browse by Alphabet

     Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz
```

#### Categories Page

Feature 5 (Categories) &mdash; *allows the user to manage the categories.*

```
<form action="{{ url_for('update_category', category_id=category._id) }}" method="POST">
    <fieldset>
        <legend>Edit Category form</legend>
        <div class="row">
            <div class="input-field col s12">
                <i class="material-icons prefix" style="color: #311b92;">format_list_bulleted</i>
                <input id="category_name" name="category_name" type="text" class="validate" value="{{category.category_name}}">
                <label for="category_name">Category Name</label>
            </div>
        </div>
        <div class="row">
            <button class="btn waves-effect waves-light deep-purple darken-4" style="color: #fff59d;" type="submit" name="action">Update Category
                <i class="material-icons right" style="color: #fff59d;">playlist_add</i>
            </button>
            <a href="{{url_for('delete_category', category_id=category._id)}}" class="waves-effect waves-light btn deep-purple darken-4" style="color: #fff59d;">
                <i class="material-icons right" style="color: #fff59d;">delete</i>Delete
            </a>
            <a href="{{ url_for('categories') }}" class="waves-effect waves-light btn deep-purple darken-4" style="color: #fff59d;">
                <i class="material-icons right" style="color: #fff59d;">cancel</i>Cancel
            </a>
        </div>
    </fieldset>
</form>
```

#### Contact Page

Feature 6 (Contact Form) &mdash; *allows the user to send feedback and/or a message to the App meaintenance team.*

```
<form action="#" method="#">
    <fieldset>
        <legend>Contact Information</legend>
        <div class="row">
            <div class="input-field col s6">
                <input id="first_name" type="text" class="validate">
                <label for="first_name">First Name</label>
            </div>
            <div class="input-field col s6">
                <input id="last_name" type="text" class="validate">
                <label for="last_name">Last Name</label>
            </div>
            <br>
        </div>
        <div class="row">
            <div class="input-field col s12">
                <input id="email" type="email" class="validate">
                <label for="email">Email</label>
                <span class="helper-text" data-error="wrong" data-success="right"> We'll never share your email with anyone else.</span>
            </div>
        </div>
        <br>
        <div class="row">
            <div class="input-field col s12">
                <textarea id="input-your-message" class="materialize-textarea" data-length="120"></textarea>
                <label for="textarea2">Message</label>
            </div>
        </div>
        <button class="btn waves-effect waves-light deep-purple darken-4" style="color: #fff59d;" type="submit" name="action">Submit
            <i class="large material-icons right" style="color: #fff59d;">playlist_add</i>
        </button>
    </fieldset>
</form>
```

### Features Left to Implement

```
 Quick Word Search Form
 Advanced Word Search Form
 Analytics
 New Words
 Contact Form
```

## Technologies Used in this Build

- [Materialize](https://materializecss.com/getting-started.html) &mdash; The Front-End web Framework used

- [Google Fonts](https://fonts.google.com/?query=jost&sidebar.open=true&selection.family=Josefin+Sans|Jost:wght@500) &mdash; The Font Families used

- [Heroku](https://www.heroku.com/) &mdash; Application Deployment

- [Python](https://www.python.org/downloads/) &mdash; Programming Language

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) &mdash; Microframework written in Python

- [Stack Overflow](https://stackoverflow.com/) &mdash; Troubleshooting

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) &mdash; Back-End NoSQL Database

- [Visual Studio Code](https://code.visualstudio.com/) &mdash; Editor used

## Testing

- [Testing Flask Applications](https://flask.palletsprojects.com/en/1.1.x/testing/#:~:text=Flask%20provides%20a%20way%20to,with%20your%20favourite%20testing%20solution.) &mdash; Used for testing

- [CSS Validator](http://www.css-validator.org/) &mdash; Validating CSS files

- Automated browser Testing [Google Lighthouse ext](https://developers.google.com/web/tools/lighthouse#devtools) 

- Testing was also conducted manually whereby friends and family browsed clicked the link sent and navigated through the site on various devices and gave their feedback in the process of making this site. 

- [Materialize Media Queries](https://materializecss.com/grid.html) allows me to stack the content into a single column on smaller devices such as smartphones; single and double columns on tablets and single, double or more columns on larger devices.

Below is a *Traceback* sample of a bug that I encountered while running my **app.py** file in the *developement sever*. I managed to solve it by editing the ```@app.route``` content.

```
 Traceback (most recent call last):
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\app.py", line 2464, in __call__
    return self.wsgi_app(environ, start_response)
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\app.py", line 2450, in wsgi_app
    response = self.handle_exception(e)
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\app.py", line 1867, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\app.py", line 2447, in wsgi_app
    response = self.full_dispatch_request()
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\app.py", line 1952, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\app.py", line 1821, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\_compat.py", line 39, in reraise
    raise value
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\app.py", line 1950, in full_dispatch_request
    rv = self.dispatch_request()
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\app.py", line 1936, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\app.py", line 37, in browse_jargon
    return render_template("jargon.html",
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\templating.py", line 137, in render_template
    return _render(
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\flask\templating.py", line 120, in _render
    rv = template.render(context)
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\jinja2\environment.py", line 1090, in render
    self.environment.handle_exception()
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\jinja2\environment.py", line 832, in handle_exception
    reraise(*rewrite_traceback_stack(source=source))
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\jinja2\_compat.py", line 28, in reraise
    raise value.with_traceback(tb)
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\templates\jargon.html", line 3, in top-level template code
    {% extends 'base.html' %}
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\templates\base.html", line 70, in top-level template code
    {% block content %}
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\templates\jargon.html", line 15, in block "content"
    {% block main %}
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\templates\jargon.html", line 85, in block "main"
    <a href="{{url_for('edit_jargon', jargon_id=jargon._id)}}"
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\jinja2\environment.py", line 475, in getattr
    return obj[attribute]
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\pymongo\cursor.py", line 612, in __getitem__
    self.__check_okay_to_chain()
  File "C:\Users\madib\OneDrive\Desktop\sheng-jargon-application\venv\Lib\site-packages\pymongo\cursor.py", line 401, in __check_okay_to_chain
    raise InvalidOperation("cannot set options after executing query")
pymongo.errors.InvalidOperation: cannot set options after executing query 
```

## Deployment

In order to deploy the application to heroku [Heroku](https://www.heroku.com/) read the following guidelines on how to [Deploy Python Flask App on Heroku](https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/).

In order to deploy your site to [GitHub](https://github.com/) read the following guidelines on [Getting Started with GitHub Pages](https://guides.github.com/features/pages/). 

## Credits

### Content


- Below are examples of *Flask Applications* used as inspiration for my project 
* [Flask Mongo Task Manager](https://github.com/Code-Institute-Solutions/flask-mongo-task-manager) 
* [Flask Blog](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog)
* [Flask Tutorial](https://github.com/pallets/flask/tree/1.1.2/examples/tutorial)


### Media

The image placeholder slides used in this project are in the SVG format and were drawn by myself using adobe Xd. Equally the logo is also in SVG format and was designed by myself using Adobe Illustrator. 

### Acknowledgements

My biggest inspiration with this project is to create a platform that the user can be able to look up the meanings and definitions of certain words and expressions used by sheng speakers. 