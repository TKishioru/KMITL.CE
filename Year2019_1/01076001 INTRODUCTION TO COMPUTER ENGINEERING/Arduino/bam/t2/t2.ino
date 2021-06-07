/*
  VCC to arduino pin 5v
  GND to arduino pin GND
  SCL to arduino pin A5 (or the SCL pin for your arduino)
  SDA to arduino pin A4 (or the SDA pin for your arduino)
*/


#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

#define OLED_RESET     4
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

int sensorPin = A0;     //Sensor soil

void setup() {
  Serial.begin(9600);
 pinMode(7, OUTPUT); //Light

  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);

  display.display();
  delay(2000);
  display.clearDisplay();

  Serial.begin(9600);
  delay(500); // wait for display to boot up
}

void loop() {
  // Clear the buffer
  display.clearDisplay();

  display.setTextSize(1);             // Draw 2X-scale text
  display.setTextColor(WHITE);        // Draw white text
  display.setCursor(0, 0);            // Start at top-left corner
  display.print("      ");
  display.println("WEAREMATE");

  int sensorValue;
  sensorValue = (mean(30)/6.14);
  //sensorValue = map(sensorValue, 69, 100, 0, 100);
  Serial.print("Soil moisture: ");
  Serial.print(sensorValue);
  Serial.println(" %");

  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.println("SOILMOISTRUE");
  display.println("");
  display.setTextSize(2);
  display.print(sensorValue);
  display.println(" %");
  display.display();

 // digitalWrite(7, HIGH); 
 // delay(100);
 // digitalWrite(7, LOW);
 // delay(100);

}

int mean(int n)
{
  int m = 0;
  for( int i = 0; i<n; i++)
  {
    m = m + analogRead(sensorPin);
  }
  return m/n;
} 
