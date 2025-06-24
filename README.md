
# 📄 Resume Analyzer CLI

A Python-based Command Line Interface tool that analyzes a PDF resume to:

- ✅ Extract text from PDF
- 🔍 Count keyword-based skill mentions
- 💡 Suggest improvements based on missing key skills

---

## 🚀 Features

- Reads `.pdf` resumes using [PyMuPDF](https://pymupdf.readthedocs.io/)
- Counts occurrences of essential tech skills (e.g., Python, SQL, Machine Learning)
- Outputs a clean summary table using `rich`
- Provides improvement suggestions based on missing skills

---

## 🧰 Tech Stack

- Python 3.x
- [PyMuPDF (`fitz`)](https://pypi.org/project/PyMuPDF/) – PDF text extraction
- [rich](https://pypi.org/project/rich/) – Beautiful CLI formatting

---

## 📦 Installation

Install the required dependencies:

```bash
pip install PyMuPDF rich
````

---

## 📝 Usage

Run the script with your resume as input:

```bash
python resume_analyzer.py your_resume.pdf
```

### ✅ Sample Output

![image](https://github.com/user-attachments/assets/5197adae-a025-4497-acc5-b7e4ba6fc931)

---

## 🧠 Customization

You can modify the list of target skills by editing the `TARGET_SKILLS` list in the script:

```python
TARGET_SKILLS = ["Python", "SQL", "Machine Learning", "NLP", "TensorFlow", "Pandas", "Java", "C++"]
```

---

## 📂 Project Structure

```
resume-analyzer-cli/
├── resume_analyzer.py
├── README.md
└── sample_resume.pdf (optional for testing)
```

---

## 📜 License

MIT License – feel free to use, modify, and distribute!

---

