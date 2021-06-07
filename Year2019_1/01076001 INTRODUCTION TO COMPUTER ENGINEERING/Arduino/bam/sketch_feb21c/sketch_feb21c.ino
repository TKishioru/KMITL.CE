#include <Servo.h>
Servo myservo; //ประกาศตัวแปรแทน Servo

void setup() {
  myservo.attach(9); // กำหนดขา 9 ควบคุม Servo
}

void loop() {
  for(int degree =  0;degree <= 180;degree += 15)
  {
    myservo.write(degree); // สั่งให้ Servo หมุนไปองศาที่ 0
  delay(200);
  }
  for(int degree =  180;degree >= 0;degree -= 15)
  {
    myservo.write(degree); // สั่งให้ Servo หมุนไปองศาที่ 0
  delay(200);
  }
  
  /*
  myservo.write(0); // สั่งให้ Servo หมุนไปองศาที่ 0
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(15); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(30); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(45); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(60); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(75); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(90); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(105); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(120); // สั่งให้ Servo หมุนไปองศาที่ 0
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(135); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(150); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(165); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(180); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(165); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(150); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(135); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(120); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(105); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(90); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(75); // สั่งให้ Servo หมุนไปองศาที่ 0
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(60); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(45); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(30); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(15); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(200); // หน่วงเวลา 1000ms
  myservo.write(0); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(200); // หน่วงเวลา 1000ms
  */
  /*
  myservo.write(0); // สั่งให้ Servo หมุนไปองศาที่ 0
  delay(500); // หน่วงเวลา 1000ms
  myservo.write(45); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(500); // หน่วงเวลา 1000ms
  myservo.write(90); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(500); // หน่วงเวลา 1000ms
  myservo.write(135); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(500); // หน่วงเวลา 1000ms
  myservo.write(180); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(500); // หน่วงเวลา 1000ms
    myservo.write(135); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(500); // หน่วงเวลา 1000ms
    myservo.write(90); // สั่งให้ Servo หมุนไปองศาที่ 90
  delay(500); // หน่วงเวลา 1000ms
    myservo.write(45); // สั่งให้ Servo หมุนไปองศาที่ 45
  delay(500); // หน่วงเวลา 1000ms*/
}
