"""
SGPA Calculator — computes Semester Grade Point Average
using the RTU 10-point absolute grading scale.

    SGPA = Σ(Credit_i × GradePoint_i) / Σ(Credit_i)
"""

from credits_data import GRADE_POINTS, get_credits_for_course


def calculate_sgpa(course_grades: list[dict]) -> tuple[float, list[dict]]:
    """
    Parameters
    ----------
    course_grades : list of dicts
        Each dict has keys  'code', 'title', 'grade'.

    Returns
    -------
    sgpa : float   – rounded to 2 decimal places
    results : list of dicts – one per course with full breakdown
    """
    total_credits = 0.0
    total_weighted = 0.0
    results: list[dict] = []

    for item in course_grades:
        code  = item['code']
        grade = item['grade'].upper().replace(' ', '')
        title = item.get('title', code)

        # Grade → grade point
        point = GRADE_POINTS.get(grade, 0)

        # Course code → credits
        credits = get_credits_for_course(code)

        earned = point * credits
        total_credits  += credits
        total_weighted += earned

        results.append({
            'title':         title,
            'code':          code,
            'grade':         grade,
            'point':         point,
            'credits':       credits,
            'earned_points': round(earned, 2),
        })

    import math
    sgpa = math.floor((total_weighted / total_credits) * 100) / 100 if total_credits > 0 else 0.0
    return sgpa, results
