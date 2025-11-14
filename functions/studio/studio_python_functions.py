def reverse_characters(x):
    if type(x) == str:  
        return ''.join(list(x)[::-1]) 
    elif type(x) == int:  
        return int(''.join(list(str(x))[::-1]))  
def reverse_list(old_list):
    # a) Define and initialize an empty list
    new_list = []
    
    # b)here we are looping through the old list
    for element in old_list:
    # c) we are reversing each character
        reversed_element = reverse_characters(element)
     # d) then we add the reversed element to the new list
        new_list.append(reversed_element)
    
    # e) Return the final reversed list
    return new_list[::-1]
