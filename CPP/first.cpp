// 
// There 1 one error in this file
// 

#include <iostream>

int main() {
    int x = 10;
    std::cout << "Value of x: " << x << std::endl;
    std::cout << "Double x: " << doubleX(x) << std::endl;
    return 0;
}

int doubleX(int num) {
    return num * 2;
}
