#define pressedUp LOW
#define pressedLow HIGH
#define btnRed 12
#define btnYellow 11
#define btnGreen 10
#define redLED 4
#define yellowLED 3
#define greenLED 2

unsigned long redtime,yellowtime,greentime;
int ReadSwitchRed, ReadSwitchYellow, ReadSwitchGreen;
void setup() 
{
  Serial.begin(9600);
  pinMode(btnRed,INPUT_PULLUP);
  pinMode(btnYellow,INPUT_PULLUP);
  pinMode(btnGreen,INPUT_PULLUP);
  pinMode(redLED,OUTPUT);
  pinMode(yellowLED,OUTPUT);
  pinMode(greenLED,OUTPUT);
}

void loop() 
{
  redtime = 0;yellowtime = 0;greentime = 0;
  ReadSwitchRed = digitalRead(btnRed);
  ReadSwitchYellow = digitalRead(btnYellow);
  ReadSwitchGreen = digitalRead(btnGreen);
  if(ReadSwitchRed == pressedLow && millis() - redtime >= 3000)
  {      
    digitalWrite(redLED,HIGH);
  } 
  else 
  {
    digitalWrite(redLED,LOW);
  }
  if(ReadSwitchYellow == pressedUp)
  {      
      digitalWrite(yellowLED,HIGH);
  } 
  else 
  {
    digitalWrite(yellowLED,LOW);
  }
  if(ReadSwitchGreen == pressedUp && millis() - greentime >= 3000)
  {      
    digitalWrite(greenLED,HIGH);
  }
  else 
  {
    digitalWrite(greenLED,LOW);
  }

  if(millis() - yellowtime >= 500)
  {
    digitalWrite(yellowLED,LOW);
  }
  if(millis() - yellowtime >= 1000)
  {
    digitalWrite(yellowLED,HIGH);
  }
  if(millis() - yellowtime >= 1500)
  {
    digitalWrite(yellowLED,LOW);
  }
}
