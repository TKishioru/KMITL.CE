int Led=13;//define LED interface
int buttonpin=3 //Define D0 Sensor Interface
int val;//define numeric variables val
void setup()
{
pinMode(Led,OUTPUT);// Define LED as output interface
pinMode(buttonpin,INPUT);//Define D0 Sensor as output Interface
}
void loop()
{
val=digitalRead(buttonpin);//digital interface will be assigned a value of 3 to read val
if(val==HIGH)//When the light sensor detects a signal is interrupted, LED flashes
{
digitalWrite(Led,HIGH)
}
else
{
digitalWrite(Led,LOW)
}
}
/*
ตัวอย่างการใช้งานแบบ Analog Output:
int sensorPin = A5; // select the input pin for the potentiometer
int ledPin = 13; // select the pin for the LED
int sensorValue = 0; // variable to store the value coming from the sensor

void setup() {
pinMode(ledPin, OUTPUT);
Serial.begin(9600);
}

void loop() {

sensorValue = analogRead(sensorPin);
digitalWrite(ledPin, HIGH);
delay(sensorValue);
digitalWrite(ledPin, LOW);
delay(sensorValue);
Serial.println(sensorValue, DEC);
}*/
