
//Author: Neal Bazirake
//Date : 11/14/2015
//Description : Using individual shift registers to get specific LEDs open for use

// SH_CP; 11
const int clockpin = 9;
// DS; 15
const int datapin = 8;
// ST_CP; 12
const int latchpin = 10;
const int ON = HIGH;
const int OFF = LOW;
int ledState = 0;
int loopCounter = 0;

void setup() {
  //set pins to output so you can control the shift register
  pinMode(latchpin, OUTPUT);
  pinMode(clockpin, OUTPUT);
  pinMode(datapin, OUTPUT);
}

void loop() {
	
   int delayTime = 100000000000;
  if (loopCounter < 4){
    delayTime=1; 
  }
  
  
   for(int i = 0; i < 8; i++){
     if( i == 0) {
     changeLED(i,ON);
     delay(delayTime);
     }
   }
   for (int i = 0; i < 7; i++){
     changeLED(i,OFF);
     //delay(delayTime);
   }
  loopCounter++;

}

void changeLED(int led, int state){
  //Used for single LED manipulation
	
	
//----------------->code cut here<-----------------

//These are used in the bitwise math that we use to change individual LEDs
//For more details http://en.wikipedia.org/wiki/Bitwise_operation
	int bits[] = {B00000001, B00000010, B00000100, B00001000,
              B00010000, B00100000, B01000000, B10000000};
	int masks[] = {B11111110, B11111101, B11111011, B11110111,
               B11101111, B11011111, B10111111, B01111111};
/*
 * changeLED(int led, int state) - changes an individual LED 
 * LEDs are 0 to 7 and state is either 0 - OFF or 1 - ON
 */
 	
  	 ledState = ledState & masks[led];  //clears ledState of the bit we are addressing

   //if the bit is on we will add it to ledState
     if(state == ON){ledState = ledState | bits[led];} 
     	updateLEDs(ledState);              //send the new LED state to the shift register
 }
  

void updateLEDs(int value){
  digitalWrite(latchpin, LOW);     //Pulls the chips latch low
  shiftOut(datapin, clockpin, MSBFIRST, value); //Shifts out the 8 bits to the shift register
  digitalWrite(latchpin, HIGH);   //Pulls the latch high displaying the data
}
