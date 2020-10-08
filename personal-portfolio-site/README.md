# Personal PortFolio 

![Portfolio Logo](images/screenshots/img-logo-1x.svg)

This is a digital *Personal PortFolio*. A platform where one can showcase the following: education history, work experience, skills, relevant competencies, hobbies & interests, personal and contact information. This site is open for viewing and collaboration from the general public as well as potential employment possibilities from recruiters.

The site can be navigated using the following pages:
```
 Home
 About 
 Education
 Work 
 PortFolio 
 Contact
 Downloads
```

```
<nav class="navbar navbar-expand-lg custom-navbar nav-fill rounded shadow-lg custom-navbar-bg">

    <button class="navbar-toggler custom-toggler" type="button" data-toggle="collapse"
        data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
        aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <a class="nav-link" target="_blank" href="index.html">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" target="_blank" href="about.html">About</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" target="_blank" href="education.html">Education</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" target="_blank" href="work.html">Work</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" target="_blank" href="portfolio.html">Portfolio</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" target="_blank" href="contact.html">Contact</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" target="_blank" href="downloads.html">Downloads</a>
            </li>
        </ul>
    </div>
</nav>
```

In addition, the page called *PortFolio* has a heading labelled **Projects Gallery** solely dedicated to screenshots of complete projects with a link icon below the image which directs the viewer to that particular site. Here the user can showcase their abilities and capabilities with regards to their respective line of work.

## UX

 As a user I want to my PortFolio to be easy to navigate and understand so that the user is able to have a pleasant experience while navigating the site.

 This site is a design template for a user interested in creating their own *Digital Personal PortFolio*. It has been split into 7 pages namely: *Home, About, Education, Work, PortFolio, Contact* and *Downloads*.

 In order to achieve this I began by drawing up a sketch of how the site would look like as shown in this link [Site PDF Mockup](images/screenshots/personal-portfolio-site-layouts.pdf)

## Features

### Colour palettes for this site are:

```
Background-color Hex code: #FFDEAD (Navajowhite)
Text color Hex code: #2d2620
```

### Google Fonts

[Google Fonts](https://fonts.google.com/specimen/Old+Standard+TT?sidebar.open=true&selection.family=Josefin+Sans|Jost|Old+Standard+TT&query=old+st)

```
Fonts:
    - Josefin Sans
    - Jost
    - Old Standard TT
```

```
@import url('https://fonts.googleapis.com/css2?family=Josefin+Sans&family=Jost&family=Old+Standard+TT&display=swap');

/* Heading styles */
    
h1, h2, h3, h4, h5, h6 {
    font-family: 'Josefin Sans', sans-serif;
}


/* Paragraphs and anchor styles */

p {
    font-family: 'Jost', sans-serif;
}

a {
    font-family: 'Josefin Sans', sans-serif;
    text-decoration: none;
}
```

#### General Page Layout

Each page is divided into four parts:
```
 header
     Logo
     Personal PortFolio

 nav
     Home
     About
     Education
     Work
     PortFolio
     Contact
     Downloads

 main
     content

 footer
     Social and professional links
     copyright
```
```
 <!DOCTYPE html>
<html lang="en">

<head>
    <title>PortFolio - Home</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans&family=Jost&family=Old+Standard+TT&display=swap" rel="stylesheet">
    <!-- Font Awesome icons -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- W3 CSS -->
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <!-- CSS only -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <!-- styles.css -->
    <link rel="stylesheet" href="./css/styles.css" type="text/css">
</head>

<body>
    <!-- Cover Page content starts here -->
        <div class="container-fluid">
            <br>
            <!-- Header content starts here -->
            <header class="shadow-lg">
                <div class="row">
                    <div class="col">
                        <a href="index.html" target="_blank">
                            <img class="brand-logo figure-img img-fluid float-left px-2 "
                                src="./images/logo/img-logo-1x.svg" alt="Circular portfolio logo">
                        </a>
                        <h1 style="font-weight: 600;">Personal PortFolio</h1>
                    </div>
                </div>
            </header>
            <!-- header content ends here -->
            <br>
            <!-- Nav content starts here -->
            <div class="row">
                <div class="col">
                    <nav class="navbar navbar-expand-lg custom-navbar nav-fill rounded shadow-lg custom-navbar-bg">

                        <button class="navbar-toggler custom-toggler" type="button" data-toggle="collapse"
                            data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                            aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>

                        <div class="collapse navbar-collapse" id="navbarSupportedContent">
                            <ul class="navbar-nav mr-auto">
                                <li class="nav-item">
                                    <a class="nav-link" target="_blank" href="index.html">Home</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" target="_blank" href="about.html">About</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" target="_blank" href="education.html">Education</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" target="_blank" href="work.html">Work</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" target="_blank" href="portfolio.html">Portfolio</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" target="_blank" href="contact.html">Contact</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" target="_blank" href="downloads.html">Downloads</a>
                                </li>
                            </ul>
                        </div>
                    </nav>
                </div>
            </div>
            <!-- Nav content ends here -->
            <br>
            <!-- Main content starts here -->
                <main>
                    <div class="row pt-5">
                        <div class="col-12 col-sm-12 col-md-12 col-lg-6 col-xl-6 offset-xl-3">
                            <aside>
                                <div id="carouselExampleCaptions"
                                    class="carousel slide carousel-fade shadow-lg rounded-lg" data-ride="carousel">
                                    <ol class="carousel-indicators">
                                        <li data-target="#carouselExampleCaptions" data-slide-to="0" class="active">
                                        </li>
                                        <li data-target="#carouselExampleCaptions" data-slide-to="1"></li>
                                        <li data-target="#carouselExampleCaptions" data-slide-to="2"></li>
                                        <li data-target="#carouselExampleCaptions" data-slide-to="3"></li>
                                        <li data-target="#carouselExampleCaptions" data-slide-to="4"></li>
                                    </ol>
                                    <div class="carousel-inner">
                                        <div class="carousel-item active">
                                            <img src="./images/homepage-carousel/welcome-carousel-img-1.svg"
                                                class="d-block w-100 rounded-lg shadow-lg" alt="Placeholder Slide 1">
                                            <div class="carousel-caption d-none d-md-block">
                                                <h5>First slide label</h5>
                                                <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                                            </div>
                                        </div>
                                        <div class="carousel-item">
                                            <img src="./images/homepage-carousel/welcome-carousel-img-2.svg"
                                                class="d-block w-100 rounded-lg shadow-lg" alt="Placeholder Slide 2">
                                            <div class="carousel-caption d-none d-md-block">
                                                <h5>Second slide label</h5>
                                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                                            </div>
                                        </div>
                                        <div class="carousel-item">
                                            <img src="./images/homepage-carousel/welcome-carousel-img-3.svg"
                                                class="d-block w-100 rounded-lg shadow-lg" alt="Placeholder Slide 3">
                                            <div class="carousel-caption d-none d-md-block">
                                                <h5>Third slide label</h5>
                                                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                                            </div>
                                        </div>
                                        <div class="carousel-item">
                                            <img src="./images/homepage-carousel/welcome-carousel-img-4.svg"
                                                class="d-block w-100 rounded-lg shadow-lg" alt="Placeholder Slide 4">
                                            <div class="carousel-caption d-none d-md-block">
                                                <h5>Fourth slide label</h5>
                                                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                                            </div>
                                        </div>
                                        <div class="carousel-item">
                                            <img src="./images/homepage-carousel/welcome-carousel-img-5.svg"
                                                class="d-block w-100 rounded-lg shadow-lg" alt="Placeholder Slide 5">
                                            <div class="carousel-caption d-none d-md-block">
                                                <h5>Fifth slide label</h5>
                                                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                                            </div>
                                        </div>
                                    </div>
                                    <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button"
                                        data-slide="prev">
                                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                        <span class="sr-only">Previous</span>
                                    </a>
                                    <a class="carousel-control-next" href="#carouselExampleCaptions" role="button"
                                        data-slide="next">
                                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                        <span class="sr-only">Next</span>
                                    </a>
                                </div>
                            </aside>
                        </div>
                    </div>
                    <br>
                    <div class="row">
                        <div class="col-12 col-sm-12 col-md-12 col-lg-6 col-xl-6 offset-xl-3">
                            <article>
                                <div class="text-center pt-5 pb-5">
                                    <h2>Welcome Note</h2>
                                    <p class="lead">Welcome to my
                                        <em>Digital PortFolio</em>. I'm a creative who is passionate
                                    about content creation and the impact it has on a user.</p>
                                    <br>
                                    <a class="btn btn-primary btn-lg shadow-lg" href="about.html" target="_blank" role="button">Learn more</a>
                                </div>
                            </article>
                        </div> 
                    </div>        
                </main>
            <!-- Main content ends here -->
            <br>
            <!-- Footer content starts here -->
            <footer>
                <div class="row">
                    <div class="col">
                        <div class="card text-center border-0" style="background-color: transparent;">
                            <div class="card-body">
                                <a class="facebook" target="_blank" href="https://www.facebook.com/">
                                    <i class="fa fa-2x fa-facebook" style="color: #3b5999;" aria-hidden="true"></i>
                                </a>
                                <a class="instagram" target="_blank" href="https://www.instagram.com/">
                                    <i class="fa fa-2x fa-instagram" style="color: #5851db;" id="insta"
                                        aria-hidden="true"></i>
                                </a>
                                <a class="youtube" target="_blank" href="https://www.youtube.com/">
                                    <i class="fa fa-2x fa-youtube" style="color: #cd201f;" aria-hidden="true"></i>
                                </a>
                                <a class="twitter" target="_blank" href="https://twitter.com/">
                                    <i class="fa fa-2x fa-twitter" style="color: #55acee;" aria-hidden="true"></i>
                                </a>
                                <a class="pinterest" target="_blank" href="https://www.pinterest.com/">
                                    <i class="fa fa-2x fa-pinterest" style="color: #bd081c;" aria-hidden="true"></i>
                                </a>
                                <a class="snapchat" target="_blank" href="https://www.snapchat.com/">
                                    <i class="fa fa-2x fa-snapchat" style="color: #fffc00;" aria-hidden="true"></i>
                                </a>
                                <a class="linkedin" target="_blank" href="https://www.linkedin.com/">
                                    <i class="fa fa-2x fa-linkedin" style="color: #2867b2;" aria-hidden="true"></i>
                                </a>
                                <a class="meetup" target="_blank" href="https://www.meetup.com/">
                                    <i class="fa fa-2x fa-meetup" style="color: #ed1c40;" aria-hidden="true"></i>
                                </a>
                                <a class="xing" target="_blank" href="https://www.xing.com/">
                                    <i class="fa fa-2x fa-xing" style="color: #026466;" aria-hidden="true"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <div class="card text-center border-0" style="background-color: transparent;">
                            <div class="card-body">
                                <!-- copyright content starts here -->
                                <small>© Copyright 2020<br>
                                    <a class="text-decoration-none" target="_blank" href="someone@example.com">First
                                        Name | Last Name</a>
                                </small>
                                <!-- copyright content ends here -->
                            </div>
                        </div>
                    </div>
                </div>
            </footer>
        <!-- Footer content ends here -->
        <br>
        </div>
    <!-- Cover Page content ends here -->
    <!-- JS, Popper.js, and jQuery -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>
```

### Existing Features

#### Home Page

Feature 1 (Carousel) &mdash; *allows the user to add their own images. In addition captions can also be included alongside the images.*

```
<aside>
    <div id="carouselExampleCaptions"
        class="carousel slide carousel-fade shadow-lg rounded-lg" data-ride="carousel">
        <ol class="carousel-indicators">
            <li data-target="#carouselExampleCaptions" data-slide-to="0" class="active"></li>
            <li data-target="#carouselExampleCaptions" data-slide-to="1"></li>
            <li data-target="#carouselExampleCaptions" data-slide-to="2"></li>
            <li data-target="#carouselExampleCaptions" data-slide-to="3"></li>
            <li data-target="#carouselExampleCaptions" data-slide-to="4"></li>
        </ol>
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="./images/homepage-carousel/welcome-carousel-img-1.svg"
                    class="d-block w-100 rounded-lg shadow-lg" alt="Placeholder Slide 1">
                <div class="carousel-caption d-none d-md-block">
                    <h5>First slide label</h5>
                    <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                </div>
            </div>
            <div class="carousel-item">
                <img src="./images/homepage-carousel/welcome-carousel-img-2.svg"
                    class="d-block w-100 rounded-lg shadow-lg" alt="Placeholder Slide 2">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Second slide label</h5>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </div>
            </div>
            <div class="carousel-item">
                <img src="./images/homepage-carousel/welcome-carousel-img-3.svg"
                    class="d-block w-100 rounded-lg shadow-lg" alt="Placeholder Slide 3">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Third slide label</h5>
                    <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                </div>
            </div>
            <div class="carousel-item">
                <img src="./images/homepage-carousel/welcome-carousel-img-4.svg"
                    class="d-block w-100 rounded-lg shadow-lg" alt="Placeholder Slide 4">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Fourth slide label</h5>
                    <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                </div>
            </div>
            <div class="carousel-item">
                <img src="./images/homepage-carousel/welcome-carousel-img-5.svg"
                    class="d-block w-100 rounded-lg shadow-lg" alt="Placeholder Slide 5">
                <div class="carousel-caption d-none d-md-block">
                    <h5>Fifth slide label</h5>
                    <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                </div>
            </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
</aside>
```

#### About Page

Feature 2 (Personal Info) &mdash; *allows the user to add their own personal info such as:*
``` 
 Date Of Birth:
     Day | Month | Year 
 Address:
     P.O. Box 12345 - Location
 Mobile Number:
     0712 345 678
 Email:
     someone@example.com  
```

```
<section class="text-center p-2">
    <h3>Personal Info</h3>
    <p><strong>Date Of Birth:</strong><br>
        Day | Month | Year</p>
    <p><strong>Address:</strong><br>
        P.O. Box 12345 - Location</p>
    <p><strong>Mobile Number:</strong><br>
        0712 345 678</p>
    <p><strong>Email:</strong><br>
        someone@example.com</p>
</section>
```

Feature 3 (Profile Pic) &mdash; *allows the user to add their own Profile Picture as per the template provided:*
```
     Your Names
     Your Current Position
```

```
<section class="text-center p-2">
    <figure class="figure">
        <img src="./images/profile-pic/img-profile-pic.svg"
            class="figure-img img-fluid rounded p-2" alt="Site owner profile picture">
            <figcaption class="text-center p-2">
                <h2>Your Names</h2>
                <h3><em>Your Current Position</em></h3>
            </figcaption> 
    </figure>
</section>
```

Feature 4 (Professional and Personal Accomplishments) &mdash; *allows the user to add their own Accomplishments as per the template provided.*
```
 Professional and personal accomplishments:
     Professional and personal capacity
     Accomplishment
```

```
<section class="text-center p-2">
    <blockquote>
        <h3>Professional and personal accomplishments</h3>
        <p>Professional and personal capacity</p>
        <footer><cite>Accomplishment</cite></footer>
    </blockquote>
</section>
```

Feature 5 (What are you looking for right now?) &mdash; *allows the user to add what they are looking for:*
```
 What are you looking for right now?
     Job, career change, collaboration, partnership
     Choice
```

```
<section class="text-center p-2">
    <blockquote>
        <h3>What are you looking for right now?</h3>
        <p>Job, career change, collaboration, partnership</p>
        <footer><cite>Choice</cite></footer>
    </blockquote>
</section>
```


Feature 6 (Why you should hire me!) &mdash; *allows the user to pitch for themselves why they should be hired:*
```
 Why you should hire me!
      Tell me about your portfolio
      Credentials
```

```
<section class="text-center p-2">
    <blockquote>
        <h3>Why you should hire me!</h3>
        <p>Tell me about your portfolio</p>
        <footer><cite>Credentials</cite></footer>
    </blockquote>
</section>
```


#### Education Page

Feature 7 (Accordion Collapse University Education History) &mdash; *allows the user to enter their studies details:*
```
 University:
      Month/Year of Start - Month/Year of End
      Course Name
      University Name
      P.O. Box: 123 45
      Location, Country
```

```
<div class="card" style="background: navajowhite;">
    <div class="card-header" id="headingUniOne">
        <h2 class="mb-0">
            <button class="btn btn-link btn-block text-left" type="button"
                data-toggle="collapse" 
                data-target="#collapseUniOne"
                aria-expanded="true"
                aria-controls="collapseUniOne">
                1<sup>st</sup> University
            </button>
        </h2>
    </div>
    <div id="collapseUniOne" class="collapse show"
        aria-labelledby="headingUniOne"
        data-parent="#accordionUni">
        <div class="card-body">
            <p><strong>Month/Year of Start - Month/Year of End</strong></p>
            <p><strong>Course Name</strong></p>
            <p><strong>University Name</strong></p>
            <p><strong>P.O. Box:</strong> 123 45</p>
            <p><strong>Location, Country</strong></p>
        </div>
    </div>
</div>
```


Feature 8 (Accordion Collapse High School Education History) &mdash; *allows the user to enter their studies details:*
```
 High School:
      Month/Year of Start - Month/Year of End
      Course Name
      High School Name
      P.O. Box: 123 45
      Location, Country
```

```
<div class="card" style="background: navajowhite;">
    <div class="card-header" id="headingHsOne">
        <h2 class="mb-0">
            <button class="btn btn-link btn-block text-left" type="button"
                data-toggle="collapse" 
                data-target="#collapseHsOne" aria-expanded="true"
                aria-controls="collapseHsOne">
                1<sup>st</sup> High School
            </button>
        </h2>
    </div>
    <div id="collapseHsOne" class="collapse show" aria-labelledby="headingHsOne"
        data-parent="#accordionHs">
        <div class="card-body">
            <p><strong>Month/Year of Start - Month/Year of End</strong></p>
            <p><strong>Course Name</strong></p>
            <p><strong>High School Name</strong></p>
            <p><strong>P.O. Box:</strong> 123 45</p>
            <p><strong>Location, Country</strong></p>
        </div>
    </div>
</div>
```

Feature 9 (Accordion Collapse Primary School Education History) &mdash; *allows the user to enter their studies details:*
```
 Primary School:
      Month/Year of Start - Month/Year of End
      Course Name
      Primary School Name
      P.O. Box: 123 45
      Location, Country
```

```
<div class="card" style="background: navajowhite;">
    <div class="card-header" id="headingPsOne">
        <h2 class="mb-0">
            <button class="btn btn-link btn-block text-left" type="button"
                data-toggle="collapse" data-target="#collapsePsOne" aria-expanded="true"
                aria-controls="collapsePsOne">
                1<sup>st</sup> Primary School
            </button>
        </h2>
    </div>
    <div id="collapsePsOne" class="collapse show" aria-labelledby="headingPsOne"
        data-parent="#accordionPs">
        <div class="card-body">
            <p><strong>Month/Year of Start - Month/Year of End</strong></p>
            <p><strong>Course Name</strong></p>
            <p><strong>Primary School Name</strong></p>
            <p><strong>P.O. Box:</strong> 123 45</p>
            <p><strong>Location, Country</strong></p>
        </div>
    </div>
</div>
```


#### Work Page

Feature 10 (Timeline for Work Experience) &mdash; *allows the user to enter their work details:*
```
 Job Title:
      Company Name
      Description
      Location, Country
      Year of Start - Year of End
```

```
<li>
    <div class="timeline-content rounded-lg shadow-lg">
        <div class="timeline-content-heading">
            <h3>Job Title</h3>
        </div>
        <div class="timeline-content-subheading font-italic">
            <h4>Company Name</h4>
        </div>
        <div class="timeline-content-body">
            <p class="pb-3">
                <strong>Description:</strong> Lorem ipsum dolor sit amet consectetur
                adipisicing elit.
                Tempore et alias ipsam temporibus, qui laudantium,
                mollitia id quibusdam eum accusamus eius? Iste dolorem nihil eaque,
                voluptatem beatae ducimus! Minus non sapiente blanditiis modi
                consequuntur,
                tempore delectus atque. Ipsam eos quibusdam reiciendis a molestias,
                fuga facilis quos, minus sint, et cum.
            </p>
            <div class="timeline-content-body-subheading font-italic">
                <h5 class="font-italic location m-0 pb-2">Location, Country</h5>
            </div>
        </div>
    </div>
    <div class="timeline-time">
        <h6>2019 &mdash; 2020</h6>
    </div>
</li>
```

#### PortFolio Page

Feature 11 (Projects Gallery) &mdash; *allows the user to add screenshots of their completed projects:*
```
 Project number:
      figure
      img
      figcaption:
         Chain Link icon
 ```

 ```
<section class="text-center p-2">
    <h3>Project 1</h3>
    <figure class="figure">
        <img class="figure-img img-fluid rounded shadow-lg project-1"
            src="./images/projects-gallery/img-project-1.svg" alt="project-1-screenshot">
        <figcaption><em>Link</em>
            <a href="#" target="_blank">
                <i class="fa fa-2x fa-link" aria-hidden="true" style="color: #F40F02;"></i>
            </a>
        </figcaption>
    </figure>
</section>
```


#### Contacts Page

Feature 12 (Contact Details) &mdash; *allows the user to enter their contact details:*
```
 Email:
     someone@example.com

 Mobile Number:
     0712 345 678

 Address:
     P.O. Box 12345 - Location
```

```
<section class="text-center p-2">
    <h3>Email:</h3>
    <p>someone@example.com</p>
    <h4>Mobile Number:</h4>
    <p>0712 345 678</p>
    <h4>Address:</h4>
    <p>P.O. Box 12345 - Location</p>
</section>
```


#### Downloads Page

Feature 13 (Downloads) &mdash; *allows the user to link the following documents:*
```
 Curriculum Vitae
     PDF Icon

 Cover Letter
     PDF Icon

 Recommendation Letter
     PDF Icon

 References
     PDF Icon
```

```
<article>
    <h2 class="text-center" style="font-weight: 600;">Downloads</h2>
    <div class="row">
        <div class="col-12 col-sm-12 col-md-12 col-lg-6 col-xl-3">
            <section class="text-center p-2">
                <h3>Curriculum Vitae</h3><br>
                    <a href="pdf/curriculum-vitae.pdf" target="_blank">
                        <i class="fa fa-4x fa-file-pdf-o" aria-hidden="true" style="color: #F40F02;"></i>
                    </a>
            </section>
        </div>
        <div class="col-12 col-sm-12 col-md-12 col-lg-6 col-xl-3">
            <section class="text-center p-2">
                <h3>Cover Letter</h3><br>
                    <a href="pdf/cover-letter.pdf" target="_blank">
                        <i class="fa fa-4x fa-file-pdf-o" aria-hidden="true" style="color: #F40F02;"></i>
                    </a>
            </section>
        </div>
        <div class="col-12 col-sm-12 col-md-12 col-lg-6 col-xl-3">
            <section class="text-center p-2">
                <h3>Rec Letter</h3><br>
                    <a href="pdf/recommendation-letter.pdf" target="_blank">
                        <i class="fa fa-4x fa-file-pdf-o" aria-hidden="true" style="color: #F40F02;"></i>
                    </a>
            </section>
        </div>
        <div class="col-12 col-sm-12 col-md-12 col-lg-6 col-xl-3">
            <section class="text-center p-2">
                <h3>References</h3><br>
                    <a href="pdf/references.pdf" target="_blank">
                        <i class="fa fa-4x fa-file-pdf-o" aria-hidden="true" style="color: #F40F02;"></i>
                    </a>
            </section>
        </div>
    </div>
</article>
```


### Features Left to Implement

```
 Forms
 Project Request Form
 Progress bar, graphs, diagrams
 Interests
 Hobbies
```

## Technologies Used in this Build

- [Bootstrap](https://getbootstrap.com/) &mdash; The Front-End web Framework used

- [Google Fonts](https://fonts.google.com/specimen/Old+Standard+TT?sidebar.open=true&selection.family=Josefin+Sans|Jost|Old+Standard+TT&query=old+st) &mdash; The Font Families used

- [Stack Overflow](https://stackoverflow.com/) &mdash; Troubleshooting

## Testing

- [html5 Validator](https://validator.nu/) &mdash; validating html5 files

- [W3c Markup validator](https://validator.w3.org/) &mdash; validating html files

- [CSS Validator](http://www.css-validator.org/) &mdash; validating CSS files

- The [Bootstrap](https://getbootstrap.com/) Framework has built in media queries which can be used to style the site so as to fit the devices that it is being viewed on.

- Automated Testing for mobile version using [Google Lighthouse ext](https://developers.google.com/web/tools/lighthouse#devtools) 
    - [Google Lighthouse Testing Results for the entire site](images/screenshots/google-lighthouse-automated-testing.pdf)

- Testing was also conducted manually whereby friends and family browsed clicked the link sent and navigated through the site on various devices and gave their feedback in the process of making this site. 

- [Bootstrap Media Queries](https://getbootstrap.com/docs/4.5/layout/overview/) allows me to stack the content into a single column on smaller devices such as smartphones; single and double columns on tablets and single, double or more columns on larger devices.

One bug that I have encountered in my testing  is in my timeline html file. [(X)HTML5 validation results for work.html bug](images/screenshots/bug-work-html-validation.pdf)

## Deployment

In order to deploy your site to [GitHub](https://github.com/) read the following guidelines on [Getting Started with GitHub Pages](https://guides.github.com/features/pages/). 

## Credits

### Content


- CSS Animations used were inspired by documentation from the [w3schools](https://www.w3schools.com/css/css3_animations.asp)

- Accordion Collapse to display the education history was copied from the [Bootstrap](https://getbootstrap.com/docs/4.5/components/collapse/)

- The timeline used to display *Work Experiences* was copied from the 
* [Seniman Koding Vertical Timeline HTML, CSS Bootstrap Responsive Part 1](https://www.youtube.com/watch?v=BlEoFexQBBk) 
* [Seniman Koding Vertical Timeline HTML, CSS Bootstrap Responsive Part 2](https://www.youtube.com/watch?v=2lczRB7givc)
* [Online Tutorials Responsive Vertical Timeline With Html5 and CSS3 - Responsive Design Using CSS Media Queries](https://www.youtube.com/watch?v=7XWL8ew-9Z4)


### Media

The image placeholder slides used in this project are in the SVG format and were drawn by myself using adobe Xd. Equally the logo is also in SVG format and was designed by myself using Adobe Illustrator. 

### Acknowledgements

My biggest inspiration with this project is to create a platform that the user can be able to showcase their talents and expertise in a fun, digitally creative and expressive manner which can attract like minded individuals to collaborate on projects that solve everyday challenges.
