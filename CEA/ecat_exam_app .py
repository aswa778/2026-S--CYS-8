# ============================================================
#  ECAT EXAM APPLICATION — DUAL PORTAL SYSTEM
#  Course : CMPE-112L  |  CEA Lab #1  |  UET Lahore
# ============================================================

import time   # time.sleep() aur time.strftime() ke liye

# ─────────────────────────────────────────────
#  CONSTANTS  (ek baar define, poore program mein use)
# ─────────────────────────────────────────────
CORRECT_MARKS  =  4
WRONG_MARKS    = -1
SKIP_MARKS     =  0
MIN_QUESTIONS  = 10

# ─────────────────────────────────────────────
#  PORTAL CREDENTIALS
# ─────────────────────────────────────────────
ADMIN_USERNAME   = "ecat_admin"
ADMIN_PASSWORD   = "ecat@2024"
STUDENT_USERNAME = "student"
STUDENT_PASSWORD = "student123"

# ─────────────────────────────────────────────
#  IN-MEMORY DATA STORAGE
# ─────────────────────────────────────────────

# questions  → list of dicts (har question ek dictionary hai)
questions = [
    {
        "id": 1,
        "subject": "Mathematics",
        "question": "What is the derivative of sin(x)?",
        "choices": {"A": "cos(x)", "B": "-cos(x)", "C": "-sin(x)", "D": "tan(x)"},
        "answer": "A"
    },
    {
        "id": 2,
        "subject": "Mathematics",
        "question": "What is the value of log₁₀(1000)?",
        "choices": {"A": "2", "B": "3", "C": "4", "D": "10"},
        "answer": "B"
    },
    {
        "id": 3,
        "subject": "Physics",
        "question": "What is the SI unit of electric current?",
        "choices": {"A": "Volt", "B": "Watt", "C": "Ampere", "D": "Ohm"},
        "answer": "C"
    },
    {
        "id": 4,
        "subject": "Physics",
        "question": "Which law states F = ma?",
        "choices": {"A": "Newton's 1st Law", "B": "Newton's 2nd Law",
                    "C": "Newton's 3rd Law", "D": "Ohm's Law"},
        "answer": "B"
    },
    {
        "id": 5,
        "subject": "Chemistry",
        "question": "What is the atomic number of Carbon?",
        "choices": {"A": "4", "B": "6", "C": "8", "D": "12"},
        "answer": "B"
    },
    {
        "id": 6,
        "subject": "Chemistry",
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "choices": {"A": "Oxygen", "B": "Carbon Dioxide", "C": "Nitrogen", "D": "Hydrogen"},
        "answer": "C"
    },
    {
        "id": 7,
        "subject": "English",
        "question": "Choose the correct spelling:",
        "choices": {"A": "Accomodate", "B": "Accommodate", "C": "Acomodate", "D": "Acommodate"},
        "answer": "B"
    },
    {
        "id": 8,
        "subject": "Mathematics",
        "question": "If x² = 49, what is the positive value of x?",
        "choices": {"A": "6", "B": "8", "C": "7", "D": "9"},
        "answer": "C"
    },
    {
        "id": 9,
        "subject": "Physics",
        "question": "Speed of light in vacuum is approximately:",
        "choices": {"A": "3×10⁶ m/s", "B": "3×10⁸ m/s", "C": "3×10¹⁰ m/s", "D": "3×10⁴ m/s"},
        "answer": "B"
    },
    {
        "id": 10,
        "subject": "Chemistry",
        "question": "What is the chemical formula of water?",
        "choices": {"A": "H₂O₂", "B": "HO", "C": "H₃O", "D": "H₂O"},
        "answer": "D"
    },
    {
        "id": 11,
        "subject": "Mathematics",
        "question": "What is the area of a circle with radius 7? (use π ≈ 22/7)",
        "choices": {"A": "144", "B": "154", "C": "164", "D": "174"},
        "answer": "B"
    },
    {
        "id": 12,
        "subject": "English",
        "question": "Which sentence is grammatically correct?",
        "choices": {
            "A": "He don't know.",
            "B": "She doesn't knows.",
            "C": "They doesn't go.",
            "D": "He doesn't know."
        },
        "answer": "D"
    },
]

# all_results → list of dicts (har student ka result ek dict)
all_results = []


# ============================================================
#  HELPER / UTILITY FUNCTIONS
# ============================================================

def print_line(char="=", length=60):
    """Decorative line print karta hai."""
    print(char * length)


def print_header(title):
    """Section header nicely print karta hai."""
    print_line()
    print(f"  {title}")
    print_line()


def calculate_grade(percentage):
    """
    Percentage dekar grade return karta hai.
    if/elif/else use kiya hai — yahi concept CEA mein cover hua hai.
    """
    if percentage >= 80:
        return "EXCELLENT"
    elif percentage >= 65:
        return "GOOD"
    elif percentage >= 50:
        return "AVERAGE"
    else:
        return "BELOW AVERAGE"


def get_max_score():
    """Maximum possible score calculate karta hai."""
    return len(questions) * CORRECT_MARKS


# ============================================================
#  ADMIN PORTAL FUNCTIONS
# ============================================================

def admin_login():
    """
    Admin login — 3 attempts ke baad lockout.
    while loop + if/elif use kiya hai.
    """
    print_header("ADMIN PORTAL LOGIN")
    attempts = 0

    while attempts < 3:                          # while loop — attempt count check
        username = input("  Username : ").strip()
        password = input("  Password : ").strip()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("\n  ✓ Login successful! Welcome, ECAT Admin.")
            time.sleep(1)                        # import time ka use
            return True
        else:
            attempts += 1                        # variable increment
            remaining = 3 - attempts
            if remaining > 0:
                print(f"  ✗ Invalid credentials. {remaining} attempt(s) left.\n")
            else:
                print("  ✗ Account locked after 3 failed attempts.")

    return False


def admin_view_questions():
    """Saare questions list karta hai — for loop use kiya."""
    print_header("ALL QUESTIONS IN QUESTION BANK")

    if len(questions) == 0:                      # len() use
        print("  No questions found.")
        return

    for idx in range(len(questions)):            # range() + len()
        q = questions[idx]
        print(f"\n  Q{idx + 1}. [{q['subject']}] {q['question']}")
        for key, val in q["choices"].items():    # dictionary .items() iterate
            marker = " ✓" if key == q["answer"] else ""
            print(f"       {key}) {val}{marker}")

    print()


def admin_add_question():
    """
    Naya question add karta hai — .append() use kiya.
    User se subject, question, 4 choices, correct answer leta hai.
    """
    print_header("ADD NEW QUESTION")

    subject  = input("  Subject          : ").strip()
    question = input("  Question text    : ").strip()
    choice_a = input("  Choice A         : ").strip()
    choice_b = input("  Choice B         : ").strip()
    choice_c = input("  Choice C         : ").strip()
    choice_d = input("  Choice D         : ").strip()

    # Correct answer validate karna — while loop + .upper()
    while True:
        answer = input("  Correct Answer (A/B/C/D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        print("  Please enter A, B, C, or D only.")

    new_id = questions[-1]["id"] + 1 if questions else 1   # last id + 1

    new_question = {                             # dictionary create ki
        "id"      : new_id,
        "subject" : subject,
        "question": question,
        "choices" : {"A": choice_a, "B": choice_b, "C": choice_c, "D": choice_d},
        "answer"  : answer
    }

    questions.append(new_question)              # .append() — list mein add
    print(f"\n  ✓ Question added successfully! Total: {len(questions)} questions.")


def admin_delete_question():
    """
    Question delete karta hai by number — .pop() use kiya.
    """
    print_header("DELETE QUESTION")

    if len(questions) == 0:
        print("  No questions to delete.")
        return

    admin_view_questions()

    while True:
        try:
            num = int(input("  Enter question number to delete (0 to cancel): "))
            if num == 0:
                return
            if 1 <= num <= len(questions):
                removed = questions.pop(num - 1)   # .pop() — list se remove
                print(f"\n  ✓ Question '{removed['question'][:40]}...' deleted.")
                break
            else:
                print(f"  Enter a number between 1 and {len(questions)}.")
        except ValueError:
            print("  Please enter a valid number.")


def admin_question_stats():
    """
    Subject-wise breakdown — dictionary use karke count kiya.
    """
    print_header("QUESTION BANK STATISTICS")
    print(f"  Total Questions : {len(questions)}\n")

    subject_count = {}                           # empty dictionary

    for q in questions:                          # for loop — iterate over list
        subj = q["subject"]
        if subj in subject_count:                # if/else — key check
            subject_count[subj] += 1
        else:
            subject_count[subj] = 1

    print("  Subject-wise Breakdown:")
    for subj, count in subject_count.items():    # dictionary iterate
        print(f"    {subj:<20} : {count} question(s)")
    print()


def admin_view_all_results():
    """
    Saare student results ka summary table — for loop."""
    print_header("ALL STUDENT RESULTS")

    if len(all_results) == 0:
        print("  No student results yet.")
        return

    # Table header
    print(f"  {'#':<4} {'Name':<20} {'Roll':<12} {'Score':<8} {'%':<8} {'Grade':<15} {'Time'}")
    print("  " + "-" * 80)

    for i, result in enumerate(all_results):    # enumerate — index + value
        print(
            f"  {i+1:<4} "
            f"{result['name']:<20} "
            f"{result['roll']:<12} "
            f"{result['score']:<8} "
            f"{result['percentage']:<8.1f} "
            f"{result['grade']:<15} "
            f"{result['time']}"
        )
    print()


def admin_view_detailed_result():
    """Per-student full question-by-question breakdown."""
    print_header("DETAILED STUDENT RESULT")

    if len(all_results) == 0:
        print("  No results available.")
        return

    admin_view_all_results()

    while True:
        try:
            num = int(input("  Enter student # to view details (0 to cancel): "))
            if num == 0:
                return
            if 1 <= num <= len(all_results):
                result = all_results[num - 1]
                break
            else:
                print(f"  Enter a number between 1 and {len(all_results)}.")
        except ValueError:
            print("  Please enter a valid number.")

    print_line("-")
    print(f"  Student : {result['name']}  |  Roll: {result['roll']}")
    print(f"  Score   : {result['score']} / {result['max_score']}")
    print(f"  Grade   : {result['grade']}  ({result['percentage']:.1f}%)")
    print(f"  Time    : {result['time']}")
    print_line("-")

    snapshot = result["snapshot"]                # snapshot of questions at exam time
    student_answers = result["answers"]          # student ka answers dict

    for idx in range(len(snapshot)):
        q          = snapshot[idx]
        given      = student_answers.get(idx, "S")   # .get() — default 'S'
        correct    = q["answer"]
        
        if given == "S":
            status = "SKIPPED"
        elif given == correct:
            status = "CORRECT ✓"
        else:
            status = f"WRONG ✗  (Correct: {correct})"

        print(f"\n  Q{idx+1}. {q['question']}")
        print(f"       Your Answer : {given}  →  {status}")
    print()


def admin_class_statistics():
    """Highest, lowest, average, pass/fail, grade distribution."""
    print_header("CLASS RESULT STATISTICS")

    if len(all_results) == 0:
        print("  No results available.")
        return

    scores      = [r["score"] for r in all_results]      # list comprehension
    percentages = [r["percentage"] for r in all_results]

    highest = max(scores)
    lowest  = min(scores)
    average = sum(scores) / len(scores)          # arithmetic operators

    pass_count = sum(1 for p in percentages if p >= 50)  # count pass (>=50%)
    fail_count = len(all_results) - pass_count

    print(f"  Total Students  : {len(all_results)}")
    print(f"  Highest Score   : {highest}")
    print(f"  Lowest Score    : {lowest}")
    print(f"  Average Score   : {average:.2f}")
    print(f"  Pass (>=50%)    : {pass_count}")
    print(f"  Fail (<50%)     : {fail_count}\n")

    # Grade distribution — dictionary use kiya
    grade_dist = {"EXCELLENT": 0, "GOOD": 0, "AVERAGE": 0, "BELOW AVERAGE": 0}
    for r in all_results:
        grade_dist[r["grade"]] += 1

    print("  Grade Distribution:")
    for grade, count in grade_dist.items():
        print(f"    {grade:<15} : {count}")
    print()


def admin_portal():
    """Admin portal ka main menu — while loop + if/elif."""
    if not admin_login():
        return

    while True:
        print_header("ADMIN PORTAL — MAIN MENU")
        print("  1. View All Questions")
        print("  2. Add New Question")
        print("  3. Delete a Question")
        print("  4. Question Bank Statistics")
        print("  5. View All Student Results")
        print("  6. View Detailed Result (Per Student)")
        print("  7. Class Result Statistics")
        print("  8. Logout")
        print()

        choice = input("  Enter your choice (1-8): ").strip()

        if   choice == "1": admin_view_questions()
        elif choice == "2": admin_add_question()
        elif choice == "3": admin_delete_question()
        elif choice == "4": admin_question_stats()
        elif choice == "5": admin_view_all_results()
        elif choice == "6": admin_view_detailed_result()
        elif choice == "7": admin_class_statistics()
        elif choice == "8":
            print("\n  Logged out. Goodbye, Admin!\n")
            break
        else:
            print("  Invalid choice. Please enter 1-8.\n")


# ============================================================
#  STUDENT PORTAL FUNCTIONS
# ============================================================

def student_login():
    """
    Student login — 3 attempts, name aur roll bhi leta hai.
    Returns (name, roll) if success, else (None, None).
    """
    print_header("STUDENT PORTAL LOGIN")
    attempts = 0

    while attempts < 3:
        username = input("  Username : ").strip()
        password = input("  Password : ").strip()

        if username == STUDENT_USERNAME and password == STUDENT_PASSWORD:
            print("\n  ✓ Credentials verified!")
            name = input("  Enter your Full Name : ").strip()
            roll = input("  Enter your Roll No   : ").strip()
            time.sleep(1)
            print(f"\n  Welcome, {name}!")
            return name, roll
        else:
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"  ✗ Invalid credentials. {remaining} attempt(s) left.\n")
            else:
                print("  ✗ Account locked after 3 failed attempts.")

    return None, None


def show_exam_rules():
    """Exam rules aur marking scheme display karta hai."""
    print_header("EXAM RULES & MARKING SCHEME")
    print("  • Total Questions  : Based on current question bank")
    print(f"  • Correct Answer   : +{CORRECT_MARKS} marks")
    print(f"  • Wrong Answer     : {WRONG_MARKS} mark")
    print(f"  • Skipped Question :  {SKIP_MARKS} marks")
    print()
    print("  Grade Boundaries:")
    print("    80% and above  → EXCELLENT")
    print("    65% – 79%      → GOOD")
    print("    50% – 64%      → AVERAGE")
    print("    Below 50%      → BELOW AVERAGE")
    print()
    print("  Instructions:")
    print("  • Type A / B / C / D to answer a question.")
    print("  • Type S to skip a question.")
    print("  • Type SUBMIT at any time to end the exam early.")
    print()


def conduct_exam(name, roll):
    """
    Exam conduct karta hai — main exam loop.
    for loop + while loop + if/elif + dictionary use kiya.
    Returns result dictionary.
    """
    print_header(f"EXAM STARTED — {name} ({roll})")
    print("  Type A/B/C/D to answer | S to skip | SUBMIT to end early\n")
    time.sleep(1)

    answers    = {}      # {question_index: 'A'/'B'/'C'/'D'/'S'} — dictionary
    submitted  = False

    # Exam questions ka snapshot lena (agar admin delete kare toh result safe rahe)
    snapshot = list(questions)                   # list copy

    for idx in range(len(snapshot)):             # for loop + range() + len()
        q = snapshot[idx]
        print_line("-", 50)
        print(f"  Question {idx + 1} of {len(snapshot)}  [{q['subject']}]")
        print(f"  {q['question']}")
        print()
        for key, val in q["choices"].items():
            print(f"    {key}) {val}")
        print()

        # Answer input loop — while loop + .upper() + .strip()
        while True:
            raw = input("  Your answer: ").strip().upper()

            if raw == "SUBMIT":                  # early submission
                submitted = True
                print("\n  ✓ Exam submitted early!")
                break
            elif raw in ["A", "B", "C", "D"]:
                answers[idx] = raw               # dictionary mein store
                break
            elif raw == "S":
                answers[idx] = "S"               # skip
                print("  Question skipped.\n")
                break
            else:
                print("  Invalid input. Enter A, B, C, D, S, or SUBMIT.")

        if submitted:
            break

    # ── Score calculate karna ──────────────────────────────
    correct = 0
    wrong   = 0
    skipped = 0

    for idx in range(len(snapshot)):
        given   = answers.get(idx, "S")          # .get() — default 'S' for unanswered
        correct_ans = snapshot[idx]["answer"]

        if given == "S":
            skipped += 1
        elif given == correct_ans:
            correct += 1
        else:
            wrong += 1

    score      = (correct * CORRECT_MARKS) + (wrong * WRONG_MARKS)  # arithmetic
    max_score  = len(snapshot) * CORRECT_MARKS
    percentage = (score / max_score) * 100 if max_score > 0 else 0
    grade      = calculate_grade(percentage)
    exam_time  = time.strftime("%Y-%m-%d %H:%M")                    # time.strftime()

    # ── Result display ─────────────────────────────────────
    print_header("YOUR RESULT")
    print(f"  Name            : {name}")
    print(f"  Roll Number     : {roll}")
    print(f"  Score           : {score} / {max_score}")
    print(f"  Correct         : {correct}  (×+{CORRECT_MARKS} = +{correct*CORRECT_MARKS})")
    print(f"  Wrong           : {wrong}  (×{WRONG_MARKS} = {wrong*WRONG_MARKS})")
    print(f"  Skipped         : {skipped}")
    print(f"  Percentage      : {percentage:.1f}%")
    print(f"  Grade           : {grade}")
    print(f"  Date & Time     : {exam_time}")

    # ── Per-question review ────────────────────────────────
    print_line("-")
    print("  ANSWER REVIEW:")
    for idx in range(len(snapshot)):
        q           = snapshot[idx]
        given       = answers.get(idx, "S")
        correct_ans = q["answer"]
        correct_text = q["choices"][correct_ans]

        if given == "S":
            status = "SKIPPED"
        elif given == correct_ans:
            status = "CORRECT ✓"
        else:
            given_text = q["choices"].get(given, "?")
            status = f"WRONG ✗  Your: {given}) {given_text} | Correct: {correct_ans}) {correct_text}"

        print(f"  Q{idx+1:<3} {status}")
    print()

    # ── Result dictionary banao aur all_results mein append karo ──
    result = {
        "name"      : name,
        "roll"      : roll,
        "score"     : score,
        "max_score" : max_score,
        "percentage": percentage,
        "grade"     : grade,
        "time"      : exam_time,
        "answers"   : answers,
        "snapshot"  : snapshot,
        "correct"   : correct,
        "wrong"     : wrong,
        "skipped"   : skipped,
    }

    all_results.append(result)                   # .append() — list mein add
    return result


def student_portal():
    """Student portal ka main menu."""
    name, roll = student_login()
    if name is None:
        return

    while True:
        print_header(f"STUDENT PORTAL — {name}")
        print("  1. Start Exam")
        print("  2. View Exam Rules")
        print("  3. Logout")
        print()

        choice = input("  Enter your choice (1-3): ").strip()

        if choice == "1":
            confirm = input("  Start exam now? (yes/no): ").strip().lower()
            if confirm == "yes":
                conduct_exam(name, roll)
                input("\n  Press Enter to return to menu...")
            else:
                print("  Exam cancelled.\n")
        elif choice == "2":
            show_exam_rules()
        elif choice == "3":
            print(f"\n  Goodbye, {name}! All the best!\n")
            break
        else:
            print("  Invalid choice. Enter 1, 2, or 3.\n")


# ============================================================
#  MAIN PROGRAM — Entry Point
# ============================================================

def main():
    """
    Program ka starting point.
    while loop se main menu chalti rehti hai jab tak exit na karo.
    """
    print_line("=", 60)
    print("       ECAT EXAM APPLICATION — DUAL PORTAL SYSTEM")
    print("         UET Lahore | CMPE-112L | CEA Lab #1")
    print_line("=", 60)
    print()

    while True:                                  # main program loop
        print("  Please select a portal:")
        print()
        print("  1. Admin Portal  (ECAT Team)")
        print("  2. Student Portal")
        print("  3. Exit Program")
        print()

        choice = input("  Enter 1, 2, or 3: ").strip()

        if   choice == "1": admin_portal()
        elif choice == "2": student_portal()
        elif choice == "3":
            print("\n  Thank you for using the ECAT Exam App. Goodbye!\n")
            break
        else:
            print("  Invalid choice. Please enter 1, 2, or 3.\n")


# ── Program yahan se start hota hai ──
if __name__ == "__main__":
    main()
