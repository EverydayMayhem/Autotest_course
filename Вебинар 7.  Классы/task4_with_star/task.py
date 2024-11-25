class RomanNums:
    def __init__(self, roman_num):
        self.roman_num = roman_num

    def from_roman(self):
        """Перевод римской записи числа в арабскую"""
        roman_num = self.roman_num
        # решаем обратную задачу из вебинара по словарям. Создадим словарь, где ключ = римская цифра, а значение - арабская

        dict = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        # будем проходить входную строку циклом while, будем брать по 2 элемента - потому что цифры в ключах у нас либо единичные, либо двойные
        # если двойной символ найден - записываем соответствующее ему значение в словаре к нашему числу,
        # если не найден, или длина строки меньше 2, то берем один символ
        counter = 0
        result = 0

        while counter < len(roman_num):
            if counter + 1 < len(roman_num) and roman_num[counter:counter+2] in dict: # ищем по ключу
                result+= dict[roman_num[counter:counter+2]] # плюсуем знеачение найденного ключа (подстроки из двух символов)
                counter += 2
            else:
                result += dict[roman_num[counter]]
                counter += 1
        return result

    def is_palindrome(self):
        """Является ли число палиндромом """
        roman_num = self.roman_num
        print(roman_num)
        palindrome = RomanNums.from_roman(self)
        is_paly = False
        palindrome_str = str(palindrome)
        if palindrome_str == palindrome_str[::-1]:
            is_paly = True
        return is_paly
