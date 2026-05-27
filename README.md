# ai-resume-analyzer
# AI Resume Analyzer

A web-based resume analysis tool designed to help students and job seekers evaluate their resumes, identify key skills, and understand how well their profiles align with industry expectations.

## Overview

The AI Resume Analyzer allows users to upload a PDF resume and receive an instant analysis of their profile. The application extracts resume content, detects relevant technical skills, estimates an ATS (Applicant Tracking System) score, and suggests areas for improvement.

This project was built as a learning project to explore Python backend development, resume parsing, API integration, and frontend-backend communication.

---

## Features

* PDF Resume Upload
* Resume Text Extraction
* Technical Skill Detection
* ATS Score Estimation
* Missing Skill Identification
* Job Role Prediction
* FastAPI Backend
* Interactive Frontend Interface

---

## Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* FastAPI
* Uvicorn

### Libraries

* pdfplumber
* scikit-learn
* pandas
* numpy
* python-multipart

---

## Project Structure

ai-resume-analyzer/

├── frontend/

│   ├── index.html

│   ├── style.css

│   └── script.js

│

├── python-ai/

│   └── main.py

│

└── README.md

---

## How It Works

1. User uploads a PDF resume.
2. The backend extracts text from the document.
3. Resume content is analyzed against a predefined skill database.
4. Skills present in the resume are identified.
5. Missing skills are highlighted.
6. An ATS score is generated.
7. A suitable job role is predicted based on detected skills.

---

## Sample Output

Predicted Role: Full Stack Developer

ATS Score: 65

Skills Found:

* Python
* Java
* Machine Learning
* Django
* Node.js
* MongoDB
* HTML
* CSS
* JavaScript
* Git
* GitHub

Missing Skills:

* React

---

## Learning Outcomes

Through this project, I gained practical experience in:

* REST API Development with FastAPI
* Resume Parsing and Data Processing
* Frontend–Backend Integration
* Git and GitHub Version Control
* Building End-to-End Web Applications
* Working with Python Libraries for Data Analysis

---

## Future Improvements

* Modern UI/UX Design
* Drag-and-Drop Resume Upload
* Resume Improvement Suggestions
* Industry-Specific Analysis
* Advanced ATS Scoring
* Resume Section Evaluation
* AI-Powered Career Recommendations
* Deployment on Cloud Platforms

---

## Author

**Swara Kanghare**

B.Tech Computer Science Engineering (Artificial Intelligence & Machine Learning)

Pimpri Chinchwad University

2024–2028
