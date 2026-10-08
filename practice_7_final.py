"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

with open("/students analysis/students.csv", "r", encoding='utf-8') as f:
    next(f)
    lines = f.readlines()
ls = []
math_sum = 0
english_sum = 0
python_sum = 0
student_count = 0
best_name= ""
best_average = -1
for line in lines:
    line_1 = (line.strip("\n").split(","))
    name, numb1, numb2, numb3 = [line_1[0], int(line_1[1]), int(line_1[2]), int(line_1[3])]
    ls.append([name, numb1, numb2, numb3])
    sum_only = numb1 + numb2 + numb3
    student_count  += 1
    math_sum += numb1
    english_sum += numb2
    python_sum += numb3
    average_only = sum_only / 3
    if average_only > best_average:
        best_average = average_only
        best_name = name


english_aver = english_sum / student_count
math_aver = math_sum / student_count
python_leng_aver = python_sum / student_count


output_text = (
    'Середній бал по класу:'
    f"math: {round(math_aver, 1)}\n"
    f"english: {round(english_aver, 1)}\n"
    f"python_leng: {round(python_leng_aver, 1)}\n"
    f"Найкращий студент: {best_name} ({best_average})\n\n"
)

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
with open("/students analysis/result.txt", "w", encoding='utf-8') as f:
    f.write(output_text)
print(output_text)
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
