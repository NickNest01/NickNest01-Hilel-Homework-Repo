adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('Кількість букв "h" у тексті:', adwentures_of_tom_sawer.count('h'))

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
upcase_count = 0

for letter in adwentures_of_tom_sawer:
    if letter.isupper():
        upcase_count += 1

print('Кількість слів що починається з першої букви у тексті:', upcase_count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_word_idx = adwentures_of_tom_sawer.find('Tom')

second_word_idx = adwentures_of_tom_sawer.find('Tom', first_word_idx + 1)
print('Позиція на якій слово "Tom" зустрічається вдруге:', second_word_idx)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
import re

adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.;]) +', adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
# Але воно ж і так у нижньому регістрі 🤔
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith('By the time'):
        print('Так, з "By the time" починається ось це речення:', sentence)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_last_sentence = adwentures_of_tom_sawer_sentences[-1].split(' ')
print('У останьому реченні з adwentures_of_tom_sawer_sentences -', len(adwentures_of_tom_sawer_last_sentence), 'слова.')
