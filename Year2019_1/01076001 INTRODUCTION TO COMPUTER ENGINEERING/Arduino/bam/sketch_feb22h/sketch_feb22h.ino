#include <Servo.h>
Servo myservo1; //ประกาศตัวแปรแทน Servo
Servo myservo2;

void setup() {
  Serial.begin(9600);
  myservo1.attach(8);
  myservo2.attach(10); // กำหนดขา 9 ควบคุม Servo

}

void loop() {
  /*myservo.write(0);
    delay();
    myservo.write(360);
    delay(3000);
    }*/

  for (int i =  0; i <= 360; i++)
  {
    myservo1.write(i); // สั่งให้ Servo หมุนไปองศาที่ 0
    delay(1);
  }

  for (int j =  0; j <= 360; j++)
  {
    myservo1.write(j); // สั่งให้ Servo หมุนไปองศาที่ 0
    delay(1);
  }

  for (int i = 360; i >= 0; i--)
  {
    myservo1.write(i); // สั่งให้ Servo หมุนไปองศาที่ 0
    delay(1);
  }
}
for (int j = 360; j >= 0; j--)
{
  myservo1.write(j); // สั่งให้ Servo หมุนไปองศาที่ 0
  delay(1);
}
}

/*
  void song ()
  {
  //เพลง
  }
*/
