#include <EEPROM.h>

void setup() {
  // put your setup code here, to run once:
    Serial.begin(115200);
    int address;
    unsigned int value;
    for (address=0; address<EEPROM.length(); address++)
    {
        value = EEPROM.read(address);
        Serial.print(value, BIN);
        Serial.print("\t");
        if ((address+1)%8 == 0)
            Serial.println("");
    }
}

void loop() {
  // put your main code here, to run repeatedly:

}
