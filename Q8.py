def calculate_stats(student_name, *grades, **kwargs):
    """Calculates stats using *args for grades and **kwargs for extra details."""
    if not grades:
        return 0, 0, 0, {}

    lowest = min(grades)
    highest = max(grades)
    average = sum(grades) / len(grades)

    # Calculate letter score distributions
    dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades:
        if grade >= 90: dist['A'] += 1
        elif grade >= 80: dist['B'] += 1
        elif grade >= 70: dist['C'] += 1
        elif grade >= 60: dist['D'] += 1
        else: dist['F'] += 1

    course = kwargs.get("course", "Unknown Course")
    print(f"--- Stats for {student_name} ({course}) ---")

    # Returning multiple metrics as a tuple
    return lowest, highest, round(average, 2), dist


# Passing variable-length *args (grades) and **kwargs (course)
# Tuple unpacking receives the structured metrics
min_g, max_g, avg_g, distribution = calculate_stats(
    "Rahul", 85, 92, 76, 95, 64, 88, 91, 
    course="Data Science"
)

print(f"Min Grade: {min_g}")
print(f"Max Grade: {max_g}")
print(f"Average: {avg_g}")
print(f"Distribution: {distribution}")