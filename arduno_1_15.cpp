/*
 * Working code for martian spider
 * Written by Neal
 */

#include <Servo.h>


Servo r1;
Servo r2;
Servo r3;
Servo r4;
Servo r5;
Servo r6;
Servo r7;
Servo r8;
Servo l1;
Servo l2;
Servo l3;
Servo l4;
Servo l5;
Servo l6;
Servo l7;
Servo l8;

int low_angle = 0;
int high_angle = 0;
Servo lefthandarray[] = {l1,l2,l3,l4,l5,l6,l7,l8};
Servo righthandarray[] = {r1,r2,r3,r4,r5,r6,r7,r8};
//Servo first_genetic_array_lower[] = {}
//Servo second_genetic_array_lower[] = {}

void setup()
{
    
    l1.attach(2); //L1 - body //FL1
    l2.attach(3); //L2 - body //MFL1
    l3.attach(4); //L3 - body //MBL1
    l4.attach(5); //L4 - body //BL1
    l5.attach(6); //L5 - knee
    l6.attach(7); //L6 - knee
    l7.attach(8); //L7 - knee
    l8.attach(9); //L8 - knee
    r1.attach(30); //R1 - body //BR1
    r2.attach(31); //R2 - body //MBR1
    r3.attach(32); //R3 - body //MFR1
    r4.attach(33); //R4 - body //FR1
    r5.attach(34); //R5 - knee
    r6.attach(35); //R6 - knee
    r7.attach(36); //R7 - knee
    r8.attach(37); //R8 - knee
    
}

void loop() {
    //move_forward();
    move_to_zero();
    delay(2000);
    //move_to_zero();
    //move_backward();
    //delay(2000);
    
}

void move_to_zero(){
    for (int i=0; i<8; i++){
        lefthandarray[i].write(0);
    }
    for (int i=0; i<8; i++){
        righthandarray[i].write(0);
    }
}

void move_forward(){
    // Using Genetic - gaint
    for (int j=low_angle; j<high_angle; j++){
        l4.write(j);
        r3.write(j);
        l2.write(j);
        r1.write(j);
    }
    for (int i=high_angle; i>low_angle; i--){
        r4.write(i);
        l3.write(i);
        r2.write(i);
        l1.write(i);
    }
    
}

void move_backward(){
    // Using Genetic - gaint
    for (int j=low_angle; j<high_angle; j++){
        r4.write(j);
        l3.write(j);
        r2.write(j);
        l1.write(j);
    }
    for (int i=high_angle; i>low_angle; i--){
        l4.write(i);
        r3.write(i);
        l2.write(i);
        r1.write(i); 
    }
}

