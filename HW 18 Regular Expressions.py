
# 1. Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R,
# за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.

import re

def shablon (line):
    pattern = r'(Rb+r)'
    return re.findall(pattern, line)

print(shablon("HooofkmRr rBBBRkfdls dsgg rgRbrlhihRbbr jgrbbrugku "))

#
# 2. Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
#
import re

def card_validation(card_number):
    pattern = r'^(\d{4}-\d{4}-\d{4}-\d{4})$'
    return False if not re.search(pattern, card_number) else True

print(card_validation("1122-3344-5566-7788"))
print(card_validation("00000-3344-5566-7788"))

# 3. Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
# Вимоги:
# -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
# -у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
# -Символ "-" не може повторюватися.

import re

def mail_validation(mail):
    pattern = r'^[0-9A-Za-z](-?[0-9A-Za-z_])+@[0-9A-Za-z](-?[0-9A-Za-z._])+$'
    return False if not re.search(pattern, mail) else True

print(mail_validation('hysar@gmail.com'))
print(mail_validation('hysa@r@gmail.com'))


# 4. Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.

import re

def login_validation(login):
    pattern = r'^[a-zA-Z0-9]{2,10}$'
    return False if not re.search(pattern, login) else True

print(login_validation("112aqwe99k"))
print(login_validation("112%aqwe99k"))