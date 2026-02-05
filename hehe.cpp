#include <iostream>
using namespace std;

int main() {
    double propertyValue, taxRate;
    const double PROPERTY_TAX = 0.60;

    cout << "Enter the actual property value: \a";
    cin >> propertyValue;

    cout << "Enter the tax rate per $100 of assessed value: ";
    cin >> taxRate;

    // Calculate assessed value
    double assessedValue = propertyValue * PROPERTY_TAX;

    // Calculate annual property tax
    double annualTax = (assessedValue / 100) * taxRate;

    cout << "Assessed Value: $" << assessedValue << endl;
    cout << "Annual Property Tax: $" << annualTax << endl;

    return 0;
}
