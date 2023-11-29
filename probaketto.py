# import module
import streamlit as st
 
# Title
st.title("Hello GeeksForGeeks !!!")


import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def main():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")

    operation = st.radio("Select operation", ("Addition", "Subtraction", "Multiplication", "Division"))

    result = 0

    if st.button("Calculate"):
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)

    st.write(f"Result: {result}")

if __name__ == "__main__":
    main()
