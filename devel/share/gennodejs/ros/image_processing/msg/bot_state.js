// Auto-generated. Do not edit!

// (in-package image_processing.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class bot_state {
  constructor() {
    this.num_circles = 0;
    this.pose = new geometry_msgs.msg.Pose2D();
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type bot_state
    // Serialize message field [num_circles]
    bufferInfo = _serializer.int8(obj.num_circles, bufferInfo);
    // Serialize message field [pose]
    bufferInfo = geometry_msgs.msg.Pose2D.serialize(obj.pose, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type bot_state
    let tmp;
    let len;
    let data = new bot_state();
    // Deserialize message field [num_circles]
    tmp = _deserializer.int8(buffer);
    data.num_circles = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [pose]
    tmp = geometry_msgs.msg.Pose2D.deserialize(buffer);
    data.pose = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'image_processing/bot_state';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5b2e80437805ede8f38eb11e1d06bb53';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 num_circles
    geometry_msgs/Pose2D pose
    
    ================================================================================
    MSG: geometry_msgs/Pose2D
    # This expresses a position and orientation on a 2D manifold.
    
    float64 x
    float64 y
    float64 theta
    `;
  }

};

module.exports = bot_state;
