def reverse_string(s):
    reversed_str = ""
    for i in range(len(s)):
        reversed_str += s[i-1] 
    return reversed_str

print(reverse_string("hello"))
