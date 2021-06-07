//เป็นโค้ดที่อาจไม่สามารถรันได้อย่างถูกต้อง เนื่องจากเป็นโค้ดที่ไม่สมบูรณ์ที่เกิดจากแนวคิด PID ในการทำ

int sensorsValue[5]; // do not use 0 index
int lineV = 0;
int groundV = 0;
int meanV = 500;
int N = 5;
int motorSpeed;
int baseSpeed = 100;
int rightSpeed, leftSpeed;
int maxSpeed = 100;
int sum_error = 0;

// PID
int error = 0;
int pre_error = 0;
int Kp = 25;
int Kd = 0;
int Ki = 0;
int enA,enB,in1,in2,in3,in4;  //ตัวแปรเอา Output

bool B(int n)
{
  if (n >= meanV)      return true;
  else                return false;
}

bool W(int n)
{
  if (n < meanV)     return true;
  else              return false;
}

void setup()
{
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  for (int i = 0; i < 5; i++) //อ่านค่าเซนเซอร์
    pinMode(i + 14, INPUT);
}

void loop()

{
  for (int i = 0; i < 5; i++)
  sensorsValue[i] = analogRead(14 + i);
  //เป็นการให้เซ็นเตอร์อ่านค่า หากตรงกับที่กำหนดจะทำตามที่กำหนด โดยที่ค่า error ช่วงลบจะเอียงไปทางด้านขวา,ช่วงบวกจะเอียงไปทางด้านซ้าย และค่า error = 0 จะเป็นการเดินตรงไป
  if ( B(sensorsValue[0]) && B(sensorsValue[1]) && B(sensorsValue[2]) && B(sensorsValue[3]) && W(sensorsValue[4]) )
  {
    error = 4;
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }
  else if ( B(sensorsValue[0]) && B(sensorsValue[1]) && B(sensorsValue[2]) && W(sensorsValue[3]) && W(sensorsValue[4]) )
  {
    error = 3;
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }
  else if ( B(sensorsValue[0]) && B(sensorsValue[1]) && B(sensorsValue[2]) && W(sensorsValue[3]) && B(sensorsValue[4]) )
  {
    error = 2;
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }
  else if ( B(sensorsValue[0]) && B(sensorsValue[1]) && W(sensorsValue[2]) && W(sensorsValue[3]) && B(sensorsValue[4]) )
  {
    error = 1;
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }
  else if ( B(sensorsValue[0]) && B(sensorsValue[1]) && W(sensorsValue[2]) && B(sensorsValue[3]) && B(sensorsValue[4]) )
  {
    error = 0;
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }
  else if ( B(sensorsValue[0]) && W(sensorsValue[1]) && W(sensorsValue[2]) && B(sensorsValue[3]) && B(sensorsValue[4]) )
  {
    error = -1;
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
  }
  else if ( B(sensorsValue[0]) && W(sensorsValue[1]) && B(sensorsValue[2]) && B(sensorsValue[3]) && B(sensorsValue[4]) )
  {
    error = -2;
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
  }
  else if ( W(sensorsValue[0]) && W(sensorsValue[1]) && B(sensorsValue[2]) && B(sensorsValue[3]) && B(sensorsValue[4]) )
  {
    error = -3;
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
  }
  else if ( W(sensorsValue[0]) && B(sensorsValue[1]) && B(sensorsValue[2]) && B(sensorsValue[3]) && B(sensorsValue[4]) )
  {
    error = -4;
  }

  /// check BBBBB

  else if ( B(sensorsValue[0]) && B(sensorsValue[1]) && B(sensorsValue[2]) && B(sensorsValue[3]) && B(sensorsValue[4]) )
  {
    error = pre_error;
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
  }
  //คำนวณความเร็ว
  motorSpeed = Kp * error + Kd * (error - pre_error) + Ki * (sum_error);
  leftSpeed = baseSpeed + motorSpeed;
  rightSpeed = baseSpeed - motorSpeed;
  
  if (leftSpeed > maxSpeed) leftSpeed = maxSpeed;
  if (rightSpeed > maxSpeed) rightSpeed = maxSpeed;
  if (leftSpeed < -maxSpeed) leftSpeed = -maxSpeed;
  if (rightSpeed < -maxSpeed) rightSpeed = -maxSpeed;

  analogWrite(enA, leftSpeed);
  analogWrite(enB, rightSpeed);
  delay(500);

  pre_error = error;
  sum_error += error;

  //lcd("e=%d pe=%d|Ls=%d RS=%d|kp=%d kd=%d", error, pre_error, leftSpeed, rightSpeed , Kp * error, Kd * (error - pre_error) );
  //แสดงผลผ่าน LCD

}
