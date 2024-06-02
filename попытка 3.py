def isPhoneNumber(text):

    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal:
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal:
            return False

    if text[7] != '-':
        return False

    for i in range(7,12):
        if not text[i].isdecimal:
            return False

    return True

messege = 'позвони по номеру - 234-234-2344 мой номер телеФОНА - 2344-234-234'
chunk = []
for i in range (messege):
    if messege[i].isdecimal():
        chunk.append([i])


    if isPhoneNumber(chunk):
        print('Найденный номер телефона', + chunk)

