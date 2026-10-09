"""
RTU SGPA Calculator — CLI entry point.

Usage
-----
    python main.py  result.png          # from screenshot
    python main.py  result.pdf          # from PDF
    python main.py  --manual            # type grades by hand
"""

import argparse
import sys
from tabulate import tabulate

from ocr_engine import extract_text_from_file
from parser import parse_extracted_text, extract_semester
from calculator import calculate_sgpa
from credits_data import GRADE_POINTS


# ── Manual entry mode ────────────────────────────────────────────────────────

def manual_entry():
    """Prompt the user to enter course codes and grades interactively."""
    print("\n--- Manual SGPA Entry ---")
    print("Enter each course code and its grade.  Type 'q' when done.\n")

    valid = ', '.join(GRADE_POINTS.keys())
    courses = []

    while True:
        code = input("Course Code (or 'q' to finish): ").strip()
        if code.lower() == 'q':
            break
        grade = input("Grade: ").strip().upper()
        if grade not in GRADE_POINTS:
            print(f"  ⚠  Invalid grade.  Choose from: {valid}\n")
            continue

        courses.append({'code': code.upper(), 'title': 'Manual Entry', 'grade': grade})
        print("  ✓  Added.\n")

    if not courses:
        print("No courses entered — nothing to calculate.")
        return

    sgpa, results = calculate_sgpa(courses)
    _display_results(None, results, sgpa)


# ── Pretty output ────────────────────────────────────────────────────────────

def _display_results(semester, results, sgpa):
    """Print a formatted table with the full SGPA breakdown."""
    print()
    print("=" * 70)
    if semester:
        print(f"  RTU SGPA CALCULATOR — SEMESTER {semester}")
    else:
        print("  RTU SGPA CALCULATOR")
    print("=" * 70)

    rows = []
    for r in results:
        rows.append([
            r['title'][:35],
            r['code'],
            r['credits'],
            r['grade'],
            r['point'],
            r['earned_points'],
        ])

    headers = ["Subject", "Code", "Credits", "Grade", "GP", "Cr × GP"]
    print(tabulate(rows, headers=headers, tablefmt="grid", numalign="center"))

    total_credits = sum(r['credits'] for r in results)
    total_earned  = sum(r['earned_points'] for r in results)
    print(f"\n  Total Credits      : {total_credits}")
    print(f"  Weighted Total     : {total_earned}")
    print(f"  ─────────────────────────────")
    print(f"  ★  SGPA            : {sgpa}\n")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(
        description="RTU SGPA Calculator — compute SGPA from a result screenshot / PDF."
    )
    ap.add_argument("file", nargs="?", help="Path to result PDF or image (PNG/JPG)")
    ap.add_argument("--manual", action="store_true", help="Enter grades manually instead")
    ap.add_argument("--debug", action="store_true", help="Print raw OCR text for debugging")

    args = ap.parse_args()

    # ── Manual mode ──
    if args.manual:
        manual_entry()
        sys.exit(0)

    # ── File mode ──
    if not args.file:
        print("Error: provide a file path, or use  --manual")
        ap.print_help()
        sys.exit(1)

    print(f"\n📄 Processing: {args.file} ...")

    try:
        text = extract_text_from_file(args.file)

        if args.debug:
            print("\n── RAW OCR TEXT ──")
            print(text)
            print("── END ──\n")

        semester = extract_semester(text)
        courses  = parse_extracted_text(text)

        if not courses:
            print(
                "\n⚠  Could not extract any courses / grades.\n"
                "   Possible causes:\n"
                "     • Image quality too low for OCR\n"
                "     • Unexpected result sheet layout\n"
                "   Try:  python main.py --manual\n"
            )
            sys.exit(1)

        sgpa, results = calculate_sgpa(courses)
        _display_results(semester, results, sgpa)

    except FileNotFoundError as e:
        print(f"\n❌  {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌  Error processing file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
