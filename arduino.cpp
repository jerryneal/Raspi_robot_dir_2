//This is a version of what has been done.

#include <Servo.h>

Servo myServo1;
Servo myServo2;
Servo myServo3;
Servo myServo4;
Servo myServo5;
Servo myServo6;
Servo myServo7;
Servo myServo8;
Servo myServo9;
Servo myServo10;
Servo myServo11;
Servo myServo12;
Servo myServo13;
Servo myServo14;
Servo myServo15;
Servo myServo16;


int angle,i;
int maxAngle = 180;
//Servo array[] = {myServo1,myServo2,myServo3,myServo4,myServo5,myServo6,myServo7,myServo8};
Servo lefthandarray[] = {myServo1,myServo2,myServo3,myServo4,myServo5,myServo6,myServo7,myServo8};
Servo righthandarray[] = {myServo9,myServo10,myServo11,myServo12,myServo13,myServo14,myServo15,myServo16};
void setup() 
{
  
  myServo1.attach(2);
  myServo2.attach(3);
  myServo3.attach(4);
  myServo4.attach(5);
  myServo5.attach(6);
  myServo6.attach(7);
  myServo7.attach(8);
  myServo8.attach(9);
  myServo9.attach(30);
  myServo10.attach(31);
  myServo11.attach(32);
  myServo12.attach(33);
  myServo13.attach(34);
  myServo14.attach(35);
  myServo15.attach(36);
  myServo16.attach(37);
 
}

void loop() {
  forward();
  delay(2000);
  reverse();
  delay(2000);
}

void forward(){
  for (i=0; i<4; i++){
      lefthandarray[i].write(0);
   }
  for (i=0; i<4; i++){
      righthandarray[i].write(180);
   }
}
 
void reverse(){
 for (i=0; i<4; i++){
      lefthandarray[i].write(180);
   }
  for (i=0; i<4; i++){
      righthandarray[i].write(0);
   }
}

 void rightTurn(){
  for (i=0; i<4; i++){
    lefthandarray[i].write(180);
  }
  for (i=0; i<4; i++){
    righthandarray[i].write(180);
  }
}

 void leftTurn(){
 //   return
  for (i=0; i<4; i++){
    lefthandarray[i].write(0);
  }
  for (i=0; i<4; i++){
    righthandarray[i].write(0);
  }
 }

 void stopRobot(){
 //  return
 for (i=0; i<4; i++){
    lefthandarray[i].write(90);
  }
 for (i=0; i<4; i++){
    righthandarray[i].write(90);
 }
 } 