/* BuzzMell.ino - Musical melodies playing through piezo buzzer
 * EyeCode4You
 * Using pitches.h from https://gist.github.com/mikeputnam/2820675
 * Using U8x8 Graphics library: https://github.com/olikraus/u8g2/wiki/u8x8reference
 * */
#include <Arduino.h>
#include <U8x8lib.h>
#include "pitches.h"

U8X8_SSD1306_128X64_NONAME_HW_I2C u8x8(/* reset=*/ U8X8_PIN_NONE);

// Melody1 - Toccata & Fugue
int melody1[] = {
  NOTE_A5, NOTE_G5, NOTE_A5, 
  NOTE_G5, NOTE_F5, NOTE_E5, NOTE_D5, NOTE_CS5, NOTE_D5,
  
  NOTE_A4, NOTE_G4, NOTE_A4,
  NOTE_E4, NOTE_F4, NOTE_CS4, NOTE_D4,

  NOTE_A3, NOTE_G3, NOTE_A3,
  NOTE_G3, NOTE_F3, NOTE_E3, NOTE_D3, NOTE_CS3, NOTE_D3,

  //PART 2
  NOTE_D4, NOTE_F4, NOTE_AS4, NOTE_F4,
  NOTE_C4, NOTE_E4, NOTE_A4, NOTE_E4,
  NOTE_AS3, NOTE_D4, NOTE_G4, NOTE_D4,

  NOTE_A3, NOTE_CS4, NOTE_E4, 
  
  NOTE_A4, NOTE_D4, NOTE_AS4, NOTE_A3, NOTE_A4, NOTE_AS3, NOTE_G4, NOTE_A4,

  NOTE_D4, NOTE_F4, NOTE_AS4, NOTE_F4,
  NOTE_C4, NOTE_E4, NOTE_A4, NOTE_E4,
  NOTE_AS3, NOTE_D4, NOTE_G4, NOTE_D4,

  NOTE_A3, NOTE_CS4, NOTE_E4, 
  
  NOTE_A4, NOTE_D4, NOTE_AS4, NOTE_A3, NOTE_A4, NOTE_AS3, NOTE_G4, NOTE_A4,


  //PART 3
  NOTE_CS4, NOTE_D4, NOTE_E4,
  NOTE_CS4, NOTE_D4, NOTE_E4,
  NOTE_CS4, NOTE_D4, NOTE_E4,
  NOTE_CS4, NOTE_D4, 
  
  NOTE_E4, NOTE_F4, NOTE_G4,
  NOTE_E4, NOTE_F4, NOTE_G4,
  NOTE_E4, NOTE_F4, NOTE_G4,
  NOTE_E4, NOTE_F4, 
  
  NOTE_G4, NOTE_A4, NOTE_AS4,
  NOTE_G4, NOTE_A4, NOTE_AS4,
  NOTE_G4, NOTE_A4, NOTE_AS4,
  NOTE_G4, NOTE_A4,

  NOTE_CS5, NOTE_D5, NOTE_E5,
  NOTE_CS5, NOTE_D5, NOTE_E5,
  NOTE_CS5, NOTE_D5, NOTE_E5,
  NOTE_CS5, NOTE_D5, 
  
  NOTE_E5, NOTE_F5, NOTE_G5,
  NOTE_E5, NOTE_F5, NOTE_G5,
  NOTE_E5, NOTE_F5, NOTE_G5,
  NOTE_E5, NOTE_F5, 
  
  NOTE_G5, NOTE_A5, NOTE_AS5,
  NOTE_G5, NOTE_A5, NOTE_AS5,
  NOTE_G5, NOTE_A5, NOTE_AS5,
  NOTE_G5, NOTE_A5
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int nDurations1[] = {
  8, 8, 2,
  8, 8, 8, 8, 2, 2,

  8, 8, 2,
  8, 8, 8, 2,

  8, 8, 2,
  8, 8, 8, 8, 2, 2,

  //PART 2
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  12, 12, 12, 
  
  12, 6, 6, 6, 6, 6, 6, 3,

  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,

  12, 12, 12, 
  
  12, 6, 6, 6, 6, 6, 6, 3,

  //PART 3
  8, 12, 12,
  12, 12, 12,
  12, 12, 12,
  12, 12,

  8, 12, 12,
  12, 12, 12,
  12, 12, 12,
  12, 12,

  8, 12, 12,
  12, 12, 12,
  12, 12, 12,
  12, 2,

  8, 12, 12,
  12, 12, 12,
  12, 12, 12,
  12, 12,

  8, 12, 12,
  12, 12, 12,
  12, 12, 12,
  12, 12,

  8, 12, 12,
  12, 12, 12,
  12, 12, 12,
  12, 2
};

// Melody2 - Kokiri Forest
int melody2[] = {
  NOTE_G6, NOTE_C7, NOTE_G6, NOTE_E6, NOTE_D6, NOTE_E6, NOTE_F6,
  NOTE_G6, NOTE_A6, NOTE_G6, NOTE_F6, NOTE_G6, NOTE_F6,
  NOTE_E6, NOTE_D6, NOTE_E6, NOTE_C6,

  NOTE_AS4, NOTE_F4, NOTE_AS4, NOTE_D5, NOTE_C5, NOTE_G4
};

int nDurations2[] = {
  6, 6, 6, 6, 4, 4, 6,
  10, 10, 3, 10, 10, 3,
  6, 6, 6, 3,

  6, 6, 6, 6, 2, 2
};


// Melody3 - Metroid Fanfare
int melody3[] = {
  NOTE_F4, NOTE_AS4, NOTE_C5, NOTE_D5, 
  NOTE_E5, NOTE_C5, NOTE_G4, NOTE_C5,
  NOTE_F5, NOTE_D5, NOTE_AS4, NOTE_G4, NOTE_A4
};

int nDurations3[] = {
  7, 7, 7, 7,
  7, 7, 7, 7,
  7, 7, 7, 7, 2
};


// Melody4 - A Cruel Angel's Thesis
int melody4[] = {
  NOTE_C5, NOTE_DS5, NOTE_F5, NOTE_DS5, NOTE_F5,
  NOTE_F5, NOTE_F5, NOTE_AS5, NOTE_GS5,
  NOTE_G5, NOTE_F5, NOTE_G5,

  NOTE_G5, NOTE_AS5,
  NOTE_C6, NOTE_F5, NOTE_DS5,
  NOTE_AS5, NOTE_AS5, NOTE_G5, NOTE_AS5,
  NOTE_AS5, NOTE_C6
};

int nDurations4[] = {
  3, 3, 4, 4, 4,
  6, 6, 6, 6,
  7, 7, 2,

  3, 3,
  4, 4, 4,
  6, 6, 6, 6,
  3, 2
};


// Melody5 - Take On Me
int melody5[] = {
  NOTE_FS5, NOTE_FS5, NOTE_D5, 
  NOTE_B4, NOTE_B4, NOTE_E5, NOTE_E5, 
  NOTE_E5, NOTE_GS5, NOTE_GS5, NOTE_A5, NOTE_B5,
  NOTE_A5, NOTE_A5, NOTE_A5, NOTE_E5, NOTE_D5,
  NOTE_FS5, NOTE_FS5, NOTE_FS5,
  NOTE_E5, NOTE_E5, NOTE_FS5, NOTE_E5,

  NOTE_FS5, NOTE_FS5, NOTE_D5, 
  NOTE_B4, NOTE_B4, NOTE_E5, NOTE_E5, 
  NOTE_E5, NOTE_GS5, NOTE_GS5, NOTE_A5, NOTE_B5,
  NOTE_A5, NOTE_A5, NOTE_A5, NOTE_E5, NOTE_D5,
  NOTE_FS5, NOTE_FS5, NOTE_FS5,
  NOTE_E5, NOTE_E5, NOTE_FS5, NOTE_E5,
};

int nDurations5[] = {
  8, 8, 8, 
  4, 4, 4, 4, 
  8, 8, 8, 8, 8,
  8, 8, 8, 4, 4,
  4, 4, 8,
  8, 8, 8, 6,

  8, 8, 8, 
  4, 4, 4, 4, 
  8, 8, 8, 8, 8,
  8, 8, 8, 4, 4,
  4, 4, 8,
  8, 8, 8, 6,
};


// Melody6 - TEST
int melody6[] = {
  NOTE_C7
};

int nDurations6[] = {
  8
};

const int b_pin = 6;

void setup() {
pinMode(b_pin, INPUT);
u8x8.begin();
u8x8.setFlipMode(1);
}


void loop() {
  int sVal = analogRead(0) / 100; //Use potentiometer for tune selection
  int b_state = digitalRead(b_pin);

  if(sVal < 1){
    sVal = 1;
    }
  else if(sVal > 6){
    sVal = 6;
    }

  u8x8.setFont(u8x8_font_chroma48medium8_r); //set OLED font
  u8x8.setCursor(0, 0);
  u8x8.print("Tune To Play:");
  u8x8.print(sVal);
  u8x8.print("  ");

  //PLAY MELODY 1
  if (b_state == 1 && sVal == 1) {
    for (int tNote=0; tNote<137; tNote++){
      int nDuration = 1000/nDurations1 [tNote];
      tone(5, melody1 [tNote], nDuration);
      int pNotes = nDuration * 1.30;
      delay(pNotes);
      noTone(8);
      }
    }

    //PLAY MELODY 2
    else if (b_state == 1 && sVal == 2) {
    for (int tNote=0; tNote<23; tNote++){
      int nDuration = 1000/nDurations2 [tNote];
      tone(5, melody2 [tNote], nDuration);
      int pNotes = nDuration * 1.30;
      delay(pNotes);
      noTone(8);
      }
    }

    //PLAY MELODY 3
    else if (b_state == 1 && sVal == 3) {
    for (int tNote=0; tNote<13; tNote++){
      int nDuration = 1000/nDurations3 [tNote];
      tone(5, melody3 [tNote], nDuration);
      int pNotes = nDuration * 1.30;
      delay(pNotes);
      noTone(8);
      }
    }

    //PLAY MELODY 4
    else if (b_state == 1 && sVal == 4) {
    for (int tNote=0; tNote<23; tNote++){
      int nDuration = 1000/nDurations4 [tNote];
      tone(5, melody4 [tNote], nDuration);
      int pNotes = nDuration * 1.30;
      delay(pNotes);
      noTone(8);
      }
    }

    //PLAY MELODY 5
    else if (b_state == 1 && sVal == 5) {
    for (int tNote=0; tNote<48; tNote++){
      int nDuration = 1000/nDurations5 [tNote];
      tone(5, melody5 [tNote], nDuration);
      int pNotes = nDuration * 1.30;
      delay(pNotes);
      noTone(8);
      }
    }

    //PLAY MELODY 6
    else if (b_state == 1 && sVal == 6) {
    for (int tNote=0; tNote<1; tNote++){
      int nDuration = 1000/nDurations6 [tNote];
      tone(5, melody6 [tNote], nDuration);
      int pNotes = nDuration * 1.30;
      delay(pNotes);
      noTone(8);
      }
    }

}
