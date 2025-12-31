import tkinter as tk
from tkinter import ttk, messagebox
import random

# =====================================================
# SUBJECT BANKS (Category-wise)
# =====================================================

politics_subjects = [
    "Central Government",
    "State Government",
    "Opposition Leaders",
    "Election Commission",
    "Parliament Committee",
    "Finance Ministry",
    "Prime Minister",
    "Cabinet Ministers",
    "Senior Bureaucrats",
    "Political Analysts"
]

education_subjects = [
    "University Administration",
    "College Students",
    "Engineering Students",
    "Medical Aspirants",
    "Education Board",
    "Exam Authorities",
    "Private Institutions",
    "Final Year Students",
    "Research Scholars",
    "Coaching Institutes"
]

technology_subjects = [
    "Software Engineers",
    "AI Researchers",
    "Cyber Security Experts",
    "IT Companies",
    "Data Scientists",
    "App Developers",
    "Robotics Engineers",
    "Cloud Architects",
    "Tech Startups",
    "Technology Analysts"
]

health_subjects = [
    "Medical Experts",
    "Doctors Association",
    "Health Ministry",
    "Nutritionists",
    "Hospital Authorities",
    "Public Health Officials",
    "Medical Colleges",
    "Fitness Trainers",
    "Pharmaceutical Companies"
]

sports_subjects = [
    "Cricket Analysts",
    "Football Coaches",
    "National Team Players",
    "Sports Authorities",
    "Olympic Committee",
    "Athletes",
    "Sports Scientists",
    "League Organizers"
]

# =====================================================
# COMMON WORD BANKS
# =====================================================

verbs = [
    "announce",
    "reveal",
    "discover",
    "confirm",
    "introduce",
    "claim",
    "deny",
    "celebrate",
    "question",
    "propose"
]

objects = [
    "a new policy",
    "a shocking truth",
    "an unexpected result",
    "a controversial decision",
    "a secret strategy",
    "a revolutionary plan",
    "a surprising outcome",
    "a bold initiative"
]

modifiers = [
    "to improve performance",
    "before the upcoming season",
    "to reduce workload",
    "using artificial intelligence",
    "after detailed analysis",
    "amid public reaction",
    "as a pilot initiative",
    "to attract global attention"
]

# =====================================================
# HEADLINE GENERATION LOGIC
# =====================================================

def generate_headline(category):
    if category == "Politics":
        subject = random.choice(politics_subjects)
    elif category == "Education":
        subject = random.choice(education_subjects)
    elif category == "Technology":
        subject = random.choice(technology_subjects)
    elif category == "Health":
        subject = random.choice(health_subjects)
    elif category == "Sports":
        subject = random.choice(sports_subjects)
    else:
        subject = "Experts"

    verb = random.choice(verbs)
    obj = random.choice(objects)
    modifier = random.choice(modifiers)

    return f"{subject} {verb} {obj} {modifier}"

# =====================================================
# GUI EVENT HANDLER
# =====================================================

def on_generate():
    selected_category = category_var.get()

    if selected_category == "Select Category":
        messagebox.showwarning(
            "Input Required",
            "Please select a category before generating a headline."
        )
        return

    headline = generate_headline(selected_category)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, headline)

# =====================================================
# GUI SETUP
# =====================================================

root = tk.Tk()
root.title("Fake News Headline Generator")
root.geometry("700x450")
root.resizable(False, False)

# Title Label
title_label = tk.Label(
    root,
    text="Fake News Headline Generator",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

# Category Selection
category_frame = tk.Frame(root)
category_frame.pack(pady=10)

category_label = tk.Label(
    category_frame,
    text="Select Category:",
    font=("Arial", 12)
)
category_label.pack(side=tk.LEFT, padx=10)

category_var = tk.StringVar()
category_dropdown = ttk.Combobox(
    category_frame,
    textvariable=category_var,
    state="readonly",
    width=25
)
category_dropdown["values"] = (
    "Select Category",
    "Politics",
    "Education",
    "Technology",
    "Health",
    "Sports"
)
category_dropdown.current(0)
category_dropdown.pack(side=tk.LEFT)

# Generate Button
generate_button = tk.Button(
    root,
    text="Generate Headline",
    font=("Arial", 12, "bold"),
    command=on_generate,
    bg="#2c3e50",
    fg="white",
    padx=10,
    pady=5
)
generate_button.pack(pady=20)

# Output Box
output_label = tk.Label(
    root,
    text="Generated Headline:",
    font=("Arial", 12)
)
output_label.pack(pady=5)

output_text = tk.Text(
    root,
    height=4,
    width=70,
    font=("Arial", 11),
    wrap=tk.WORD
)
output_text.pack(pady=10)

# Disclaimer
disclaimer_label = tk.Label(
    root,
    text="Disclaimer: This application generates synthetic headlines for educational purposes only.",
    font=("Arial", 9),
    fg="gray"
)
disclaimer_label.pack(side=tk.BOTTOM, pady=10)

# =====================================================
# APPLICATION START
# =====================================================

root.mainloop()