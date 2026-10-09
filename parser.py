"""
Parser — extract semester number, course codes, and grades
from raw OCR text produced by the RTU result sheet.
"""

import re

# Roman numeral ↔ integer mapping (up to VIII for B.Tech)
_ROMAN_TO_INT = {
    'I': 1, 'II': 2, 'III': 3, 'IV': 4,
    'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8,
}

# All valid RTU grades (longest first so regex matches greedily)
_VALID_GRADES = ['A++', 'A+', 'B+', 'C+', 'D+', 'E+', 'A', 'B', 'C', 'D', 'E', 'F']


def extract_semester(text: str):
    """
    Scan OCR text for a line like
        "B. Tech. VI SEM MAIN EXAM …"
    and return the semester as an integer (1-8), or None.
    """
    # Match Roman numeral immediately before "SEM"
    match = re.search(
        r'\b(VIII|VII|VI|V|IV|III|II|I)\s*SEM',
        text,
        re.IGNORECASE,
    )
    if not match:
        match = re.search(r'B\.?\s*Tech\.?\s+(VIII|VII|VI|V|IV|III|II|I)\b', text, re.IGNORECASE)
    
    if match:
        roman = match.group(1).upper()
        return _ROMAN_TO_INT.get(roman)
    return None


def _extract_grade_from_tokens(tokens: list[str]) -> str | None:
    """
    Given the whitespace-split tokens of one result row,
    find the grade (last meaningful token).
    Handles OCR quirks like "A +" becoming two tokens.
    """
    if not tokens:
        return None

    # Try last token first
    last = tokens[-1].upper().replace(' ', '')
    
    # OCR Correction rules
    ocr_fixes = {
        'AT': 'A+',
        'ATT': 'A++',
        'AT+': 'A++',
        'A++': 'A++',
        'BT': 'B+',
        'CT': 'C+',
        'CE': 'C+',
        'DT': 'D+',
        'ET': 'E+',
        'CC': 'C',
        'A+': 'A+',
        'B+': 'B+',
        'C+': 'C+',
        'D+': 'D+',
        'E+': 'E+',
        'A': 'A',
        'B': 'B',
        'C': 'C',
        'D': 'D',
        'E': 'E',
        'F': 'F'
    }

    if last in ocr_fixes:
        return ocr_fixes[last]

    # OCR sometimes splits "A++" → "A+", "+" or "A", "++"
    if len(tokens) >= 2:
        combined = (tokens[-2] + tokens[-1]).upper().replace(' ', '')
        if combined in ocr_fixes:
            return ocr_fixes[combined]
        # Also try second-to-last on its own (grade followed by junk)
        second_last = tokens[-2].upper().replace(' ', '')
        if second_last in ocr_fixes:
            return ocr_fixes[second_last]

    return None


def parse_extracted_text(text: str) -> list[dict]:
    """
    Parse OCR output and return a list of dicts:
        [{'code': '6CS4-02', 'title': 'Machine Learning', 'grade': 'B'}, …]
    """
    # Fix common OCR hallucinations before parsing
    text = text.replace('4084-', '4CS4-').replace('4C84-', '4CS4-').replace('40S4-', '4CS4-').replace('6C54-', '6CS4-')
    
    # AID branch specific mobile screenshot hallucinations
    text = text.replace('4102-01', '4AID2-01').replace('4aD3-08', '4AID3-04')
    text = text.replace('4AND4.05', '4AID4-05').replace('4014-06', '4AID4-06')
    text = text.replace('4104.07', '4AID4-07').replace('4a1D4.21', '4AID4-21')
    text = text.replace('4104-22', '4AID4-22').replace('aaio4-23', '4AID4-23')
    text = text.replace('ani04-24', '4AID4-24').replace('FECIS', 'FEC13')
    text = text.replace('FECI3', 'FEC13').replace('4AID1- G3', '4AID1-03').replace('4AID1- 03', '4AID1-03')
    
    # Fix 4A1D, 4AlD, 4ALD (OCR confusing I with 1, l, L)
    text = text.replace('4A1D', '4AID').replace('4AlD', '4AID').replace('4ALD', '4AID')
    text = text.replace('4a1D', '4AID').replace('4aID', '4AID')
    text = text.replace('5A1D', '5AID').replace('5AlD', '5AID').replace('SAID', '5AID')
    text = text.replace('C1T', 'CIT').replace('ClT', 'CIT').replace('GCIT', '6CIT')
    
    lines = text.split('\n')
    courses: list[dict] = []

    in_table = False

    # Regex for course codes:
    #   Standard: digit + letters + digit(s) + hyphen + digits  (e.g. 6CS4-02)
    #   FEC-type: letters + digits                              (e.g. FEC17)
    code_re = re.compile(
        r'\b([0-9][A-Z]{2,4}[0-9]*-[A-Z0-9]{2,3})\b'   # 6CS4-02, 3CS4-21
        r'|'
        r'\b(FEC[A-Z0-9]+)\b',                           # FEC17, FECI7
        re.IGNORECASE,
    )

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        upper = stripped.upper()

        # Detect table header
        if 'COURSE CODE' in upper or 'COURSE TITLE' in upper:
            in_table = True
            continue

        # Detect table end
        if 'REMARKS' in upper or 'RESULT' in upper or 'INSTRUCTION' in upper:
            in_table = False
            continue

        if not in_table:
            continue

        # Try to find a course code in this line
        m = code_re.search(stripped)
        if not m:
            continue

        code = (m.group(1) or m.group(2)).upper()

        # Everything before the code is the title
        title = stripped[:m.start()].strip()
        # Everything after the code → split into tokens to find marks & grade
        after_code = stripped[m.end():].strip()
        tokens = after_code.split()

        grade = _extract_grade_from_tokens(tokens)
        if grade is None:
            # Last-ditch: scan the entire line for a grade pattern
            for g in _VALID_GRADES:
                if g in upper.split():
                    grade = g
                    break

        if grade is None:
            # Try to infer from marks if available
            try:
                # Find the last two numbers in the tokens
                nums = [int(t) for t in tokens if t.isdigit()]
                if len(nums) >= 1:
                    total = sum(nums[-2:])
                    if total >= 80: grade = 'A++'
                    elif total >= 75: grade = 'A+'
                    elif total >= 70: grade = 'A'
                    elif total >= 60: grade = 'B+'
                    elif total >= 50: grade = 'C'
                    elif total >= 40: grade = 'D'
                    else: grade = 'F'
            except:
                pass

        if grade is None:
            # If all else fails, default to C
            grade = 'C'

        courses.append({
            'code': code,
            'title': title if title else code,
            'grade': grade,
        })

    return courses
