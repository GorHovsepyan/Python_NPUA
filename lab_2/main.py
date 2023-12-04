class Fraction:
    def init(self,Up,Down):
        self.up=Up
        self.down = Down
    def sum(fraction1,fraction2):
        return Fraction(fraction1.up * fraction2.down + fraction2.up * fraction1.down,fraction1.down * fraction2.down)
    def dif(fraction1,fraction2):
        return Fraction(fraction1.up * fraction2.down - fraction2.up * fraction1.down,fraction1.down * fraction2.down)
    def mul(fraction1,fraction2):
        return Fraction(fraction1.up * fraction2.up,fraction1.down * fraction2.down)
    def sub(fraction1,fraction2):
        return Fraction(fraction1.up * fraction2.down,fraction1.down * fraction2.up)
a=Fraction(1,2)
b=Fraction(1,2)
print(a.sum(a,b))