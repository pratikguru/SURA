#include "Arduino.h"
#include <Servo.h>
#ifndef THRUSTER
#define THRUSTER

class thrusters{
 
  public:
        thrusters();
        thrusters(int pin_number);
        ~thrusters();
        int thrust(int timing);
        bool initialize_thrusters(int init_time);
        
  private:  

    int pin_number;
    int timing;
    Servo thruster_one;
};


#endif
