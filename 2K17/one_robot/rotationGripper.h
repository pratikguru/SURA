#include "Arduino.h"
#ifndef rotationGripper
#define rotationGripper

class rotGrip{
  

  public:
        rotGrip();
        rotGrip(int pin1, int pin2);
        ~rotGrip();
        int Rotate_clockWise();
        int Rotate_antiClockWise();
        int stop_rotation();

  private:  

    int pin1;
    int pin2;

};


#endif
