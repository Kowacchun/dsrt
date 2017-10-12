## Radiation Therapy Decision Support

Radiation Therapy Decision Support is a web project designed to help radiation therapists (and other specialists) make a radiation plan to maximize radiation dose to tumors and minimize radiation to nearby healthy organs accurately without having to use various trial plans by comparing uploaded files (MRI and contour) to numerous other cases in our database. 

Contents:
  * [Introduction](#introduction)
  * [Project Tools](#project-tools)
  * [Database](#database)
  * [Feature Extraction](#feature-extraction)
  * [Decision Support Interface](#decision-support-interface)
  * [Discussion and Plans](#discussion-and-plans)
  * [References](#references)
  * [Team Members](#team-members)

# Introduction

* A main challenge in radiation therapy is that there are healthy organs near the tumor.
* **Main Goal**:
``` 
Target the tumor with as much radiation as possible while limiting the dose to healthy organs as risk (OARs).
```
* Current radiation treatment plans and dose contraints are based off of universal guidelines and the clinician's experience.
* Data-driven decision support can help provide dose treatment recommendations based off quantified and evidence-based sources.

# Project Tools

Django 1.11 Web Framework
```
https://www.djangoproject.com/download/
```

Apache HTTP Server
```
https://httpd.apache.org/
```

Python 3.4
```
https://www.python.org/download/releases/3.4.0/
```

Bootstrap
```
http://getbootstrap.com/
```

MySQL Database
```
https://dev.mysql.com/downloads/
```

#Database
