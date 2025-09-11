#include <iostream>

int main() {
    char f_ltr {'M'};
    char s_ltr {'O'};
    char t_ltr {'R'};
    char fo_ltr {'O'};
    std::cout << static_cast<int>(f_ltr) << std::endl;
    std::cout << static_cast<int>(s_ltr) << std::endl;
    std::cout << static_cast<int>(t_ltr) << std::endl;
    std::cout << static_cast<int>(fo_ltr) << std::endl;
    std::cout << "Size of char is: " << sizeof(char) << std::endl;
    return 0;
}