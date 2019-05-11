// Auto-generated. Do not edit!

// (in-package treinamento.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class mymessage {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.impar = null;
      this.par = null;
    }
    else {
      if (initObj.hasOwnProperty('impar')) {
        this.impar = initObj.impar
      }
      else {
        this.impar = 0.0;
      }
      if (initObj.hasOwnProperty('par')) {
        this.par = initObj.par
      }
      else {
        this.par = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type mymessage
    // Serialize message field [impar]
    bufferOffset = _serializer.float32(obj.impar, buffer, bufferOffset);
    // Serialize message field [par]
    bufferOffset = _serializer.float32(obj.par, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type mymessage
    let len;
    let data = new mymessage(null);
    // Deserialize message field [impar]
    data.impar = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [par]
    data.par = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'treinamento/mymessage';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '572be5cba3decd7de0c8c159cd353f2c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 impar
    float32 par
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new mymessage(null);
    if (msg.impar !== undefined) {
      resolved.impar = msg.impar;
    }
    else {
      resolved.impar = 0.0
    }

    if (msg.par !== undefined) {
      resolved.par = msg.par;
    }
    else {
      resolved.par = 0.0
    }

    return resolved;
    }
};

module.exports = mymessage;
