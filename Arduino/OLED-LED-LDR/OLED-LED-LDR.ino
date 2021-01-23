/* Arduino Grove Program that reads in data from Light sensor, turns LED on/off and displays info on OLED screen
   EyeCode4You - Do what you like with this file!
   Arduino IDE v1.8.9
   Based on: https://wiki.seeedstudio.com/Grove-OLED_Display_1.12inch/
   Using U8x8 Graphics library: https://github.com/olikraus/u8g2/wiki/u8x8reference
*/

#include <Arduino.h>
#include <U8x8lib.h>

 U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);
 
// U8X8_SSD1306_128X64_NONAME_SW_I2C u8x8(/* clock=*/ SCL, /* data=*/ SDA, /* reset=*/ U8X8_PIN_NONE);   // OLEDs without Reset of the Display

const int ledPin=4;                 //Constant we use for the GROVE LED (Pin 4 on the board)
const int thresholdvalue=10;        //The threshold on the Light sensor for which the LED should turn on. 
float Rsensor; //Resistance of sensor in K

void intro(){ //print initial message to OLED
  u8x8.clear(); //clear OLED screen
  u8x8.setInverseFont(1);
  u8x8.draw1x2String(4, 2, "Light");
  delay(500); //(half second delay)
  u8x8.draw1x2String(2, 4, "Intensity!");
  delay(500);
  u8x8.setInverseFont(0);
  }

void night(int Rsensor){//Low light intensity
  char buffer [30];//for int to string conversion with itoa()
  u8x8.clear();
  u8x8.draw1x2String(5, 0, itoa(Rsensor, buffer, 10));
  delay(25);
  u8x8.draw1x2String(5, 2, "Night");
  delay(25);
  u8x8.draw1x2String(5, 4, "Time!");
  delay(250);
  }

void day(int Rsensor){//High light intensity
   char buffer [30];//for int to string conversion with itoa()
   u8x8.clear();
   u8x8.draw1x2String(5, 0, itoa(Rsensor, buffer, 10));
   delay(25);
   u8x8.draw1x2String(5, 2, "Day");
   delay(25);
   u8x8.draw1x2String(5, 4, "Time!"); 
  }

void setup() {
  Serial.begin(9600);    //Start the Serial connection
  pinMode(ledPin,OUTPUT);  //Set the LED as an OUTPUT. Pin = 4 (From our const above!)
  u8x8.begin();
  u8x8.setFlipMode(1);
}

void loop() {
  int sensorValue = analogRead(6); //create var for light sensor
  Rsensor=(float)(1023-sensorValue)*10/sensorValue;
  u8x8.setFont(u8x8_font_chroma48medium8_r); //set OLED font
  
  intro();//Intro message
  
  if(Rsensor>thresholdvalue)
  {
    digitalWrite(ledPin,HIGH); //Turn LED on
    
    for(int i=0; i<1; i++){
      night(Rsensor);
      }
  }
  else
  {
    digitalWrite(ledPin,LOW); //Turn LED off
    for(int i=0; i<1; i++){
      day(Rsensor); 
      }
  }
  delay(2000);//delay for 2 seconds
}//end main loop
