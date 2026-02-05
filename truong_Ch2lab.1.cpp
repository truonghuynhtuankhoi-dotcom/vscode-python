#include <iostream>

int main(){
    double flash_drive_price =8.0;
    double profit_rate = 0.35;

    double sell_price= flash_drive_price*(1+profit_rate);

    std::cout<< "To have a 35% profit, the flash drive should sell for $"<<sell_price;
    return 0;


}