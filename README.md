# RTU SGPA Calculator

A Python CLI tool that **automatically** calculates your RTU (Rajasthan Technical University) SGPA from a result **screenshot** or **PDF** — no manual grade entry needed!

> Supports **all 8 semesters** of B.Tech CSE under the RTU CBCS scheme (2021-22 onwards).

---

## ✨ Features

| Feature | Description |
|---|---|
| 📸 **OCR Input** | Feed a result screenshot (PNG/JPG) or PDF |
| 🔍 **Auto Detection** | Automatically identifies the semester (I–VIII) |
| 📊 **Grade Extraction** | Reads course codes & grades from the result table |
| 🎓 **8 Semesters** | Full credit database for all 8 semesters |
| ⌨️ **Manual Mode** | Fallback `--manual` mode for manual grade entry |
| 🐛 **Debug Mode** | `--debug` flag to see raw OCR output |

---

## 📋 Prerequisites

1. **Python 3.10+**

2. **Tesseract OCR** — the OCR engine
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - During installation, note the install path (e.g. `C:\Program Files\Tesseract-OCR`)
   - Add Tesseract to your system **PATH**, or set it in Python:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
     ```

3. **Poppler** (only needed for PDF input)
   - Download from: https://github.com/oschwartz10612/poppler-windows/releases
   - Extract and add the `bin/` folder to your system **PATH**

---

## 🚀 Installation

```bash
cd C:\Users\gupta\.gemini\antigravity\scratch\rtu-sgpa-calculator
pip install -r requirements.txt
```

---

## 📖 Usage

### From a screenshot or PDF:
```bash
python main.py path/to/result.png
python main.py path/to/result.pdf
```

### Manual entry (fallback):
```bash
python main.py --manual
```

### Debug mode (see raw OCR text):
```bash
python main.py result.png --debug
```

---

## 📐 RTU Grading Scale

| Grade | Grade Point |
|:-----:|:-----------:|
| A++   | 10          |
| A+    | 9           |
| A     | 8.5         |
| B+    | 8           |
| B     | 7.5         |
| C+    | 7           |
| C     | 6.5         |
| D+    | 6           |
| D     | 5.5         |
| E+    | 5           |
| E     | 4           |
| F     | 0 (Fail)    |

**Formula:** `SGPA = Σ(Credit × GradePoint) / Σ(Credits)`

---

## 📁 Project Structure

```
rtu-sgpa-calculator/
├── main.py           # CLI entry point
├── ocr_engine.py     # Image/PDF → text (Tesseract OCR)
├── parser.py         # Text → semester, course codes, grades
├── credits_data.py   # Course code → credit mapping (all 8 sems)
├── calculator.py     # SGPA computation
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---|---|
| `TesseractNotFoundError` | Install Tesseract & add to PATH |
| `poppler not found` | Install Poppler & add `bin/` to PATH (for PDFs only) |
| No courses extracted | Try `--debug` to see OCR output, or use `--manual` |
| Wrong credits shown | Check `credits_data.py` and add missing course codes |
