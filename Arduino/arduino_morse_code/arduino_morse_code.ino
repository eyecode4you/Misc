/* arduino_morse_code.ino - Convert inputted message to Morse Code (International) and display on OLED screen 
   Jonathan Mooney D19124230 24/11/2020
   DT080A IoT Final Project
*/
#include <Arduino.h>
#include <U8x8lib.h>
#include "morse_check.h"

U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE); //u8x8 Object

const int b_pin = 6; //Push Button Pin
char msg[17] = "tu dublin iot!!"; //Word to convert to Morse
int len = strlen(msg); //Length of word

void setup() { 
pinMode(b_pin, INPUT); //Set push button as an input

//OLED SETUP
u8x8.begin();
u8x8.setFlipMode(1);
u8x8.setFont(u8x8_font_chroma48medium8_r); //Set OLED Font

//Due to size of OLED, message can only be up to 16 Characters in length
if(len>16){
  u8x8.setCursor(0, 0);
  u8x8.print("ERROR! MSG > 16!");
  exit(1);
  }
  
//Convert msg to upper case for checking characters
for(int i = 0; msg[i]; i++) msg[i] = toupper(msg[i]);

//DISPLAY INTRO MESSAGE
u8x8.setCursor(0, 0);
u8x8.print("Morse Code Msg:");
u8x8.setCursor(0, 4);
u8x8.print("Push Button");
u8x8.setCursor(0, 5);
u8x8.print("To Begin");

u8x8.setFont(u8x8_font_victoriamedium8_u);
}

void loop() {
  int b_state = digitalRead(b_pin); //Get state of button

  if (b_state == 1) { //If button is pressed
    u8x8.setCursor(0, 2);
    u8x8.print("                "); //Clear message on screen
    for(int x = 0; msg[x]; x++){ //For each character in message
      morse_check(msg[x]); //Check character in message
      u8x8.print(msg[x]);  //Print character in message
      delay(150); //Delay between each character in message
      }
    }
}
