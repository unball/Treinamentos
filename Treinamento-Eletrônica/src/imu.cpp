#include <imu.hpp>

#define IMU_ADDRESS 0x68
#define REGISTER_WHOAMI_ADDR 0x75
#define WHO_AM_I_VALUE 0x68
#define REGISTER_CLEAR_ADDR
#define REGISTER_PWR_MGNT_ADDR 0x6b
#define REGISTER_PWR_MGNT2_ADDR 0x6c
#define REGISTER_ACCEL_CONFIG_ADDR 0x1c
#define REGISTER_GYRO_CONFIG_ADDR 0x1b 
#define REGISTER_GYRO_XOUT_ADDR 0x43
#define REGISTER_ACCEL_XOUT_ADDR 0x3b
#define REGISTER_FIFO_EN_ADDR 0x23

void write(uint8_t register_addr, uint8_t data){

    Wire.beginTransmission(IMU_ADDRESS);
    Wire.write(register_addr);
    Wire.write(data);
    Wire.endTransmission();
}

uint8_t read(uint8_t register_addr){
    Wire.beginTransmission(IMU_ADDRESS);
    Wire.write(register_addr);
    Wire.endTransmission();
    Wire.requestFrom(IMU_ADDRESS, 1);
    return Wire.read();
}

void read(uint8_t register_addr, uint8_t size, uint8_t data[]){
    Wire.beginTransmission(IMU_ADDRESS);
    Wire.write(register_addr);
    Wire.endTransmission();
    Wire.requestFrom((uint8_t)IMU_ADDRESS, size);
    for(uint8_t i=0; i<size; i++){
        data[i] = Wire.read();
    }
}

void clear(){
    write(REGISTER_PWR_MGNT_ADDR, 0b10000000);
    delay(50);
    write(REGISTER_PWR_MGNT_ADDR, 0b00000000);
    write(REGISTER_PWR_MGNT2_ADDR, 0b00000000);
}

bool isIMU(){
    return read(REGISTER_WHOAMI_ADDR) == WHO_AM_I_VALUE;
}

void configureSensitivity(){
    write(REGISTER_ACCEL_CONFIG_ADDR, 0b11100000);
    write(REGISTER_GYRO_CONFIG_ADDR, 0b00011000);
}

void readAngularSpeed(){
    uint16_t angularSpeed[3] = {0};
    read(REGISTER_GYRO_XOUT_ADDR, 6, (uint8_t *)angularSpeed);
    //read(REGISTER_ACCEL_XOUT_ADDR, 6, (uint8_t *)angularSpeed);
    Serial.println(angularSpeed[0]);

}