int data;

void setup(){
    Serial.begin(115200);
}

void loop(){
    Serial.write("666");
    delay(2000);
}
