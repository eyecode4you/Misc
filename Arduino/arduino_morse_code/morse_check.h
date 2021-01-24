/*
  morse_check.h - Check letter passed in by main and play International Morse code equivalent
  EyeCode4You
  International Morse Code Chart from: https://otasurvivalschool.com/signalling/learn-the-morse-code/
 
  Order of Operation based on Highest Letter Frequency in English language:
  e.g. "etaoinshrdlcumwfgypbvkjxqz"
  https://en.wikipedia.org/wiki/Letter_frequency
*/
#include <Arduino.h>
#define NC7  2093 //Buzzer tone for dots and dashes

const int l_pin = LED_BUILTIN; //BUILTIN LED Pin

// DOT - Dot tone + duration
void dot(){
  pinMode(l_pin, OUTPUT); //Set LED as output
  digitalWrite(l_pin,HIGH); //Turn on LED for duration of dot
  int dot_sound = NC7;
  int dot_duration = 8;
  int nDuration = 1000/dot_duration;
  int pNotes = nDuration * 1.30;
  tone(5, dot_sound, nDuration);
  delay(pNotes);
  noTone(5);
  digitalWrite(l_pin,LOW);
  delay(8);
 }

// DASH - Dash tone + duration
void dash(){
  pinMode(l_pin, OUTPUT); //Set LED as output
  digitalWrite(l_pin,HIGH); //Turn on LED for duration of dot
  int dash_sound = NC7;
  int dash_duration = 4;
  int nDuration = 1000/dash_duration;
  int pNotes = nDuration * 1.30;
  tone(5, dash_sound, nDuration);
  delay(pNotes);
  noTone(5);
  digitalWrite(l_pin,LOW);
  delay(8);
 }

//Letters in order of increasing time to transmit i.e. "eitsanhurdmwgvlfbkopxczjyq"
void Le(){dot();}
void Li(){for(int y=0; y<2; y++){dot();}}
void Lt(){dash();}
void Ls(){for(int y=0; y<3; y++){dot();}}
void La(){dot(); dash();}
void Ln(){dash(); dot();}
void Lh(){for(int y=0; y<4; y++){dot();}}
void Lu(){dot(); dot(); dash();}
void Lr(){dot(); dash(); dot();}
void Ld(){dash(); dot(); dot();}
void Lm(){for(int y=0; y<2; y++){dash();}}
void Lw(){dot(); dash(); dash();}
void Lg(){dash(); dash(); dot();}
void Lv(){Ls(); dash();}
void Ll(){Lr(); dot();}
void Lf(){Lu(); dot();}
void Lb(){Ld(); dot();}
void Lk(){dash(); dot(); dash();}
void Lo(){for(int y=0; y<3; y++){dash();}}
void Lp(){Lw(); dot();}
void Lx(){Ld(); dash();}
void Lc(){Lk(); dot();}
void Lz(){Lg(); dot();}
void Lj(){Lw(); dash();}
void Ly(){Lk(); dash();}
void Lq(){Lg(); dash();}

//Numbers in no particular order
void N0(){Lo(); Lm();}
void N1(){dot(); dash(); Lo();}
void N9(){Lo(); dash(); dot();}
void N2(){Li(); Lo();}
void N8(){Lo(); Li();}
void N3(){Ls(); Lm();}
void N7(){Lm(); Ls();}
void N4(){Lh(); dash();}
void N6(){dash(); Lh();}
void N5(){Lh(); dot();}
void morse_num_check(char N){
  if(N == '0'){
    N0();
  }else if(N == '1'){
    N1();
  }else if(N == '2'){
    N2();
  }else if(N == '3'){
    N3();
  }else if(N == '4'){
    N4();
  }else if(N == '5'){
    N5();
  }else if(N == '6'){
    N6();
  }else if(N == '7'){
    N7();
  }else if(N == '8'){
    N8();
  }else if(N == '9'){
    N9();
  }
 }

//Characters .,?'!/:;=+-_"@
void Cdot(){for(int y=0; y<3; y++){La();}}
void Ccomma(){Lz(); Lm();}
void Cques(){Lu(); Ld();}
void Capos(){N1(); dot();}
void Cex(){Lc(); Lm();}
void Cslash(){Lx(); dot();}
void Colon(){N8(); dot();}
void Colonsemi(){Lc(); Ln();}
void Ceq(){Lb(); dash();}
void Cplus(){Lr(); Ln();}
void Cmin(){N6(); dash();}
void Cuscore(){Lu(); Lk();}
void Cquo(){Ll(); Ln();}
void Cat(){Lw(); Lr();}
void morse_char_check(char C){
  if(C == '.'){
    Cdot();
   }else if(C == ','){
    Ccomma();
   }else if(C == '?'){
    Cques();
   }else if(C == '\''){
    Capos();
   }else if(C == '!'){
    Cex();
   }else if(C == '/'){
    Cslash();
   }else if(C == ':'){
    Colon();
   }else if(C == ';'){
    Colonsemi();
   }else if(C == '='){
    Ceq();
   }else if(C == '+'){
    Cplus();
   }else if(C == '-'){
    Cmin();
   }else if(C == '_'){
    Cuscore();
   }else if(C == '\"'){
    Cquo();
   }else if(C == '@'){
    Cat();
   }
}

//Check Letters in message and play tone
void morse_check(char L){
  if(L == 'E'){
    Le();
   }else if(L == 'T'){
    Lt();
   }else if(L == 'A'){
    La();
   }else if(L == 'O'){
    Lo();
   }else if(L == 'I'){
    Li();
   }else if(L == 'N'){
    Ln();
   }else if(L == 'S'){
    Ls();
   }else if(L == 'H'){
    Lh();
   }else if(L == 'R'){
    Lr();
   }else if(L == 'D'){
    Ld();
   }else if(L == 'L'){
    Ll();
   }else if(L == 'C'){
    Lc();
   }else if(L == 'U'){
    Lu();
   }else if(L == 'M'){
    Lm();
   }else if(L == 'W'){
    Lw();
   }else if(L == 'F'){
    Lf();
   }else if(L == 'G'){
    Lg();
   }else if(L == 'Y'){
    Ly();
   }else if(L == 'P'){
    Lp();
   }else if(L == 'B'){
    Lb();
   }else if(L == 'V'){
    Lv();
   }else if(L == 'K'){
    Lk();
   }else if(L == 'J'){
    Lj();
   }else if(L == 'X'){
    Lx();
   }else if(L == 'Q'){
    Lq();
   }else if(L == 'Z'){
    Lz();
   }else if(L == ' '){
    delay(25);
   }else{
    morse_num_check(L);
    morse_char_check(L);
   }
    
  }
