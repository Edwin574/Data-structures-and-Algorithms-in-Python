from Fraction import Fraction

fraction1 = Fraction(3, 5)
print(fraction1)

fraction2 = Fraction(4, 7)
print(fraction2)

add = fraction1 + fraction2
print(f'addition:{add}')

sub = fraction1 - fraction2
print(f'subtraction:{sub}')

print(f'Are the two fractions equal ?:{fraction1 == fraction2}')
mult = fraction1 * fraction2
print(f'multiplication:{mult}')
