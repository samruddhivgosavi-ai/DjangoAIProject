from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import PyPDF2

def home(request):
    return render(request, "home.html")


def roadmaps(request):
    return render(request, "roadmaps.html")


def study_planner(request):
    return render(request, "study_planner.html")


def interview_questions(request):
    return render(request, "interview_questions.html")


def resources(request):
    return render(request, "resources.html")


def predict_career(request):
    return render(request, "predict_career.html")


def start_assessment(request):
    return render(request, "start_assessment.html")


def analyze_resume(request):

    skills = []
    missing_skills = []
    score = 0

    if request.method == "POST":

        uploaded_file = request.FILES.get("resume")

        if uploaded_file:

            pdf_reader = PyPDF2.PdfReader(uploaded_file)

            text = ""

            for page in pdf_reader.pages:

                extracted_text = page.extract_text()

                if extracted_text:
                    text += extracted_text

            resume_text = text.lower()

            if "python" in resume_text:
                skills.append("Python")

            if "sql" in resume_text:
                skills.append("SQL")

            if "django" in resume_text:
                skills.append("Django")

            if "machine learning" in resume_text:
                skills.append("Machine Learning")

            if "power bi" in resume_text:
                skills.append("Power BI")

            if "manual testing" in resume_text:
                skills.append("Software Testing")

            if (
                "html" in resume_text
                or "css" in resume_text
                or "bootstrap" in resume_text
                or "javascript" in resume_text
            ):
                skills.append("Frontend Development")

            all_skills = [
                "Python",
                "SQL",
                "Django",
                "Machine Learning",
                "Power BI",
                "Software Testing",
                "Frontend Development"
            ]

            for skill in all_skills:

                if skill not in skills:
                    missing_skills.append(skill)

            score = int(
                (len(skills) / len(all_skills)) * 100
            )

    return render(
        request,
        "analyze_resume.html",
        {
            "skills": skills,
            "missing_skills": missing_skills,
            "score": score
        }
    )


def signup_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if User.objects.filter(username=username).exists():

            return render(
                request,
                "signup.html",
                {
                    "error": "Username already exists"
                }
            )

        if password != confirm_password:

            return render(
                request,
                "signup.html",
                {
                    "error": "Passwords do not match"
                }
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return render(
            request,
            "signup.html",
            {
                "success": "Registration Successful"
            }
        )

    return render(
        request,
        "signup.html"
    )


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return render(
                request,
                "login.html",
                {
                    "success": "Login Successful"
                }
            )

        return render(
            request,
            "login.html",
            {
                "error": "Invalid Username or Password"
            }
        )

    return render(
        request,
        "login.html"
    )

def logout_view(request):
    logout(request)
    return render(request,
                  "login.html", {
                      "success":"Logout Successful"
                  }
                  )

def start_assessment(request):

    score = None

    if request.method == "POST":

        score = 0

        if request.POST.get("q1") == "C":
            score += 1

        if request.POST.get("q2") == "C":
            score += 1

        if request.POST.get("q3") == "B":
            score += 1

        if request.POST.get("q4") == "C":
            score += 1

        if request.POST.get("q5") == "B":
            score += 1

    return render(
        request,
        "start_assessment.html",
        {
            "score": score
        }
    )