/*  Robo Fish V1 
 *  Amy Phung
 *  3/24/2021
*/

#include <Servo.h>

Servo tail_servo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
float pause = 6;
int range = 40;
int state = 0;

void setup() {
  tail_servo.attach(9);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
}

void loop() {
  while(Serial.available()){
    int serial_input = Serial.read();

    // Update state based on input
    switch (serial_input) {
      case 10:   // Enter key: ignore
        break;
      case 119:  // W: Go straight
        Serial.println("Straight");
        state = 1;
        break;
      case 97:  // A: Turn left
        Serial.println("Left");
        state = 2;
        break;
      case 100:  // D:Turn right
        Serial.println("Right");
        state = 3;
        break;
      default: // S(115) or any other key: E-stopped mode
        Serial.println("Stopped");
        state = 0;
        break;
    }
  }

  
  // Main action loop
  switch (state) {
    case 1:  // Go straight
      oscillate(90-range, 90+range, pause);
      break;
    case 2:  // Turn left
      oscillate(90-range, 90, pause);
      break;
    case 3:  // Turn right
      oscillate(90, 90+range, pause);
      break;
    default: // E-stopped mode
      tail_servo.write(90);
      break;
  }
}

void oscillate(int start_angle, int stop_angle, int pause) {
  for (pos = start_angle; pos <= stop_angle; pos += 1) {
    // in steps of 1 degree
    tail_servo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(pause);                       // wait for the servo to reach the position
  }
  for (pos = stop_angle; pos >= start_angle; pos -= 1) {
    // in steps of 1 degree
    tail_servo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(pause);                       // wait for the servo to reach the position
  }
}
