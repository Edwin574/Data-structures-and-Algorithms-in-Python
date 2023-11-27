from Deques import Deque

def palindrome_checker(a_sting):
    '''
    This function takes a string and checks whether it is a palindrome by using a Deque data structure
    '''
    char_deque=Deque()
    for character in a_sting:
        char_deque.add_front(character)
        still_equal=True
    while char_deque.size()>1 and still_equal:
        first=char_deque.remove_front()
        last=char_deque.remove_rear()

        if first != last:
            still_equal=False
    return still_equal
    
    
print(palindrome_checker("effrrvfrvyu"))
print(palindrome_checker('radar'))
print(palindrome_checker('madam'))