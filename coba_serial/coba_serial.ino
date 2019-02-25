int data;
int led = 13;

void setup()
{
    Serial.begin(115200);
    Serial.println(F("Serial test"));
    pinMode(led, OUTPUT);   
}


void loop()
{
    while (Serial.available())
    {
      data = Serial.read();
    }
    if (data == '1')
    digitalWrite (led, HIGH);
        
    else if (data == '0')
    digitalWrite (led, LOW);
    
}
