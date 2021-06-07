#include <Servo.h>
Servo myservo; //ประกาศตัวแปรแทน Servo

int speakerPin = 10;
int length = 28; // the number of notes
char notes[] = "GGAGcB GGAGdc GGxecBA yyecdc";
int beats[] = { 2, 2, 8, 8, 8, 16, 1, 2, 2, 8, 8, 8, 16, 1, 2, 2, 8, 8, 8, 8, 16, 1, 2, 2, 8, 8, 8, 16 };
int tempo = 150;
void playTone(int tone, int duration) {
  for (long i = 0; i < duration * 1000L; i += tone * 2) {
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
  }
}
void playNote(char note, int duration) {
  char names[] = {'C', 'D', 'E', 'F', 'G', 'A', 'B',
                  'c', 'd', 'e', 'f', 'g', 'a', 'b',
                  'x', 'y'
                 };
  int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014,
                  956,  834,  765,  593,  468,  346,  224,
                  655 , 715
                };
  int SPEE = 5;
  // play the tone corresponding to the note name
  for (int i = 0; i < 17; i++) {
    if (names[i] == note) {
      int newduration = duration / SPEE;
      playTone(tones[i], newduration);
    }
  }
}

void setup() {
  myservo.attach(9); // กำหนดขา 9 ควบคุม Servo
  pinMode(speakerPin, OUTPUT);
}

void loop() {myservo.write(0); // สั่งให้ Servo หมุนไปองศาที่ 0
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

  for (int i = 0; i < length; i++) {
    if (notes[i] == ' ') {
      delay(beats[i] * tempo); // rest
    } else {
      playNote(notes[i], beats[i] * tempo);
    }
    // pause between notes
    delay(tempo);
  }
}
