#include <Arduino.h>
#include <imu.hpp>

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  while(!Serial);
  Wire.begin();

  while(!isIMU());

  clear();
  configureSensitivity();
}

void loop() {
  // put your main code here, to run repeatedly:
  readAngularSpeed();
  Serial.println("Funciona mesmo");
  
}