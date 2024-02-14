import tkinter as tk

def isbn13(input):
    input = [int(x) for x in input]

    if len(input) == 13:
        odd = 0
        even = 0
        for i in range(1, 13, 2):  # for even
            even += input[i] * 3
        for j in range(0, 12, 2):  # for odd
            odd += input[j]

        x = (odd + even) % 10

        if (10 - x) == input[-1]:
            return "The ISBN 13 is Valid!"
        else:
            return "The ISBN 13 is Not Valid!"
def isbn10(input):
    input_list = [x for x in input]
    
    # check for length 
    if len(input_list) != 10: 
        return "Not A Valid ISBN Number!"

    # Computing weighted sum  
    # of first 9 digits 
    _sum = 0
    for i in range(9): 
        if '0' <= input_list[i] <= '9': 
            _sum += int(input_list[i]) * (10 - i) 
        else: 
            return "Invalid Input"

    # Checking last digit 
    if input_list[9] != 'X' and not ('0' <= input_list[9] <= '9'):
       return "Invalid Input"
    # If the last digit is 'X', add  
    # 10 to sum; else, add its value. 
    _sum += 10 if input_list[9] == 'X' else int(input_list[9]) 

    # Check if the weighted sum of  
    # digits is divisible by 11 
    if _sum % 11 == 0:
        return "Valid ISBN 10 Number"
    else:
        return "Not a Valid ISBN 10 Number"

    
def upc(input):
    input = [int(x) for x in input]

    if len(input) == 12:
        odd = 0
        even = 0
        for i in range(0, 12, 2):
            odd += input[i] * 3
        for j in range(1, 12, 2):
            even += input[j]
        total = (even + odd) % 10
        if total == 0:
            return "The UPC is Valid!"
        else:
            return "The UPC is Not Valid!"
            
    elif len(input) == 0:
        return "valid"

    else:
        return "Not A Valid UPC Code!"

def card(input):
    input = input[::-1]
    input = [int(x) for x in input]

    if len(input) == 16:
        odd = 0
        even = 0
        for i in range(0, 16, 2):  # for odd
            odd += input[i]
        for j in range(1, 16, 2):  # for even
            x = input[j] * 2
            if x > 9:
                x = sum(int(d) for d in str(x))
            even += x
        # Addition of even and odd places!
        x = (odd + even) % 10
        if x == 0:
            return "The Card is Valid!"
        else:
            return "The Card is Not Valid Card!"

    elif len(input) == 0:
        return "Empty!"

    else:
        return "Not A Valid Card Number!"

def validate():
    choice = int(var.get())
    input = entry.get()
    if choice == 1:
        result_label.config(text=card(input))
    elif choice == 2:
        result_label.config(text=upc(input))
    elif choice == 3:
        result_label.config(text=isbn13(input))
    elif choice == 4:
        result_label.config(text=isbn10(input))

root = tk.Tk()

root.geometry("400x400")
root.title("Validation")

var = tk.IntVar()
var.set(1)
card_rb = tk.Radiobutton( root,text="Card Validation", variable=var, value=1,font=("Arial", 15))
card_rb.pack()

upc_rb = tk.Radiobutton(root, text="UPC Validation", variable=var, value=2,font=("Arial", 15))
upc_rb.pack()

isbn13_rb = tk.Radiobutton(root, text="ISBN-13 Validation", variable=var, value=3,font=("Arial", 15))
isbn13_rb.pack()

isbn10_rb = tk.Radiobutton(root, text="ISBN-10 Validation", variable=var, value=4,font=("Arial", 15))
isbn10_rb.pack()

entry = tk.Entry(root, font=("Arial", 18))
entry.pack(pady=10)

validate_button = tk.Button(root, text="Validate", command=validate,bg="yellow", fg="black", borderwidth=2,font=("Arial", 15), relief="groove")
validate_button.pack()  

result_label = tk.Label(root, font=("Arial", 18))
result_label.pack()

root.mainloop()