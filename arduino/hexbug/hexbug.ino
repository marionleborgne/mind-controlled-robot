/*

  Purpose: This code assumes that you've hacked the IR remote control of a hex bug
  to allow the Arduino to "push" the remote control's buttons.  You issue serial commands
  from the PC, which are received by the Arduino, when then interacts with the remote control.
  
  Hex Bug IR Remote: There are four buttons on the Hex Bug IR remote.   The high side of
  each button attached to the remote control's microcontroller, which must use a pull-up
  to hold the pin at 3.3V.  The low side of each button is connected to ground so that,
  when the button is pressed, the pin goes low by conducting through the now-closed button.

  Hack: Wires are soldered to the high side of each button and to the remote's "ground".
  These wires are connected to the Arduino. 
  
  Normally, the Arduino pins are set to "OUTPUT" and "HIGH".
  To make the Arduino to "push" one of the buttons, the idea is to change
  the pin to "OUTPUT" and "LOW", which gives a low-resistance path to ground.
  As a result, it pulls the remote's   microcontroller pin low,
  which makes the remote think that a button was pressed.
  
  License: MIT License 2014
 
 */

int pins[]= {2, 3};
#define NPINS 2
#define COMMAND_FOREWARD 0
#define COMMAND_LEFT 1

volatile char inChar;
unsigned long lastCommand_millis = 0;
int commndDuration_millis = 500;


void setup() {
  // initialize serial:
  Serial.begin(9600);
  
  // print help
  Serial.println("TestHexBugController: starting...");
  Serial.println("Commands Include: ");
  Serial.println("    'f' = Forward");
  Serial.println("    'l' = Left");
  
  //initialize the pins
  stopAllPins();
}

void stopAllPins() {
  //stopping all pins means putting them into a high impedance state
  //Serial.println("Stopping All Pins...");
  for (int Ipin=0; Ipin < NPINS; Ipin++) {
    pinMode(pins[Ipin],OUTPUT);
    digitalWrite(pins[Ipin],HIGH);
    
  }
}

void loop() {
  // print the string when a newline arrives:
  if (millis() > lastCommand_millis+commndDuration_millis) {
    lastCommand_millis = millis()+10000; //don't do this branch for a while
    stopAllPins();
  }
}

void issueCommand(int command_pin_ind) {
  if (command_pin_ind < NPINS) {
    stopAllPins();
    pinMode(pins[command_pin_ind],OUTPUT);
    digitalWrite(pins[command_pin_ind],LOW);
    Serial.print("command pin index : "); Serial.println(command_pin_ind);
    Serial.print("pin : "); Serial.println(pins[command_pin_ind]);
    lastCommand_millis = millis();  //time the command was received
  }
}
 

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    Serial.print("Received "); Serial.println(inChar);
    switch (inChar) {
     case 'f':
       issueCommand(COMMAND_FOREWARD); break;
     case 'l':
       issueCommand(COMMAND_LEFT); break;
     }
  }
}


