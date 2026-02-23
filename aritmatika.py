# mengimport modul math untuk operasi matematika lanjutan seperti akar kuadrat
import math

# =============
# OPERATOR DASAR
# =============

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: pembagian dengan nol tidak diperbolehkan")
    return a / b

def power(a, b):
    return a**b

def modulo(a, b):
    if b == 0:
        return "Error: pembagian dengan nol tidak diperbolehkan"
    else:
        return a % b

def square_root(a):
    if a < 0:
        return "Error: tidak dapat menghitung akar kuadrat dari bilangan negatif"
    else:
        return math.sqrt(a)

# =============
# OPERASI ILMIAH
# =============

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def log_base10(x):
    if x <= 0:
        raise ValueError("Log is only defined for numbers > 0.")
    return math.log10(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Natural log is only defined for numbers > 0.")
    return math.log(x)

# =============
# OPERASI BERANTAI
# =============

def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception:
        return "Invalid expression."

# =============
# MENU UTAMA ARITMATIKA
# =============

def menu_aritmatika():
    print("=== KALKULATOR ARITMATIKA3 ===")
    print("1. operasi dasar")
    print("2. operasi ilmiah")
    print("3. ekspresi berantai")

    # ambil input user
    input_menu = input("menu pilihan: ")

        # =============
        # OPERASI DASAR
        # =============

    # memvalidasi input user
    if input_menu == "1":
        try:
            a = float(input("masukkan angka pertama: "))
            operator = input("masukkan operator (+, -, *, /, ^, %, √): ")

            if operator == "√":
                result = square_root(a)
            else:
                b = float(input("masukkan angka kedua:"))
                if operator == "+":
                    result = add(a, b)
                elif operator == "-":
                    result = subtract(a, b)
                elif operator == "*":
                    result = multiply(a, b)
                elif operator == "/":
                    result = divide(a, b)
                elif operator == "^":
                    result = power(a, b)
                elif operator == "%":
                    result = modulo(a, b)
                else:
                    print("operator tidak valid")
                    return
            print(f"hasil: {result:g}")
        except ValueError:
            print("input tidak valid")

        # =============
        # OPERASI ILMIAH
        # =============

    elif input_menu == "2":
        try:
            print("1. sin") 
            print("2. cos")  
            print("3. tan")   
            print("4. log")
            print("5. ln")
                
            scientific_choice = input("Pilih operasi ilmiah (1-5): ")
            number = float(input("Masukkan angka: "))
                
            if scientific_choice == "1":
                result = sine(number)
            elif scientific_choice == "2":
                result = cosine(number)
            elif scientific_choice == "3":
                result = tangent(number)
            elif scientific_choice == "4":
                result = log_base10(number)
            elif scientific_choice == "5":
                result = natural_log(number)
            else:
                print("Pilihan tidak valid.")
                return

            print("Hasil:", result)
        except Exception as error:
            print("Error:", error)
            
            
        # =============
        # OPERASI BERANTAI
        # =============
        
    elif input_menu == "3":
        expression = input("masukkan input bruntun anda: ")
        result = evaluate_expression(expression)
        print(f"hasil: {result}")
        
    else:
        print("pilihan menu tidak valid")

if __name__ == "__main__":
    menu_aritmatika()