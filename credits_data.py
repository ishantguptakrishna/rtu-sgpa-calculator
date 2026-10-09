"""
Credit database for RTU B.Tech CSE — all 8 semesters.
Based on the RTU CBCS scheme for students admitted from session 2021-22 onwards.
"""

# RTU 10-point absolute grading scale
GRADE_POINTS = {
    'A++': 10,
    'A+':  9,
    'A':   8.5,
    'B+':  8,
    'B':   7.5,
    'C+':  7,
    'C':   6.5,
    'D+':  6,
    'D':   5.5,
    'E+':  5,
    'E':   4,
    'F':   0,
}

# ── Master course-code → credit map ──────────────────────────────────────────
# Course codes are stored UPPERCASE.  The lookup function normalises input.

CREDITS_MAP = {

    # ── Semester 1 (common to all branches) ──────────────────────────────────
    # Exact codes may vary; these cover the most common RTU first-year codes.
    '1BS2-01': 4.0,   # Mathematics-I
    '1BS4-01': 4.0,   # Engineering Physics
    '1HS1-01': 2.0,   # Communication Skills / English
    '1ES4-01': 2.0,   # Basic Mechanical Engineering
    '1ES4-02': 2.0,   # Basic Civil Engineering
    '1BS4-21': 1.0,   # Physics Lab
    '1HS1-21': 1.0,   # Language Lab
    '1ES4-22': 1.5,   # Computer Programming Lab / Workshop
    '1ES4-23': 1.0,   # BCE Lab
    '1ES4-24': 1.5,   # CAMD (Computer Aided Machine Drawing)
    '1SO8-00': 0.5,   # SODECA
    '1XX8-00': 0.5,   # SODECA (alternate code)

    # ── Semester 1 & 2 (First Year FY codes) ─────────────────────────────────
    '2FY1-04': 2.0,   # Communication Skills
    '2FY1-05': 2.0,   # Human Values
    '2FY1-22': 1.0,   # Language Lab
    '2FY1-23': 1.0,   # Human Values Lab
    '2FY2-01': 4.0,   # Engineering Mathematics
    '2FY2-02': 4.0,   # Engineering Physics
    '2FY2-03': 4.0,   # Engineering Chemistry
    '2FY2-20': 1.0,   # Physics Lab
    '2FY2-21': 1.0,   # Chemistry Lab
    '2FY3-07': 2.0,   # Basic Mechanical Engineering
    '2FY3-08': 2.0,   # Basic Electrical Engineering
    '2FY3-09': 2.0,   # Basic Civil Engineering
    '2FY3-25': 1.5,   # Manufacturing Practices Workshop
    '2FY3-27': 1.0,   # Basic Civil Engineering Lab
    '2FY3-29': 1.5,   # Computer Aided Machine Drawing
    'FEC02': 0.5,     # Sports II / SODECA
    'FECO2': 0.5,     # OCR typo
    '1FY1-04': 2.0,
    '1FY1-05': 2.0,
    '1FY1-22': 1.0,
    '1FY1-23': 1.0,
    '1FY2-01': 4.0,
    '1FY2-02': 4.0,
    '1FY2-03': 4.0,
    '1FY2-20': 1.0,
    '1FY2-21': 1.0,
    '1FY3-06': 2.0,
    '1FY3-07': 2.0,
    '1FY3-08': 2.0,
    '1FY3-09': 2.0,
    '1FY3-24': 1.5,
    '1FY3-25': 1.5,
    '1FY3-26': 1.0,
    '1FY3-27': 1.0,
    '1FY3-28': 1.5,
    '1FY3-29': 1.5,
    '2FY1-04': 2.0,
    '2FY1-05': 2.0,
    '2FY3-06': 2.0,
    '2FY3-24': 1.5,
    '2FY3-26': 1.0,
    'FEC01': 0.5,

    # ── Semester 3 ───────────────────────────────────────────────────────────
    '3CS1-01': 2.0,
    '3CS1-02': 2.0,
    '3CS2-01': 3.0,
    '3CS3-04': 3.0,
    '3CS4-01': 3.0,
    '3CS4-02': 3.0,
    '3CS4-03': 3.0,
    '3CS4-04': 3.0,
    '3CS4-05': 3.0,
    '3CS4-06': 3.0,
    '3CS4-07': 3.0,
    '3CS4-21': 1.5,
    '3CS4-22': 1.5,
    '3CS4-23': 1.5,
    '3CS4-24': 1.5,
    '3CS7-10': 1.0,
    '3CS7-30': 1.0,
    '3CS8-00': 0.5,
    
    # AID Semester 3
    '3AID1-02': 2.0,
    '3AID2-01': 3.0,
    '3AID3-04': 3.0,
    '3AID4-05': 3.0,
    '3AID4-06': 3.0,
    '3AID4-07': 3.0,
    '3AID4-21': 1.5,
    '3AID4-22': 1.5,
    '3AID4-23': 1.5,
    '3AID4-24': 1.5,
    '3AID7-30': 1.0,
    '3CS4-24': 1.5,   # DE Lab
    '3CS7-10': 1.0,   # ITS / Minor Project
    '3CS8-00': 0.5,   # SODECA

    # ── Semester 4 ───────────────────────────────────────────────────────────
    '4CS2-01': 3.0,   # Discrete Mathematical Structures
    '4CS1-03': 2.0,   # Managerial Economics
    '4CS1-02': 2.0,   # Technical Communication
    '4CS3-04': 3.0,   # Microprocessor & Interfaces
    '4CS4-05': 3.0,   # Database Management Systems
    '4CS4-06': 3.0,   # Theory of Computation
    '4CS4-07': 3.0,   # Data Communication & Computer Networks
    '4CS4-21': 1.0,   # MPI Lab
    '4CS4-22': 1.5,   # DBMS Lab
    '4CS4-23': 1.5,   # Network Programming Lab
    '4CS4-24': 1.0,   # Linux System Programming Lab
    '4CS4-25': 1.0,   # Java Programming Lab
    '4CS8-00': 0.5,   # SODECA

    # ── Semester 5 ───────────────────────────────────────────────────────────
    '5CS3-01': 2.0,   # Info Theory & Coding / Data Mining
    '5CS4-02': 3.0,   # Compiler Design
    '5CS4-03': 3.0,   # Operating System
    '5CS4-04': 3.0,   # Computer Graphics & Multimedia Techniques
    '5CS4-05': 3.0,   # Analysis of Algorithms
    '5CS4-21': 1.0,   # CGMT Lab
    '5CS4-22': 1.0,   # CD Lab
    '5CS4-23': 1.0,   # AOA Lab
    '5CS4-24': 1.0,   # Java Advanced Lab
    '5CS5-12': 2.0,   # Human-Computer Interaction
    '5CS7-20': 2.5,   # Industrial Training (Summer)
    '5CS7-30': 2.5,   # Industrial Training Sem 5 (Alternate Code)
    '5CS8-00': 0.5,   # SODECA
    
    # AID Semester 5
    '5AID3-01': 2.0,
    '5AID4-02': 3.0,
    '5AID4-03': 3.0,
    '5AID4-04': 3.0,
    '5AID4-05': 3.0,
    '5AID4-21': 1.0,
    '5AID4-22': 1.0,
    '5AID4-23': 1.0,
    '5AID4-24': 1.0,
    '5AID5-13': 2.0,
    '5AID7-30': 2.5,

    # ── Semester 6 ───────────────────────────────────────────────────────────
    '6CS3-01': 2.0,   # Digital Image Processing
    '6CS4-02': 3.0,   # Machine Learning
    '6CS4-03': 2.0,   # Information Security Systems
    '6CS4-04': 3.0,   # Computer Architecture & Organization
    '6CS4-05': 2.0,   # Artificial Intelligence
    '6CS4-06': 3.0,   # Cloud Computing
    '6CS4-21': 1.5,   # DIP Lab
    '6CS4-22': 1.5,   # Machine Learning Lab
    '6CS4-23': 1.5,   # Python Lab
    '6CS4-24': 1.5,   # Mobile Application Development Lab
    '6CS8-00': 0.5,   # SODECA

    # ── Semester 7 ───────────────────────────────────────────────────────────
    '7CS4-01': 3.0,   # Internet of Things
    '7CS4-21': 2.0,   # IoT Lab
    '7CS4-22': 2.0,   # Cyber Security Lab
    '7CS7-30': 2.5,   # Industrial Training
    '5CS7-30': 2.5,   # Industrial Training Sem 5
    '7CS7-40': 2.0,   # Seminar
    '7CS8-00': 0.5,   # SODECA

    # ── Semester 8 ───────────────────────────────────────────────────────────
    '8CS4-01': 3.0,   # Big Data Analytics
    '8CS4-21': 1.0,   # Big Data Analytics Lab
    '8CS4-22': 1.0,   # Software Testing & Validation Lab
    '8CS7-50': 7.0,   # Project
    '8CS8-00': 0.5,   # SODECA

    # ── Common elective / non-CS codes seen on RTU results ───────────────────
    # Professional Electives (various semesters)
    '5CS5-01': 2.0,   # PE — Sem 5
    '5CS5-02': 2.0,
    '5CS5-03': 2.0,
    '5CS6-01': 2.0,   # OE — Sem 5
    '6CS5-01': 2.0,   # PE — Sem 6
    '6CS5-02': 2.0,
    '6CS5-03': 2.0,
    '6CS5-11': 2.0,   # Distributed System
    '6CS5-12': 2.0,   # SDN
    '6CS5-13': 2.0,   # Ecommerce & ERP
    '7CS6-01': 3.0,   # OE — Sem 7
    '7CS6-02': 3.0,
    '8CS6-01': 3.0,   # OE — Sem 8
    '8CS6-02': 3.0,

    # AID Branch Semester 6 & 4
    '6AID3-01': 2.0,
    '6AID4-02': 3.0,
    '6AID4-03': 2.0,
    '6AID4-04': 3.0,
    '6AID4-05': 2.0,
    '6AID4-06': 3.0,
    '6AID4-21': 1.5,
    '6AID4-22': 1.5,
    '6AID4-23': 1.5,
    '6AID4-24': 1.5,
    '6AID5-12': 2.0,
    '6AIDS-12': 2.0,  # OCR error for 5-12
    
    # AID Semester 4 (Matches CS)
    '4AID2-01': 3.0,
    '4AID1-03': 2.0,
    '4AID1-02': 2.0,
    '4AID3-04': 3.0,
    '4AID4-05': 3.0,
    '4AID4-06': 3.0,
    '4AID4-07': 3.0,
    '4AID4-21': 1.0,
    '4AID4-22': 1.5,
    '4AID4-23': 1.5,
    '4AID4-24': 1.0,
    '4AID4-25': 1.0,
    '4AID8-00': 0.5,

    # Foundation / FEC codes (non-departmental)
    'FEC17':   0.5,   # Public Speaking
    'FEC15':   0.5,   # Generic foundation elective
    'FEC16':   0.5,
    'FEC18':   0.5,
}

CDS_CODES = {
    # CDS Semester 3
    '3CDS1-02': 2.0, '3CDS2-01': 3.0, '3CDS3-04': 3.0, '3CDS4-05': 3.0, 
    '3CDS4-06': 3.0, '3CDS4-07': 3.0, '3CDS4-21': 1.5, '3CDS4-22': 1.5, 
    '3CDS4-23': 1.5, '3CDS4-24': 1.5, '3CDS7-30': 1.0,
    
    # CDS Semester 4
    '4CDS1-03': 2.0, '4CDS2-01': 3.0, '4CDS3-04': 3.0, '4CDS4-05': 3.0, 
    '4CDS4-06': 3.0, '4CDS4-07': 3.0, '4CDS4-21': 1.0, '4CDS4-22': 1.5, 
    '4CDS4-23': 1.5, '4CDS4-24': 1.0, '4CDS4-25': 1.0,
    
    # CDS Semester 5
    '5CDS-01': 2.0, '5CDS-02': 3.0, '5CDS-03': 3.0, '5CDS-04': 3.0, 
    '5CDS-05': 3.0, '5CDS-13': 2.0, '5CDS-21': 1.0, '5CDS-22': 1.0, 
    '5CDS-23': 1.0, '5CDS-24': 1.0, '5CDS-30': 2.5,
    
    # CDS Semester 6
    '6CDS-01': 2.0, '6CDS-02': 3.0, '6CDS-03': 2.0, '6CDS-04': 3.0, 
    '6CDS-05': 2.0, '6CDS-06': 3.0, '6CDS-11': 2.0, '6CDS-21': 1.5, 
    '6CDS-22': 1.5, '6CDS-23': 1.5, '6CDS-24': 1.5,
}
CREDITS_MAP.update(CDS_CODES)

CIT_CODES = {
    # CIT Semester 3
    '3CIT1-02': 2.0, '3CIT2-01': 3.0, '3CIT3-04': 3.0, '3CIT4-05': 3.0,
    '3CIT4-06': 3.0, '3CIT4-07': 3.0, '3CIT4-21': 1.5, '3CIT4-22': 1.5,
    '3CIT4-23': 1.5, '3CIT4-24': 1.5, '3CIT7-30': 1.0,
    
    # CIT Semester 4
    '4CIT1-03': 2.0, '4CIT2-01': 3.0, '4CIT3-04': 3.0, '4CIT4-05': 3.0,
    '4CIT4-06': 3.0, '4CIT4-07': 3.0, '4CIT4-21': 1.0, '4CIT4-22': 1.5,
    '4CIT4-23': 1.5, '4CIT4-24': 1.0, '4CIT4-25': 1.0,
    
    # CIT Semester 5
    '5CIT3-01': 2.0, '5CIT4-02': 3.0, '5CIT4-03': 3.0, '5CIT4-04': 3.0,
    '5CIT4-05': 3.0, '5CIT4-13': 2.0, '5CIT4-21': 1.0, '5CIT4-22': 1.0,
    '5CIT4-23': 1.0, '5CIT4-24': 1.0, '5CIT7-30': 2.5,
    
    # CIT Semester 6
    '6CIT3-01': 2.0, '6CIT4-02': 3.0, '6CIT4-03': 2.0, '6CIT4-04': 3.0,
    '6CIT4-05': 2.0, '6CIT4-06': 3.0, '6CIT4-21': 1.5, '6CIT4-22': 1.5,
    '6CIT4-23': 1.5, '6CIT4-24': 1.5, '6CIT5-13': 2.0,
}
CREDITS_MAP.update(CIT_CODES)

def get_credits_for_course(course_code: str) -> float:
    """
    Look up the credit value for a course code.
    Falls back to pattern-based heuristics when the code isn't in the map.
    """
    code = course_code.strip().upper()

    # 1. Exact match
    if code in CREDITS_MAP:
        return CREDITS_MAP[code]

    # 2. Partial / fuzzy match — strip spaces OCR might have inserted
    clean = code.replace(' ', '')
    if clean in CREDITS_MAP:
        return CREDITS_MAP[clean]

    # 3. Pattern-based inference
    #    Semester 7 generic codes
    if code.startswith('7'):
        if '4-01' in code or '6-60' in code:
            return 3.0
        if '4-21' in code or '4-22' in code:
            return 2.0
    #    Lab codes usually contain "-2" in the second part (e.g. 6CS4-21)
    if '-2' in code:
        return 1.5
    #    SODECA codes end with 8-00
    if '8-00' in code:
        return 0.5
    #    Training / Seminar codes contain 7-
    if '7-' in code:
        return 2.0
    #    FEC / foundation electives
    if code.startswith('FEC') or 'SODECA' in code or 'DECA' in code:
        return 0.5

    # 4. Default for unrecognised theory / elective subjects
    return 2.0
