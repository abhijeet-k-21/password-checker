import re
 
def check_strength(password):
     length_error = len(password) < 8
     digit_error = re.search(r"\d", password) is None
     uppercase_error = re.search(r"[A-Z]", password) is None
     lowercase_error = re.search(r"[a-z]", password) is None
     symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
 
     errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
     score = 5 - sum(errors)
 
     if score == 5:
         return "Strong"
     elif score >= 3:
         return "Medium"
     else:
         return "Weak"
 
 
if __name__ == "__main__":
     password = input("Enter your password: ")
     strength = check_strength(password)
     print(f"Password strength: {strength}")
