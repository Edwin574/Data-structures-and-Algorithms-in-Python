'''
Suppose you want to convert an integer to string in some base between binary and hexadecimal.
    example:
        Convert the integer 10 to its string representation in decimal as '10' or to its binary representation
        as '1010'.
        Bases can be 2(binary),8(octal),10(decimal),16(hexadecimal)

--> This problem can be solved using a stack but since we are learning recursion, it will be quite elegant for the job.

TODO
    -Reduce the original given number to a series of single digit numbers.
    -Convert the single digit number to a string using a lookup.
    -Concatenate the single digit strings together to form the final result.
    
    *Our base case will be after reducing the number, the digit(s) should be less than the base
'''

#code

def to_str(the_number,base):
    convert_to_string="0123456789ABCDEF"
    if the_number<base:
        return convert_to_string[the_number]
    else:
        return to_str(the_number/base)+convert_to_string[the_number%base]
