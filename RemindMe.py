import time
import easygui

todo = easygui.enterbox("Про що ви хочете зробити нагадування?\n текст виведется по настанню часу\n","Нагадування")

try:
    totime = easygui.enterbox("Введіть час в форматі HH:MM (Наприклад 14:30)\n","Нагадування").split(":")

    if len(totime) !=2:
        easygui.msgbox("Некоректний формат часу! Введіть у форматі HH:MM (наприклад, 14:30).", "Помилка")

    elif not (0 <= int(totime[0]) < 24):
        easygui.msgbox("Година повинна бути в діапазоні від 0 до 23!", "Помилка")

    elif not (0 <= int(totime[1]) < 60):
        easygui.msgbox("Хвилини повинні бути в діапазоні від 0 до 59!", "Помилка")

    else:
        easygui.msgbox("Нагадування встановлено","Нагадування")
        lt = time.localtime()
        while lt.tm_hour != int(totime[0]) or lt.tm_min != int(totime[1]):
            lt = time.localtime()
            time.sleep(15)

        easygui.msgbox(f"Час настав!\n{todo}","Нагадування")

except ValueError:
    easygui.msgbox("Години та хвилини повинні бути цілими числами!","Помилка")
