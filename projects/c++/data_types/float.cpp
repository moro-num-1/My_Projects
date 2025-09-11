#include <iostream>
#include <iomanip>
int main() {
    //Size of float is 4 bytes;
    //Size of double is 8 bytes;
    //Size of long double is 16 bytes;
    float flt = {1.0f};
    double dbl {1.0};
    long double lng {1.0l};
    
    /*double nan {0.0 / 0};
    double inf1 {1.0 / 0};
    double inf2 {1.0 / 0};*/
    std::cout << "The number is: " << -1 / (dbl / 0) << std::endl;
    std::cout << "Size of the number is: " << sizeof(dbl) << std::endl;
    return 0;
}