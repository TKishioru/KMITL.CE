#include <Servo.h>
Servo myservo; //ประกาศตัวแปรแทน Servo

String data;

void setup() {
  Serial.begin(9600);
  myservo.attach(9); // กำหนดขา 9 ควบคุม Servo
}

void loop() {
  for (int degree =  0; degree <= 360; degree++)
  {
    myservo.write(degree);
    delay(10);
  }
  for (int degree =  360; degree >= 0; degree--)
  {
    myservo.write(degree);
    delay(10);
  }
}
