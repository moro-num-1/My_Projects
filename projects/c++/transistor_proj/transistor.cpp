#include <iostream>

/*    ================
    || AND Truth Table ||
      ================
    1-false & false = off;
    2-true & false = off;
    3-false & true = off;
    4-true & true = on;
*/
             
/*    ================
    ||NAND Truth Table||
      ================
    1-false & false = on;
    2-true & false = on;
    3-false & true = on;
    4-true & true = off;
*/

/*    ================  
    || OR Truth Table ||
      ================
    1-false & false = off;
    2-true & false = on;
    3-false & true = on;
    4-true & true = on;
*/

int main() {   
    std::cout << std::boolalpha;
    bool switch_a = true;
    bool switch_b = true;
    bool and_state = switch_a & switch_b;
    bool nand_state = !and_state;
    bool or_state = !(!switch_a & !switch_b);
    if (or_state) {std::cout << "ON" << std::endl;}
    else {std::cout << "OFF" << std::endl;}
    return 0;
}