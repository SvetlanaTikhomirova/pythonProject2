'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
'''

class DivNaNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def div_na_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль невозможно")


div = DivNaNull(10, 100)
print(div.div_na_null(80, 0))
print(DivNaNull.div_na_null(2, 0))
print(DivNaNull.div_na_null(35, 0.1))
print(DivNaNull.div_na_null(35, 0.1))

