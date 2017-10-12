# Radiation Therapy Decision Support

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

## Introduction

* A main challenge in radiation therapy is that there are healthy organs near the tumor.
**Main Goal**:
``` 
Target the tumor with as much radiation as possible while limiting the dose to healthy organs as risk (OARs).
```
* Current radiation treatment plans and dose contraints are based off of universal guidelines and the clinician's experience.
* Data-driven decision support can help provide dose treatment recommendations based off quantified and evidence-based sources.

## Project Tools

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

MATLAB
```
https://www.mathworks.com/products/matlab.html
```

## Database

Dataset:
* UCLA (University of California Los Angeles) Dataset: 137 anonymized cases.
* TUM (Technical University at Munich) Dataset: 50 anonymized cases.
```
Note: DICOM images are anonymized first and then parsed into the database with the metadata
```
MySQL database stores:
* DICOM images
* Metadata
* Extracted Features

## Feature Extraction

Features to identify the Planning Target Volume (PTV)-Organ At Risk (OAR) spatial relationships calculated in MATLAB:
1. Overlap Volume Histogram (OVH)
2. Spatial Target Signature
   * 3D location of PTV with respect to OAR
   * Spherical coordinates of PTV centroid to OAR centroid

## Decision Support Interface

* Written in HTML and Javascript
* Django Web Framework 1.11 with Python 3.4
* Allows the user to access features solely on our web project that would otherwise require the use of softwares such as MATLAB.

## Discussion and Plans

* Potential to improve the radiation treatment planning workflow
* Integrate data from additional institutions to our knowledge base.
* Streamline web-based GUI for clinicians to use.
TO-DO:
* Integrate the MATLAB code into Python
* Direct integration of feature extraction and matching with web interface
* Obtain outcomes of retrospective cases

## References

1. Kazhdan M., Simari P., McNutt T., Wu B., et al., A Shape Relationship Descriptor for Radiation Therapy Planning, MICCAI 2009; 5762:100-108
2. Deshpande R., Zhou, A., Zhang, J., et al., Role of an imaging informatics-based DICOM-RT cancer registry in evaluating treatment parameters of IMRT for prostate cancer, Proceedings of SPIE Vol. 8674, 86740O (2013)
3. Deshpande R., DeMarco, J., Liu, B., et al., Design and Evaluation of an Imaging Informatics Decision Support System for Radiation Therapy, SPIE 2015 Medical Imaging

## Team Members

* Slevin Zhang (Si Liang) - Project Leader
* Alan Cheng
* Veda Murthy
* Natalie Ramsy
* Piyush Maiti
