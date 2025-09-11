//Runtime error;
#include <iostream>
int main() {
    std::cout << "Runtime error" << std::endl;
    int value = 1/0;
    std::cout << "The value is: " << value;
    return 0;
}