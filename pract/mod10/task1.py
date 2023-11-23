import re
import doctest

def validate_password(password: str) -> bool:
    """
    Проверяет безопасность пароля и возвращает результат
    :param password: пароль
    :return: значение типа bool (True - безопасен; False - уязвим)

    >>> validate_password('rtG3FG!Tr^e')
    True
    >>> validate_password('aA1!*!1Aa')
    True
    >>> validate_password('oF^a1D@y5e6')
    True
    >>> validate_password('enroi#$rkdeR#$092uWedchf34tguv394h')
    True
    >>> validate_password('пароль')
    False
    >>> validate_password('password')
    False
    >>> validate_password('qwerty')
    False
    >>> validate_password('lOngPa$$$W0Rd')
    False
    """
    # пароль должен состоять из не менее чем шести символов
    if len(password) < 6:
        return False

    # пароль должен содержать по крайней мере два латинских символа в верхнем регистре
    if len(re.findall(r'[A-Z]', password)) < 2:
        return False

    # пароль должен содержать по крайней мере одну цифру
    if len(re.findall(r'\d', password)) < 1:
        return False

    # пароль должен содержать по крайней мере два различных специальных символа
    if len(re.findall(r'[$^%@#&*!?]', password)) < 2:
        return False

    # пароль не должен содержать трех одинаковых символов подряд
    if re.findall(r'(.)\1{2}', password):
        return False

    return True

if __name__ == '__main__':
    doctest.testmod()