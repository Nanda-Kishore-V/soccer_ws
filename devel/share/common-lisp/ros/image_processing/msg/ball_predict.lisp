; Auto-generated. Do not edit!


(cl:in-package image_processing-msg)


;//! \htmlinclude ball_predict.msg.html

(cl:defclass <ball_predict> (roslisp-msg-protocol:ros-message)
  ((predicted_x
    :reader predicted_x
    :initarg :predicted_x
    :type cl:float
    :initform 0.0)
   (predicted_y
    :reader predicted_y
    :initarg :predicted_y
    :type cl:float
    :initform 0.0))
)

(cl:defclass ball_predict (<ball_predict>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ball_predict>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ball_predict)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name image_processing-msg:<ball_predict> is deprecated: use image_processing-msg:ball_predict instead.")))

(cl:ensure-generic-function 'predicted_x-val :lambda-list '(m))
(cl:defmethod predicted_x-val ((m <ball_predict>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader image_processing-msg:predicted_x-val is deprecated.  Use image_processing-msg:predicted_x instead.")
  (predicted_x m))

(cl:ensure-generic-function 'predicted_y-val :lambda-list '(m))
(cl:defmethod predicted_y-val ((m <ball_predict>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader image_processing-msg:predicted_y-val is deprecated.  Use image_processing-msg:predicted_y instead.")
  (predicted_y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ball_predict>) ostream)
  "Serializes a message object of type '<ball_predict>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'predicted_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'predicted_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ball_predict>) istream)
  "Deserializes a message object of type '<ball_predict>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'predicted_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'predicted_y) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ball_predict>)))
  "Returns string type for a message object of type '<ball_predict>"
  "image_processing/ball_predict")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ball_predict)))
  "Returns string type for a message object of type 'ball_predict"
  "image_processing/ball_predict")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ball_predict>)))
  "Returns md5sum for a message object of type '<ball_predict>"
  "8ddf12d0486a66fc3a6ad21565f35185")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ball_predict)))
  "Returns md5sum for a message object of type 'ball_predict"
  "8ddf12d0486a66fc3a6ad21565f35185")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ball_predict>)))
  "Returns full string definition for message of type '<ball_predict>"
  (cl:format cl:nil "float64 predicted_x~%float64 predicted_y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ball_predict)))
  "Returns full string definition for message of type 'ball_predict"
  (cl:format cl:nil "float64 predicted_x~%float64 predicted_y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ball_predict>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ball_predict>))
  "Converts a ROS message object to a list"
  (cl:list 'ball_predict
    (cl:cons ':predicted_x (predicted_x msg))
    (cl:cons ':predicted_y (predicted_y msg))
))
