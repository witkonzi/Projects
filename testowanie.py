def nwd(meter,denominator) -> int:
    list_for_dividers = []
    for number in range(1,min(meter,denominator)+1):
        if meter % number == 0 and denominator % number == 0:
            list_for_dividers.append(number)
    if list_for_dividers:
        return max(list_for_dividers)
    else :
        return 1

class Fraction:
    def __init__(self,meter: int,denominator: int) -> None:
        self._meter = meter
        self._denominator = denominator

    def get_meter(self) -> int:
        return self._meter
    def get_denominator(self) -> int:
        return self._denominator

    def __str__(self) -> str:
        return f'Your fraction : {self._meter}/{self._denominator}'

    def formatting_fractions(self,other_fraction,formula : str):
        meter_main_fraction = self.get_meter() * other_fraction.get_denominator()
        meter_other_fraction = other_fraction.get_meter() * self.get_denominator()
        new_denominator = self.get_denominator() * other_fraction.get_denominator()
        new_meter = 0
        match formula:
            case "+":
                new_meter = meter_main_fraction + meter_other_fraction
            case "-":
                new_meter = meter_main_fraction - meter_other_fraction
            case "*":
                new_meter = meter_main_fraction * meter_other_fraction
                new_denominator = new_denominator * new_denominator
            case "/":
                new_meter = meter_main_fraction * new_denominator
                new_denominator = meter_other_fraction * new_denominator
        divider = nwd(new_meter, new_denominator)
        formatted_meter = new_meter / divider
        formatted_denominator = new_denominator / divider
        if formatted_meter == 0 :
            return 0
        elif formatted_meter == 1 and formatted_denominator == 1:
            return 1
        elif formatted_denominator == 1:
            return int(formatted_meter)
        else :
            return f'{int(formatted_meter)}/{int(formatted_denominator)}'

    def add_fractions(self,other_fraction) -> str:
        formated_add = self.formatting_fractions(other_fraction,"+")
        return f'New fraction after adding : {formated_add}'

    def subtract_fractions(self,other_fraction) -> str:
        formated_subtract = self.formatting_fractions(other_fraction, "-")
        return f'New fraction after subtracting : {formated_subtract}'

    def multiply_fractions(self,other_fraction) -> str:
        formated_multiply = self.formatting_fractions(other_fraction, "*")
        return f'New fraction after Multiplying : {formated_multiply}'

    def divide_fractions(self,other_fraction) -> str:
        formated_divide = self.formatting_fractions(other_fraction, "/")
        return f'New fraction after Dividing : {formated_divide}'

fraction_1 = Fraction(1,4)
fraction_2 = Fraction(1,4)
print(fraction_1.__str__())
print(fraction_2.__str__())
print(fraction_1.add_fractions(fraction_2))
print(fraction_1.subtract_fractions(fraction_2))
print(fraction_1.multiply_fractions(fraction_2))
print(fraction_1.divide_fractions(fraction_2))




