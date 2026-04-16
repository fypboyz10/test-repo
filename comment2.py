text = input("Enter a string: ")  
reversed_text = ""  

index = len(text) - 1 
while index >= 0:  
    reversed_text += text[index]  
    index -= 1  

print("Reversed string:", reversed_text)  

if text == reversed_text:  
    print("It is a palindrome")  
else:
    print("Not a palindrome")  
