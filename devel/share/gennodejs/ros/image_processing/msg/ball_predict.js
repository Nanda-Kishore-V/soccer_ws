// Auto-generated. Do not edit!

// (in-package image_processing.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class ball_predict {
  constructor() {
    this.predicted_x = 0.0;
    this.predicted_y = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type ball_predict
    // Serialize message field [predicted_x]
    bufferInfo = _serializer.float64(obj.predicted_x, bufferInfo);
    // Serialize message field [predicted_y]
    bufferInfo = _serializer.float64(obj.predicted_y, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type ball_predict
    let tmp;
    let len;
    let data = new ball_predict();
    // Deserialize message field [predicted_x]
    tmp = _deserializer.float64(buffer);
    data.predicted_x = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [predicted_y]
    tmp = _deserializer.float64(buffer);
    data.predicted_y = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'image_processing/ball_predict';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8ddf12d0486a66fc3a6ad21565f35185';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 predicted_x
    float64 predicted_y
    
    `;
  }

};

module.exports = ball_predict;
