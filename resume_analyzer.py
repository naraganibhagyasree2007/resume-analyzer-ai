resume = input("Paste your resume text:\n")

skills = [
    "python",
    "machine learning",
    "ai",
    "sql",
    "communication",
    "html",
    "css",
    "java"
]

print("\n--- Resume Analysis ---")

score = 0

for skill in skills:
    if skill.lower() in resume.lower():
        print(f"{skill} skill found ✅")
        score += 1
    else:
        print(f"{skill} skill missing ❌")

print(f"\nResume Score: {score}/{len(skills)}")

print("\nSuggestions:")

if score < 4:
    print("- Add more technical skills")
    print("- Mention projects")
    print("- Include certifications")
else:
    print("- Your resume looks good 👍")