#include <iostream>

int main() {
    std::cout << "Hello, World" << std::endl;
    std::cout << "Hello, World" << std::endl << std::flush;
    std::cout << "Hello, World" << "\n";
    std::cout << "Hello, World" << "\n" << std::flush;
    return 0;
}