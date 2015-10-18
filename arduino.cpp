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
  
void setup() 
{
  
  myServo1.attach(1);
  myServo2.attach(2);
  myServo3.attach(3);
  myServo4.attach(4);
  //myServo1.attach(5);
  //myServo2.attach(6);
  //myServo3.attach(7);
  //myServo4.attach(8);
  //myservo5
}

void loop()
{
  //rotations from 0 to 180 degrees
  for (angle=0; angle < maxAngle; angle++)
  {
    for (i=0; i<8; i++){
      array[i].write(angle);
    }
    delay(10);
  }
  //rotations from 180 back to 0 degrees
  for (angle=maxAngle; angle > 0; angle--)
  {
    for (i=0; i<8; i++){
      array[i].write(angle);
    }
    delay(10);
  }
}

