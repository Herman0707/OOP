
# Подію додавання нового студента до групи необхідно фіксувати у лог-файлі.

import logging
logger=logging.getLogger("logging.py")

logger.setLevel(logging.INFO)


formatter=logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s')

cons=logging.StreamHandler()
cons.setLevel(logging.WARNING)
cons.setFormatter(formatter)



file=logging.FileHandler("logs/my_log.log")
file.setLevel(logging.INFO)
file.setFormatter(formatter)

logger.addHandler(file)
logger.addHandler(cons)




if __name__ =='logging.py':
    logger.info("Add student")
    logger.warning("Something was wrong")



