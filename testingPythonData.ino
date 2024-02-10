#include <Servo.h>
Servo myServo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(4,OUTPUT);
  digitalWrite(4,LOW);
  myServo.attach(2);
  myServo.write(0);  
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    int commaIndex = data.indexOf(',');
    if (commaIndex != - 1) {
      int angle = data.substring(0,commaIndex).toInt();
      angle = constrain(angle,0,180);
      myServo.write(angle);
      digitalWrite(4,HIGH);
    }
    //Serial.println(val);
  }
  delay(10);
}
