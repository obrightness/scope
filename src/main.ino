
int readPin = A2;
void setup() {
    Serial.begin(9600);
    pinMode(A0, INPUT);
    Serial.println(100);
}

int readValue = 0;
void loop()
{
    //Serial.println("Hi again");
    readValue = analogRead(readPin);
    Serial.println(readValue);
}

