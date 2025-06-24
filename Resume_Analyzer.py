import fitz  # PyMuPDF
import sys
from collections import Counter
from rich import print
from rich.console import Console
from rich.table import Table

# Predefined skill keywords to search
TARGET_SKILLS = ["Python", "SQL", "Machine Learning", "Deep Learning", "Data Analysis", "NLP", "Java", "C++", "Pandas", "TensorFlow"]

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"[red]Error reading PDF:[/red] {e}")
        sys.exit(1)

def analyze_skills(text):
    word_list = text.split()
    counter = Counter(word_list)
    found_skills = {skill: counter.get(skill, 0) for skill in TARGET_SKILLS}
    return found_skills

def suggest_improvements(skill_counts):
    missing = [skill for skill, count in skill_counts.items() if count == 0]
    return missing

def main():
    if len(sys.argv) != 2:
        print("[yellow]Usage: python resume_analyzer.py <resume.pdf>[/yellow]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    text = extract_text_from_pdf(pdf_path)
    skill_counts = analyze_skills(text)
    suggestions = suggest_improvements(skill_counts)

    console = Console()
    table = Table(title="Resume Skill Analysis")

    table.add_column("Skill", style="cyan", justify="left")
    table.add_column("Mentions", style="green", justify="right")

    for skill, count in skill_counts.items():
        table.add_row(skill, str(count))

    console.print(table)

    if suggestions:
        print(f"[bold red]\nSuggestions:[/bold red] Consider adding or emphasizing these skills: {', '.join(suggestions)}")
    else:
        print("[bold green]\nGreat! All key skills are mentioned.[/bold green]")

if __name__ == "__main__":
    main()
