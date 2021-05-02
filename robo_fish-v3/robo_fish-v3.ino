/// There are several params that can be used!
/***
 *MODES 
 * (Q) (Stop mode that turns off the pumps!)
 * (T) TAIL MODE Using servo and pump adjustable hz, delay, on off, and flow rate
 * (F) FLOW MODE Runs the pump, allows steering with a servo 
 
 Program start in Q mode with everything off

 make sure serial monitor has no line endings turned on and is @9600 baud

 to turn on the fish go enter T to goto tail mode

 then enter s to change the pump speed and hit enter

 then enter a float value between 0 and 1 and hit enter

 the fish should start swithcing

 
 */


#include <Servo.h>

const int pumpLPin =  9;// the number of the pump pin
const int pumpRPin =  10;// the number of the pump pin
const int tailPin =  11;// the number of the tail servo pin
int pumpL_on = 0;
int pumpR_on = 1;
const String valid_params = "shd";//Speed, Hertz
float s = 1; //Speed of the pump 
float h = 1; //Hertz of the pump/tail
float t = 90; // Servo position
float d = 0.7; //Delay to turn off pump
int pump_val = 255*s;

char mode = 'Q';
bool mode_sw = false;
const long mode_sw_time = 1000; //Time to have nothing happen during a mode switch
unsigned long modeMillis = 0;
unsigned long last_update_tm = 0;
const unsigned long update_tm = 10000;
unsigned long last_cycle_tm = 0;


bool hz_del = false;
float pos_1 = 90;
float pos_2 = 0.0;
float cur_pos = pos_1;

bool param_edit = false;
char param;

Servo tailServo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
//  Servo1.attach(pumpLPin);
//  Servo1.attach(servoPin);
  tailServo.attach(tailPin);
}

void loop() {
  unsigned long currentMillis = millis();
  
  if(Serial.available() > 0)  {
    int incomingData;
    float paramData;
    //Parse characters and floats differnetly
    if (param_edit){
      paramData= Serial.parseFloat();
    }
    else{
      incomingData= Serial.read(); // can be -1 if read error
    }
    //HANDLE PARAMETER EDITING
    if (param_edit){
      if (paramData <= 0){
        param_edit = false;
        Serial.println("Quiting Param Edit mode");
      }
      else{
        //Call a param helper
        param_change(paramData);
      }
    }
    //HANDLE MODE SWITHCING and swithcing to paameter editing
    else{
      if (mode != incomingData){
        Serial.print("Current mode: ");
        Serial.println(mode);
        switch(incomingData) { 
            case 'Q':
              mode = incomingData;
              Serial.println("Stop Mode");
              s = 0;
              mode_helper();
              //MODE SWITCH PAUSE ALL INPUTS
              break;
            case 'F':
              mode = incomingData;
              Serial.println("Flow mode");
              mode_helper();
              //MODE SWITCH PAUSE ALL INPUTS
              break;
            case 'T':
              mode = incomingData;
              Serial.println("Tail Mode");
              mode_helper();
              break;
            //PARAMS
            default:
              int response = valid_params.indexOf(incomingData);
              if (response >= 0){
                param_helper(incomingData);
              }
              break;
        }
      }
    }
  }


  /*****
  *MOTOR ACTUATION CHUNK!! 
  */
  if (mode_sw){
    //Turn off the pump
    analogWrite(pumpLPin, 0);
    analogWrite(pumpRPin, 0);

    //Get out of mode switch mode then !!
    if (currentMillis - modeMillis >= mode_sw_time) {
      mode_sw = false;
      Serial.print("Starting mode: ");
      Serial.println(mode);
    }
  }
  //MAIN MODES 
  else{
    switch(mode){
      case 'F':
        /// Motor Controls and outputs here
        pump_val = 255*s;
        analogWrite(pumpLPin, pump_val);
        tailServo.write(val);
        
        break;
      case 'T':
        //Control servo every TS seconds
        // TS = 1/h seconds
        float Ts = 1/h*1000;//Milliseconds
        pump_val = 255*s;
        // 
        if(currentMillis-last_cycle_tm >= Ts){
          int temp = pumpL_on;
          pumpL_on = pumpR_on;
          pumpR_on = temp;
          hz_del = true;
          last_cycle_tm = currentMillis;
        }
        if(hz_del){
          pump_val = 0;
          if(currentMillis - last_cycle_tm >= d){
            hz_del = false;
          }
        }
        analogWrite(pumpLPin, pump_val*pumpL_on);
        analogWrite(pumpRPin, pump_val*pumpR_on);
        break;
    }
  }


  if (currentMillis -last_update_tm >= update_tm){
    //PRint and update of mode and params
    print_status(); 
    last_update_tm = currentMillis;
  }
}

void print_status(){
  Serial.print("Mode: ");
  Serial.println(mode);
  Serial.println("PARAMS");
  Serial.print("Pump Speed(s): ");
  Serial.println(s);
  Serial.print("Servo HZ(h): ");
  Serial.println(h);
  Serial.print("Delay (ms): ");
  Serial.println(d);
  Serial.print("Turn (deg): ");
  Serial.println(t);

}

void mode_helper(){
  Serial.print("Switching to mode: ");
  Serial.println(mode);
  mode_sw = true;
  modeMillis = millis();
  Serial.println("Disabling motors during a mode switch");
}

void param_helper(char new_param){
  Serial.print("Param Edit: ");
  Serial.println(new_param); 
  param = new_param;
  param_edit = true;
}

void param_change(float new_val){
  Serial.print("Setting: ");
  Serial.print(param);
  Serial.print(" : to -> ");
  Serial.println(new_val);
  switch(param){
    case 's':
      s = new_val; 
      break;
    case 'h':
      h = new_val;
      break;
    case 'd':
      d = new_val;
      break;
    case 't':
      d = new_val;
      break;
    default:
    Serial.print("Bad parameter to change");
      break;
  }
  param_edit = false;
  
}
