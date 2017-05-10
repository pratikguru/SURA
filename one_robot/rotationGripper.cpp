#include "Arduino.h"
#include "rotationGripper.h"

rotGrip::rotGrip(){

}

rotGrip::rotGrip(int pin1, int pin2):pin1(pin1), pin2(pin2){

    pinMode(pin1, OUTPUT);
    pinMode(pin2, OUTPUT);

}

rotGrip::~rotGrip(){

}

int rotGrip::Rotate_clockWise(){

digitalWrite(this->pin1, HIGH);
digitalWrite(this->pin2, LOW);

}

int rotGrip::Rotate_antiClockWise(){
digitalWrite(this->pin1, LOW);
digitalWrite(this->pin2, HIGH);

}

int rotGrip::stop_rotation(){

    digitalWrite(this->pin1, LOW);
    digitalWrite(this->pin2, LOW);
    
}


