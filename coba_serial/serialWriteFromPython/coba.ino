int x, y;
void setup() {
  Serial.begin(9600);
}

void loop()
{
  while (Serial.available())
  {
    if (Serial.parseInt() == 777) {
      x = Serial.parseInt();
      Serial.print('x');
      Serial.println(x);
    }
    if (Serial.parseInt() == 666) {
      y = Serial.parseInt();
      Serial.print('y');
      Serial.println(y);
    }
  }
}
