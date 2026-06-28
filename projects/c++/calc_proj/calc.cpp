#include <iostream>
//Functions;
void take_line() {std::cout << std::endl;}
int add(int num1, int num2) {
    return num1 + num2;
}
int sub(int num1, int num2) {
   return num1 - num2;
}
int mult(int num1, int num2) {
    return num1 * num2;
}
int dvd(int num1, int num2) {
    return num1 / num2;
}
void print_result(int num1, char sign, int num2, int result) {
    std::cout << num1 << " " << sign << " " << num2 << " = " << result;
}

//Code;
int main() {
    //Declaring variables;
    char sign;
    //Take a sign;
    std::cout << "Enter the sign: ";
    std::cin >> sign;
    take_line();
    //Check the sign;
    if (sign != '+' & sign != '-' & sign != '*' & sign != '/') {
        std::cout << sizeof(sign);
        std::cout << "This is an invalid sign! Try again";
        take_line();
    }
    else {
        //Take the numbers;
        int num1;
        int num2;
        double result;
        std::cout << "Enter the first number: ";
        std::cin >> num1;
        take_line();
        std::cout << "Enter the second number: ";
        std::cin >> num2;
        take_line();
        //Operation on numbers;
        if (sign == '+') {
            result = add(num1, num2);
            print_result(num1, sign, num2, result);
        }
        else if (sign == '-') {
            result = sub(num1, num2);
            print_result(num1, sign, num2, result);
        }
        else if (sign == '*') {
            result = mult(num1, num2);
            print_result(num1, sign, num2, result);
        }
        else if (sign == '/') {
            if (num2 == 0) {std::cout << "Division by zero isn't allowed! Try again.";}
            else {result = dvd(num1, num2);
                print_result(num1, sign, num2, result);
            }
        }
        take_line();
    }
    //Code End;
    return 0;
}
