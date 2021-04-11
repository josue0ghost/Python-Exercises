"""
    - Ask X student's grades
    - Show how many student's passed
    - Show how many student's failed
"""

student = int(input("How many students are?: "))
passed = 0
failed = 0

for count in range(1, student + 1):
    grade = float(input(f"Student {count} grade: "))
    if grade > 60:
        passed += 1
    else:
        failed += 1

print(f"{passed} students passed")
print(f"{failed} students failed")
