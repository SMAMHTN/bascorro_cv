int input = 12;
int x;
void setup() {
  Serial.begin(300);
  pinMode(input, INPUT);
}
void loop() {
  x = digitalRead(input);
  if (x = HIGH){
    Serial.println('1');
    }
  else {
    Serial.println('0');
    }

}
