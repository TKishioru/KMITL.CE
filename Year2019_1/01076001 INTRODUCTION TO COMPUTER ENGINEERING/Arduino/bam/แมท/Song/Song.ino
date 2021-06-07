//เสียงเตือน
int speakerPin = 9;
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
  for (int i = 0; i < 17; i++)
    if (names[i] == note) {
      int newduration = duration / SPEE;
      playTone(tones[i], newduration);
    }
}


int sensorPin = A0;
int sensorValue = 0;
int song = 2;
int SOUT = 11;
int PLAYE = 9;
int s1 = A0;
int s2 = A1;
int aX;
int bY;
int sensorxOrigin;
int sensoryOrigin;
void setup()
{
  pinMode (sensorValue, INPUT);
  pinMode (song, OUTPUT);
  pinMode (SOUT, INPUT);
  Serial.begin(9600);
  s_serial.begin(9600);
  aX = analogRead(s1);
  bY = analogRead(s2);
  pinMode(speakerPin, OUTPUT);
}

void loop()
{
  int a = analogRead(s1);
  int b = analogRead(s2);
  Serial.print("Sensorx = ");
  Serial.print(a);
  delay(500);
  Serial.print("      ");
  Serial.print("Sensory = ");
  Serial.println(b);
  delay(500);
  sensorxOrigin = aX;
  sensoryOrigin = bY;

  if ((sensorxOrigin - a >= 30) || (sensoryOrigin - b >= 30) || (sensorxOrigin - a <= -30) || (sensoryOrigin - b <= -30))
  {
    for (int i = 0; i < length; i++) {
      if (notes[i] == ' ') {
        delay(100);
        //delay(beats[i] * tempo); // rest
      } else {
        playNote(notes[i], beats[i] * tempo);
      }
      // pause between notes
      delay(tempo);
    }
    aX = a;
    bY = b;
  }
}
