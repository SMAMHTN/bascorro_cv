int x, y;
void setup() {
  Serial.begin(9600);
}

void loop()
{
  while (Serial.available()){
      x = Serial.read();
      Serial.print('x');
      Serial.println(x);
  }
 } 
