#include <Stepper.h>

const int stepsPerRevolution = 512;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);

char serialData;

void setup() {
  // set the speed at 60 rpm:
  myStepper.setSpeed(60);
  Serial.begin(9600);

}

void loop() {
  if(Serial.available() > 0){
    serialData = Serial.read();
    Serial.print(serialData);

    if(serialData = '1'){
      myStepper.step(-stepsPerRevolution);

      delay(5000);

      myStepper.step(stepsPerRevolution);
    }
    
  }
}
