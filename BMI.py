import tkinter

window = tkinter.Tk()
window.title("BMI Calculate")
window.minsize(width=300, height=300)
window.configure(bg="#F2ECE4")


def calculate_bmi():
    a = entry_w.get()
    b = entry_h.get()

    if a == "" or b == "":
        result.config(text="Please enter your weight and height.")
    else:
        try:
            bmi = round(float(a) / (float(b) / 100) ** 2, 2)

            if 0 < bmi <= 19:
                result.config(text=f"Your BMI is {bmi}.You are Under Weight.")
            elif 19 < bmi <= 25:
                result.config(text=f"Your BMI is {bmi}.You are Normal Weight.")
            elif 25 < bmi <= 30:
                result.config(text=f"Your BMI is {bmi}.You are Over Weight.")
            elif 30 < bmi <= 35:
                result.config(text=f"Your BMI is {bmi}.You are Obesity(Class I).")
            elif 35 < bmi <= 40:
                result.config(text=f"Your BMI is {bmi}.You are Obesity(Class II.")
            elif bmi > 40:
                result.config(text=f"Your BMI is {bmi}.You are Extreme Obesity.")
            else:
                result.config("Enter a valid number")
        except:
            result.config(text=" Please enter a valid number.!!!")


#Label1
label_w = tkinter.Label(text="Enter Your Weight(kg)", bg="#F2ECE4", font=("Arial Rounded MT Bold", 8))
label_w.place(x=85, y=25)

entry_w = tkinter.Entry(width=10)
entry_w.place(x=115, y=50)
entry_w.focus()

#label2
label_h = tkinter.Label(text="Enter Your Height(cm)", bg="#F2ECE4", font=("Arial Rounded MT Bold", 8))
label_h.place(x=85, y=75)

entry_h = tkinter.Entry(width=10)
entry_h.place(x=115, y=100)

#button
button = tkinter.Button(window, text="Calculate", bg="#D9C2A7", borderwidth=4, relief="raised",
                        activebackground="#594A3C", command=calculate_bmi)
button.place(x=115, y=135)

result = tkinter.Label(bg="#F2ECE4", font=("Arial", 8))
result.place(x=70, y=195)

window.mainloop()
