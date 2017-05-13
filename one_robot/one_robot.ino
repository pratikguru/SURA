
//#include <Stepper.h>
#include "led.h"
#include "gripper.h"
#include "rotationGripper.h"
#include <Servo.h>
#include "BLDC.h"
const int stepsPerRevolution = 200;  

gripper grip(65, 5,3,4,2);  
rotGrip rot(6,7);
thrusters f(11);
thrusters q(10);


int stepCount = 0;         
char data;

led my(8,9);

void setup() {
  Serial.begin(115200);
  pinMode(A0, INPUT);
}

int i = 0;
String data2;

void loop() {
  int val1 = 0;
  int valmoist;
  valmoist = analogRead(A0);
  Serial.println(valmoist);
 /*
  while(Serial.available() > 0){
    data = Serial.read();
    data2 += data;
    i++;S
  }
  if(i == 10){
   Serial.write("k");
   i = 0;
   Serial.println(data2); 
   q.thrust(data2.substring(0,3).toInt());
   Serial.println(data2.substring(1,3).toInt());
   
   data2 = "";
   
  }
   
   */
   
   
   while(Serial.available() > 0){
    data = Serial.read();
    if(data == 'o'){
      my.flashOn();
   }
   else if(data == 'l'){
     
    my.flashOff(); 
   }
   else if(data == '4'){
     rot.Rotate_clockWise();
   }
   else if(data == '5'){
    rot.Rotate_antiClockWise();
   }
   
   else if(data == 's'){
    rot.stop_rotation(); 
   }
    
    else if(data == '1'){
      grip.stepq(1);
      stepCount++;
      
    }
    
    else if(data == '2'){
     grip.stepq(-1);
     stepCount--;
    //delay(500); 
    }
}

}






