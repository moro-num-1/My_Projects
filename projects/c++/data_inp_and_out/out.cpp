#include <iostream>

int main() {
    //std::out print data from the program to the console;
    std::cout << "Text" << std::endl;
    
    //std::err prints data errors from program to the console;
    std::cout << "Something unexpected happened, check your code" << std::endl;

    //std::clog sends log messages to the output;
    std::cout << "A log message";

    return 0;
}