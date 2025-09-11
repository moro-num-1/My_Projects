#include <iostream>

int main() {
    std::cout << std::boolalpha;
    bool single = 0;
    if (single == 1) {
        std::cout << "You need to have a girl right now!!" << std::endl;
    }
    else {
        std::cout << "You're lucky to have a girl" << std::endl;
    }
    std::cout << single << std::endl;
    return 0;
}