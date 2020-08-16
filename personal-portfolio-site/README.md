# Personal PortFolio 

![Portfolio Logo](images-readme.md/img-logo-1x.svg)

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

In addition, the page called *PortFolio* has a heading labelled **Projects Gallery** solely dedicated to screenshots of complete projects with a link icon below the image which directs the viewer to that particular site. Here the user can showcase their abilities and capabilities with regards to their respective line of work.

## UX

 As a user I want to my PortFolio to be easy to navigate and understand so that the user is able to have a pleasant experience while navigating the site.

 This site is a design template for a user interested in creating their own *Digital Personal PortFolio*. It has been split into 7 pages namely: *Home, About, Education, Work, PortFolio, Contact* and *Downloads*.

 In order to achieve this I began by drawing up a sketch of how the site would look like as shown in this link [Site PDF Mockup](images-readme.md/personal-portfolio-site-layouts.pdf)

## Features

### Colour palettes for this site are:

```
Background-color Hex code: #FFDEAD (Navajowhite)
Text color Hex code: ##2d2620
```

### Google Fonts

[Google Fonts](https://fonts.google.com/specimen/Old+Standard+TT?sidebar.open=true&selection.family=Josefin+Sans|Jost|Old+Standard+TT&query=old+st)

```
Fonts:
    - Josefin Sans
    - Jost
    - Old Standard TT
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

### Existing Features

#### Home Page

Feature 1 (Carousel) &mdash; *allows the user to add their own images. In addition captions can also be included alongside the images.*

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

Feature 3 (Profile Pic) &mdash; *allows the user to add their own Profile Picture as per the template provided:*
```
     Your Names
     Your Current Position
```

Feature 4 (Professional and Personal Accomplishments) &mdash; *allows the user to add their own Accomplishments as per the template provided.*
```
 Professional and personal accomplishments:
     Professional and personal capacity
     Accomplishment
```

Feature 5 (What are you looking for right now?) &mdash; *allows the user to add what they are looking for:*
```
 What are you looking for right now?
     Job, career change, collaboration, partnership
     Choice
```

Feature 6 (Why you should hire me!) &mdash; *allows the user to pitch for themselves why they should be hired:*
```
 Why you should hire me!
      Tell me about your portfolio
      Credentials
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

Feature 8 (Accordion Collapse High School Education History) &mdash; *allows the user to enter their studies details:*
```
 High School:
      Month/Year of Start - Month/Year of End
      Course Name
      High School Name
      P.O. Box: 123 45
      Location, Country
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

#### Work Page

Feature 10 (Timeline for Work Experience) &mdash; *allows the user to enter their work details:*
```
 Job Title:
      Company Name
      Description
      Location, Country
      Year of Start - Year of End
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
    - [Google Lighthouse Testing Results for the entire site](images-readme.md/google-lighthouse-automated-testing.pdf)

- Testing was also conducted manually whereby friends and family browsed clicked the link sent and navigated through the site on various devices and gave their feedback in the process of making this site. 

- [Bootstrap Media Queries](https://getbootstrap.com/docs/4.5/layout/overview/) allows me to stack the content into a single column on smaller devices such as smartphones; single and double columns on tablets and single, double or more columns on larger devices.

One bug that I have encountered in my testing  is in my timeline html file. [(X)HTML5 validation results for work.html bug](images-readme.md/bug-work-html-validation.pdf)

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
