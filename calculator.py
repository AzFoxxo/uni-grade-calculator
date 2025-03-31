"""
    @author: Az Foxxo (@AzFoxxo on GitHub)
    @date: 2025-03-28
    @description: Calculate grade percentage from currently completed parts
"""

from dataclasses import dataclass

def convert_grade_to_overall_percent(grade_on_test: float, total_grade_on_test:
    float, weight_overall: float) -> float:
    """Returns what percentage of overall grade the test results are worth.

    Args:
        grade_on_test (float): Grade got on test
        total_grade_on_test (float): Total grade on test if 100% correct
        weight_overall (float): Weight of the test for module grade

    Returns:
        float: Percentage of overall grade that the test results are worth
    """

    # Calculate what percentage of the test was correct
    percent_correct: float = grade_on_test / total_grade_on_test

    return percent_correct * weight_overall

@dataclass
class Results:
    """Results for a test/assignment"""
    grade_on_test: float
    total_grade_on_test: float
    weight_overall: float

# Module results
module_results: list[Results] = [
    # Percentage, Total, Weight
    # Content quizzes
    Results(0, 35, 15), # Quiz 1
    Results(0, 35.0, 15), # Quiz 2
    Results(0, 35.0, 15), # Quiz 3

    # Assignment Quiz
    Results(0, 10, 5), # Quiz 4

    # Assignment
    Results(0, 100.0, 20), # Research (20% super-conservative estimate)
    Results(0, 100.0, 30), # Code (20% super-conservative estimate)
]

# Calculate overall percentage
overall_percent: float = 0
mark_required: float = 40
for result in module_results:
    overall_percent += convert_grade_to_overall_percent(result.grade_on_test,
    result.total_grade_on_test, result.weight_overall)

# Display results
print(f"Overall percentage: {overall_percent:.2f}%")
print(f"Pass mark for module: {mark_required:.2f}% - short: {mark_required - overall_percent:.2f}%")
