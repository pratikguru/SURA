#include "Arduino.h"
#include "gripper.h"

gripper::gripper(){
    
}

gripper::gripper(int num_steps, int p1, int p2, int p3, int p4):num_steps(num_steps), p1_(p1),
    p2_(p2), p3_(p3), p4_(p4){

    this->step_number = 0;
    this->directionq = 0;
    this->last_step_time = 0;
    pinMode(p1_, OUTPUT);
    pinMode(p2_, OUTPUT);
    pinMode(p3_, OUTPUT);
    pinMode(p4_, OUTPUT);



    }

gripper::~gripper(){
  
}

void gripper::stepq(int steps_to_move)
{
  int steps_left = abs(steps_to_move);  // how many steps to take

  // determine direction based on whether steps_to_mode is + or -:
  if (steps_to_move > 0) { this->directionq = 1; }
  if (steps_to_move < 0) { this->directionq = 0; }


  // decrement the number of steps, moving one step each time:
  while (steps_left > 0)
  {
    unsigned long now = micros();
    // move only if the appropriate delay has passed:
    if (now - this->last_step_time >= this->delay_)
    {
      // get the timeStamp of when you stepped:
      this->last_step_time = now;
      // increment or decrement the step number,
      // depending on direction:
      if (this->directionq == 1)
      {
        this->step_number++;
        if (this->step_number == this->num_steps) {
          this->step_number = 0;
        }
      }
      else
      {
        if (this->step_number == 0) {
          this->step_number = this->num_steps;
        }
        this->step_number--;
      }
      // decrement the steps left:
      steps_left--;
      // step the motor to step number 0, 1, ..., {3 or 10}
      if (6 == 5)
        stepgripper(this->step_number % 10);
      else
        stepgripper(this->step_number % 4);
    }
  }
}


void gripper::stepgripper(int this_step){
    switch (this_step) {
      case 0:  // 1010
        digitalWrite(p1_, HIGH);
        digitalWrite(p2_, LOW);
        digitalWrite(p3_, LOW);
        digitalWrite(p4_, HIGH);
      break;
      case 1:  // 0110
        digitalWrite(p1_, HIGH);
        digitalWrite(p2_, HIGH);
        digitalWrite(p3_, LOW);
        digitalWrite(p4_, LOW);
      break;
      case 2:  //0101
        digitalWrite(p1_, LOW);
        digitalWrite(p2_, HIGH);
        digitalWrite(p3_, HIGH);
        digitalWrite(p4_, LOW);
      break;
      case 3:  //1001
        digitalWrite(p1_, LOW);
        digitalWrite(p2_, LOW);
        digitalWrite(p3_, HIGH);
        digitalWrite(p4_, HIGH);
      break;
     }

}
