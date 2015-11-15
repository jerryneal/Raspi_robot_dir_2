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


int angle,i;
int maxAngle = 180;
Servo array[] = {myServo1,myServo2,myServo3,myServo4,myServo5,myServo6,myServo7,myServo8};
Servo lefthandarray[] = {myServo1,myServo2,myServo3,myServo4};
Servo righthandarray[] = {myServo5,myServo6,myServo7,myServo8};
void setup() 
{
  
  myServo1.attach(1);
  myServo2.attach(2);
  myServo3.attach(3);
  myServo4.attach(4);
  myServo5.attach(5);
  myServo6.attach(6);
  myServo7.attach(7);
  myServo8.attach(8);
 
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