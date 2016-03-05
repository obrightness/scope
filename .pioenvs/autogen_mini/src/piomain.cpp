#include <Arduino.h>

void setup();
void loop();
#line 2 "main.ino"
int readPin = A2;
void setup() {
Serial.begin(9600);
pinMode(A0, INPUT);
Serial.println(100);
}

int readValue = 0;
void loop()
{

readValue = analogRead(readPin);
Serial.println(readValue);
}
