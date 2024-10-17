# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            pass
        else:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def two_values_sum(num_1, num_2):
    result = num_1 + num_2
    print("The sum of two numbers:", result)

    return result

two_values_sum(18, 945)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def mid_num_list(list):
    _sum = 0

    for i in list:
        _sum += i

    result = _sum / len(list)
    print("The arithmetic mean of the list:", result)

    return result

num_list = [6, 9, 82, 67, 8, 0, 112, 1, 34, 5, 6, 90]
mid_num_list(num_list)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_list(list):
    result = list[::-1]
    print(result)

    return result

random_list = [1, 6, 7, 'abc', 'string', 123213]
reverse_list(random_list)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(list):
    longest = ''

    for k in list:
        if len(k) > len(longest):
            longest = k

    print(' The longest word in the list:', longest)

    return longest

words_list = ['cat', 'apple', 'automobile', 'Planetenverteidigungskanonenkommandant', 'car', 'grape', 'butterfly']
longest_word(words_list)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# homework 04 | task 03
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
# Я зроблю функцію що фіксить криві пробіли у тексті
import re

text_with_unwanted_spaces = ("Lorem  ipsum odor  amet, consectetuer adipiscing elit.    Nisi nibh lectus nisi eget "
                             "montes quam. Nec   augue  vehicula metus  sodales       erat aptent purus.   Amet et ac "
                             "maecenas          felis eu aptent luctus adipiscing. Tincidunt   vehicula dictum mauris "
                             "non dis  volutpat. Interdum  pharetra   facilisi congue    amet potenti  sagittis "
                             "hac in     lacus. Tristique convallis      commodo curae amet sed    ligula.  Amet "
                             "nascetur senectus  interdum   quisque   tempus    lobortis.")

def fix_spaces(string):
    # Робимо змінну в яку буде зберігатися текст що буде пропускатися через регулярку яка заміняє усі пробіли що йдуть
    # підряд - на 1 пробіл
    fixed_text = re.sub(r'\s+', ' ', string)
    # Виводимо результат у консоль
    print(fixed_text)

    return fixed_text

# Приклад використання функції
fix_spaces(text_with_unwanted_spaces)

# task 8
# homework 04 | task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
# Створю функцію що підраховує кількість слів що починаються з великої букви

def count_words_with_uppercase(text):
    # Розбиваємо текст на слова і перевіряємо, чи починається кожне слово з великої літери
    upcase_count = sum(1 for word in text.split() if word[0].isupper())
    # Виводимо результат у консоль
    print('The number of words starting with a capital letter in the text:', upcase_count)
    return upcase_count

# Приклад використання функції
sample_text = "Tom and Huck went fishing. Aunt Polly was worried."
count = count_words_with_uppercase(sample_text)

# task 9
# homework 04 | task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# Зроблю функцію що розділяє текст по кінцю речення

def split_into_sentences(text):
    # Розділяємо текст на речення за допомогою регулярного виразу
    sentences = re.split(r'(?<=[.;]) +', text)
    # Виводимо результат у консоль
    print(sentences)
    return sentences

# Приклад використання функції
adventures_of_tom_sawyer = "Tom and Huck went fishing. Aunt Polly was worried; she thought they might be in danger."
sentences = split_into_sentences(adventures_of_tom_sawyer)

# task 10
# homework 04 | task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
# Створю функцію що буде перевіряти чи починається якесь речення з заданого значення у тексті

def find_sentence_starting_with_phrase(sentences, phrase):
    # Проходимо через кожне речення
    for sentence in sentences:
        # Перевіряємо, чи починається речення з вказаної фрази
        if sentence.startswith(phrase):
            print(f'Yes, this sentence begins with "{phrase}": {sentence}')

# Приклад використання функції
adventures_of_tom_sawyer_sentences = [
    "Tom and Huck went fishing.",
    "By the time they returned, it was dark.",
    "Aunt Polly was worried; she thought they might be in danger."
]

find_sentence_starting_with_phrase(adventures_of_tom_sawyer_sentences, 'By the time')

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""