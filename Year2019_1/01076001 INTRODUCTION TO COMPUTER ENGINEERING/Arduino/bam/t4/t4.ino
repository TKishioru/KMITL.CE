int s1 = 6;
int s2 = 7;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int a = digitalRead(s1);
  int b = digitalRead(s2);
  Serial.print(a);
  Serial.print("");
  Serial.print(b);
  Serial.print("");
  if (a == 0 && b == 0) {
    Serial.println("A");
  } else if (a == 1 && b == 0) {
    Serial.println("B");
  } else if (a == 1 && b == 1) {
    Serial.println("C");
  } else if (a == 0 && b == 1) {
    Serial.println("D");
  }
  delay(200);
}
