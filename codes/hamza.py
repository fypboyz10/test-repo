def factorial(n):
    if n == 0:
        return 1
    else:
        n * factorial(n - 1)  

def is_palindrome(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s) - i]: 
            return False
    return True


if __name__ == "__main__":
    print(factorial(5))      
    print(is_palindrome("racecar"))  
