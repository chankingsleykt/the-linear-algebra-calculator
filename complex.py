import math

class Complex:


    def __init__(self, *args):
        if len(args) == 2:
            self.real = args[0]
            self.imaginary = args[1]
        elif len(args) == 1:
            if args[0].find('+') != -1:
                self.real = int(args[0][:args[0].find('+')].strip())
                self.imaginary = int(args[0][args[0].find('+')+1:args[0].find('i')].strip())
            else:
                self.real = int(args[0][:args[0].find('-')].strip())
                self.imaginary = int(args[0][args[0].find('-')+1:args[0].find('i')].strip())*-1


    def __str__(self):
        result = '' + str(self.real)
        if self.imaginary < 0:
            result += ' - ' + str(self.imaginary)[1:] + 'i'
        else:
            result += ' + ' + str(self.imaginary) + 'i'
        return result


    def __eq__(self, value):
        return self.real == value.real and self.imaginary == value.imaginary


    def __add__(self, value):
        if type(value) == Complex:
            return Complex(self.real + value.real, self.imaginary + value.imaginary)
        elif type(value) == float:
            return Complex(self.real + value, self.imaginary)
        elif type(value) == int:
            return Complex(self.real + value, self.imaginary)
        else:
            raise Exception("Cannot add!")


    def __sub__(self, value):
        if type(value) == Complex:
            return Complex(self.real - value.real, self.imaginary - value.imaginary)
        elif type(value) == float:
            return Complex(self.real - value, self.imaginary)
        elif type(value) == int:
            return Complex(self.real - value, self.imaginary)
        else:
            raise Exception("Cannot subtract!")


    def __mul__(self, value):
        if type(value) == Complex:
            real = (self.real * value.real) - (self.imaginary * value.imaginary)
            imaginary = (self.real * value.imaginary) + (value.real * self.imaginary)
            return Complex(real, imaginary)
        elif type(value) == float:
            return Complex(self.real * value, self.imaginary * value)
        elif type(value) == int:
            return Complex(self.real * value, self.imaginary * value)
        else:
            raise Exception("Cannot multiply!")


    def __truediv__(self, value):
        if type(value) == Complex:
            numerator = self*value.conjugate()
            denominator = value*value.conjugate()
            return Complex(numerator.real/denominator.real, numerator.imaginary/denominator.real)
        elif type(value) == float:
            return Complex(self.real / value, self.imaginary / value)
        elif type(value) == int:
            return Complex(self.real / value, self.imaginary / value)
        else:
            raise Exception("Cannot divide!")


    def conjugate(self):
        return Complex(self.real, -self.imaginary)


    def modulus(self):
        return math.sqrt(math.pow(self.real, 2) + math.pow(self.imaginary, 2))