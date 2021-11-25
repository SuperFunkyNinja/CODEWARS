"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
Symbol	Value
I	1
IV	4
V	5
X	10
L	50
C	100
D	500
M	1000
"""


class RomanNumerals:
    def to_roman(val):
        return ""

    def from_roman(roman_num):
        return 0


print(RomanNumerals.to_roman(1000))  # 'M', '1000 should == "M"')
print(RomanNumerals.to_roman(4))  # 'IV', '4 should == "IV"')
print(RomanNumerals.to_roman(1))  # 'I', '1 should == "I"')
print(RomanNumerals.to_roman(1990))  # 'MCMXC', '1990 should == "MCMXC"')
print(RomanNumerals.to_roman(2008))  # 'MMVIII', '2008 should == "MMVIII"')

print(RomanNumerals.from_roman("XXI"))  # 21, 'XXI should == 21')
print(RomanNumerals.from_roman("I"))  # 1, 'I should == 1')
print(RomanNumerals.from_roman("IV"))  # 4, 'IV should == 4')
print(RomanNumerals.from_roman("MMVIII"))  # 2008, 'MMVIII should == 2008')
print(RomanNumerals.from_roman("MDCLXVI"))  # 1666, 'MDCLXVI should == 1666')

"""
@test.describe('sample_tests')
def sample_tests():
    @test.it('to roman')
    def sample_tests_to():
        test.assert_equals(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
        test.assert_equals(RomanNumerals.to_roman(4), 'IV', '4 should == "IV"')
        test.assert_equals(RomanNumerals.to_roman(1), 'I', '1 should == "I"')
        test.assert_equals(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
        test.assert_equals(RomanNumerals.to_roman(2008), 'MMVIII', '2008 should == "MMVIII"')
    @test.it('from roman')
    def sample_tests_from():
        test.assert_equals(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
        test.assert_equals(RomanNumerals.from_roman('I'), 1, 'I should == 1')
        test.assert_equals(RomanNumerals.from_roman('IV'), 4, 'IV should == 4')
        test.assert_equals(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
        test.assert_equals(RomanNumerals.from_roman('MDCLXVI'), 1666, 'MDCLXVI should == 1666')
"""
