#include <iostream>

int main() {
    //short unsigned int can store 2 bytes and positive numbers 0~(2^16) -1;
    short unsigned int num1 = 0;
    short unsigned int num2 = 65535;
    //short signed int can store 2 bytes and positive or negative numbers (-2^15)~(2^15);
    short signed int num3 = -32768;
    short signed int num4 = 32767;
    //unsigned int can store 4 bytes and positive numbers 0~(2^32) -1;
    unsigned int num5 = 0;
    unsigned int num6 = 4294967295;
    //signed int can store 4 bytes and positive or negative numbers (-2^31)~(2^31);
    signed int num7 = -2147483648;
    signed int num8 = 2147483647;
    //long unsigned int store 8 bytes and positive numbers 0~(2^64) -1;
    long unsigned int num9 = 0;
    long unsigned int num10 = 18446744073709551615;
    //long signed int store 8 bytes and positive or negative numbers (-2^63)~(2^63);
    long signed int num11 = -9223372036854775808;
    long signed int num12 = 9223372036854775807;

    std::cout << sizeof(num12) << std::endl;
    return 0;
}