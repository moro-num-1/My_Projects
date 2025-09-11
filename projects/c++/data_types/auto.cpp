#include <iostream>

int main() {
    //Auto variables;
    auto name {"MORO"};
    auto fl {'M'};
    auto age {16};
    auto num1 {2.5};
    auto num2 {2.5f};
    auto num3 {2.5l};
    auto num4 {2ul};
    auto num5 {2lu};
    //Print variables;
    std::cout << name << std::endl;
    std::cout << fl << std::endl;
    std::cout << age << std::endl;
    std::cout << num1 << std::endl;
    std::cout << num2 << std::endl;
    std::cout << num3 << std::endl;
    std::cout << num4 << std::endl;
    std::cout << num5 << std::endl;
    //Print variable sizes;
    std::cout << sizeof(name) << std::endl;
    std::cout << sizeof(fl) << std::endl;
    std::cout << sizeof(age) << std::endl;
    std::cout << sizeof(num1) << std::endl;
    std::cout << sizeof(num2) << std::endl;
    std::cout << sizeof(num3) << std::endl;
    std::cout << sizeof(num4) << std::endl;
    std::cout << sizeof(num5) << std::endl;

    //End code;
    return 0;
}