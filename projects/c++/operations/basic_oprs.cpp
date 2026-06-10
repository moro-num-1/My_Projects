#include <iostream>

int main() {
    int num1 {3};
    int num2 {8};
    int result;
    //Addition;
    result = num1 + num2;
    std::cout << "Result: " << result << std::endl;
    //Substraction;
    result = num2 - num1;
    std::cout << "Result: " << result << std::endl;
    //Multiplication;
    result = num1 * num2;
    std::cout << "Result: " << result << std::endl;
    //Division;
    result = num2 / num1;
    std::cout << "Result: " << result << std::endl;
    //Modulus;
    result = num2 % num1;
    std::cout << "Result: " << result << std::endl;
}
