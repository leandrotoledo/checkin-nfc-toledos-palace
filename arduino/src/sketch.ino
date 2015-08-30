#include "../lib/SPI.h"
#include "PN532_SPI.h"
#include "PN532.h"
#include "NfcAdapter.h"
 
PN532_SPI interface(SPI, 10);
NfcAdapter nfc = NfcAdapter(interface);
 
void setup(void) {
    Serial.begin(9600);
    nfc.begin();
}
 
void loop(void) {

    if (nfc.tagPresent())
    {
        NfcTag tag = nfc.read();
        Serial.println(tag.getUidString());
    }
    delay(500);
}
