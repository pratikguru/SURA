

#include "led.h"
#include   "Arduino.h"
led::led(){
}

led::led(int pin1, int pin2):pin1_(pin1), pin2_(pin2){
pinMode(pin1, OUTPUT);
pinMode(pin2, OUTPUT);
  
  
}


led:: ~led(){
}
bool led::flashOn(){
digitalWrite(pin1_, HIGH);
digitalWrite(pin2_, LOW);
Serial.println("on");
return 1;
}

bool led::flashOff(){
digitalWrite(pin1_, LOW);
digitalWrite(pin2_, LOW);
Serial.println("off");
return 2;

}
