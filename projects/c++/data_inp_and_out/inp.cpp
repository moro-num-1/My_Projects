#include <iostream>
#include <string>

int main() {
    std::string full_name;
    std::cout << "Enter your name: ";
    std::getline(std::cin, full_name);
    std::cout << "Your name is: " << full_name << std::endl;
}