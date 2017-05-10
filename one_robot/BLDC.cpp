#include "Arduino.h"
#include <Servo.h>
#include "BLDC.h"

thrusters::thrusters(){

}

thrusters::thrusters(int pin_number):pin_number(pin_number){
    
}

thrusters::~thrusters(){

}

int thrusters::thrust(int timing){
    
    thruster_one.attach(this->pin_number);
    thruster_one.writeMicroseconds(timing);
    
}

bool thrusters::initialize_thrusters(int init_time){
 
 thruster_one.writeMicroseconds(init_time);
  
}
