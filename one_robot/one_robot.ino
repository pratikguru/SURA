
//#include <Stepper.h>
#include "led.h"
#include "gripper.h"
#include "rotationGripper.h"
#include <Servo.h>
#include "BLDC.h"
const int stepsPerRevolution = 200;  


gripper grip(200, 5,3,4,2);  
rotGrip rot(A0,A1);
thrusters f(11);
thrusters q(10);


int stepCount = 0;         
char data;

led my(3,4);

void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
}

void loop() {
 
 while(Serial.available() > 0){
  
   data = Serial.read();
   Serial.println(data);
   if(data == 'op_grip'){
     q.thrust(1200);
 }
 else{
   q.thrust(0);
 }
 }
 
  
  
/*  
for(int i = 1000; i < 2000; i += 100){
  q.thrust(i);
  f.thrust(i);
  delay(1000);
  Serial.println(i);
  
}

for(int i = 2000; i < 1000; i--){
 
 q.thrust(i);
 f.thrust(i);
 delay(1000);
 Serial.println(i);
}

 
 
  while(Serial.available() > 0){
   data = Serial.read();
    if(data == '1'){
      grip.stepq(1);
      stepCount++;
      delay(10);
    }
   else if(data == '2'){
    grip.stepq(-1);
    stepCount--; 
   }
   
  else if(data == 'o'){
    my.flashOn(); 
    Serial.println("on");
}
  
  else if(data == 'l'){
    my.flashOff();
    Serial.println("off");
  }
}

*/
}

