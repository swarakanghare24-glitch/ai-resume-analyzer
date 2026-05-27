from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import pdfplumber

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

skills_db = [
    "Python",
    "Java",
    "Machine Learning",
    "SQL",
    "Django",
    "Node.js",
    "MongoDB",
    "FastAPI",
    "React",
    "HTML",
    "CSS",
    "JavaScript",
    "Git",
    "GitHub",
    "Prompt Engineering",
    "Generative AI",
    "TensorFlow",
    "Pandas",
    "Spring Boot"
]

job_roles = {

    "AI/ML Engineer": [
        "Python",
        "Machine Learning",
        "TensorFlow",
        "Pandas",
        "SQL"
    ],

    "Backend Developer": [
        "Java",
        "Spring Boot",
        "SQL",
        "Git"
    ],

    "Full Stack Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "MongoDB"
    ]
}

@app.get("/")
def home():
    return {"message": "Resume Analyzer Backend Running"}

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    text = ""

    with pdfplumber.open(file.file) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    ats_score = len(found_skills) * 5

    if ats_score > 100:
        ats_score = 100

    predicted_role = ""

    max_match = 0

    missing_skills = []

    for role, required_skills in job_roles.items():

        matched = 0

        current_missing = []

        for skill in required_skills:

            if skill in found_skills:
                matched += 1
            else:
                current_missing.append(skill)

        if matched > max_match:

            max_match = matched
            predicted_role = role
            missing_skills = current_missing

    return {

        "predicted_role": predicted_role,

        "ats_score": ats_score,

        "skills_found": found_skills,

        "missing_skills": missing_skills
    }