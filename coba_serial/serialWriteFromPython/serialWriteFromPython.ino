int r = 1;
int led = 13;
void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);  
  digitalWrite(led, HIGH);
  
}

void loop()
{
  while(Serial.available())
  {
    r = Serial.read();
    Serial.print(r);
  }
  r = int(r);
  if (r > 100)
    digitalWrite(led, HIGH);
  else if (r == 'B') 
    digitalWrite(led, LOW);  
}
