#include "Arduino.h"
#ifndef gripper_h
#define gripper_h   



class gripper{
    
public:
        gripper();
        gripper(int num_steps, int p1, int p2, int p3, int p4);
        ~gripper();
        void stepq(int steps);




private:
    int p1_;
    int p2_;
    int p3_;
    int p4_;
    int num_steps;

    void stepgripper(int this_step);

    int directionq;
    unsigned long delay_;
    int step_number;
    unsigned long last_step_time;

};

#endif
