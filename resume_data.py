"""
تمام محتوای رزومه در همین فایل است.
هر چیزی را که می‌خواهید عوض کنید، بعد بزنید:  python build.py
"""

resume = {
    "name": "Afagh KFN",
    "role": "International Language Instructor",

    "contacts": [
        {"icon": "email", "label": "kfnafagh@gmail.com", "url": "mailto:kfnafagh@gmail.com"},
        # ⬇️ لینک واقعی پروفایل Preply خود را اینجا بگذارید
        {"icon": "link", "label": "Preply Profile (Super Tutor)", "url": "https://preply.com"},
    ],

    "about": (
        "International language instructor and Super Tutor on Preply with more than one year "
        "of experience helping learners master advanced language skills. Outside the classroom "
        "I am a programmer — Python, HTML, and JavaScript are tools I work with, not subjects "
        "I teach. My academic background is in Management, which shapes the way I plan lessons "
        "and run my work."
    ),

    "experience": [
        {
            "title": "Super Tutor",
            "company": "Preply",
            # ⬇️ در صورت نیاز سال شروع را اصلاح کنید
            "date": "2025 — Present",
            "highlights": [
                "Super Tutor on Preply — recognized for high-quality lessons, reliability, and student satisfaction.",
                "Teaching advanced language skills to an international audience of learners.",
                "Designing personalized, goal-oriented lesson plans for learners at every level.",
                "More than one year of hands-on online teaching experience.",
            ],
        },
    ],

    "projects": [],

    "skills": [
        {"category": "Teaching Areas", "tags": ["Advanced Language"]},
        {"category": "Programming", "tags": ["Python", "HTML", "JavaScript", "CSS"]},
        {"category": "Tools & Platforms", "tags": ["Preply", "Online Tutoring", "Lesson Planning"]},
    ],

    "education": [
        # ⬇️ نام دانشگاه و سال را اضافه کنید (اختیاری)
        {"title": "Management", "school": "", "date": ""},
    ],
}
