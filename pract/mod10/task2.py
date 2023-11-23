import re
import doctest
def color_valid(color: str) -> bool:
    """
    :param color: Параметры цвета
    :return Bool: Возвращает значение типа bool, (True - correct input; False - incorrect input)

    >>> color_valid("#21f48D")
    True
    >>> color_valid("#888")
    True
    >>> color_valid("rgb(255, 255,255)")
    True
    >>> color_valid("rgb(10%, 20%, 0%)")
    True
    >>> color_valid("hsl(200,100%,50%)")
    True
    >>> color_valid("hsl(0, 0%, 0%)")
    True
    >>> color_valid("#2345")
    False
    >>> color_valid("ffffff")
    False
    >>> color_valid("rgb(257, 50, 10)")
    False
    >>> color_valid("hsl(20, 10, 0.5)")
    False
    >>> color_valid("hsl(34%, 20%, 50%)")
    False
    """

    hex = re.fullmatch(r'^#([0-9a-fA-F]{3}){1,2}$', color)
    rgb_reg = r'^rgb\((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0%|100%) ?, ?(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0%|100%) ?, ?(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0%|100%)\)$'
    rgb = re.fullmatch(rgb_reg, color)
    hsl_reg = r'^hsl\((\d{1,2}|[1-2]\d{2}|3[0-5]\d) ?, ?(100%|\d{1,2}%) ?, ?(100%|\d{1,2}%)\)$'
    hsl = re.fullmatch(hsl_reg, color)
    percent_reg = r'rgb\(\s*((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)%\s*,\s*){2}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)%\s*\)'
    percent = re.fullmatch(percent_reg, color)

    if not(hex) and not(rgb) and not(hsl) and not(percent):
        return False

    return True


if __name__ == "__main__":
    doctest.testmod()