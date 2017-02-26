; Auto-generated. Do not edit!


(cl:in-package image_processing-msg)


;//! \htmlinclude bot_state.msg.html

(cl:defclass <bot_state> (roslisp-msg-protocol:ros-message)
  ((num_circles
    :reader num_circles
    :initarg :num_circles
    :type cl:fixnum
    :initform 0)
   (pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:Pose2D
    :initform (cl:make-instance 'geometry_msgs-msg:Pose2D)))
)

(cl:defclass bot_state (<bot_state>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <bot_state>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'bot_state)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name image_processing-msg:<bot_state> is deprecated: use image_processing-msg:bot_state instead.")))

(cl:ensure-generic-function 'num_circles-val :lambda-list '(m))
(cl:defmethod num_circles-val ((m <bot_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader image_processing-msg:num_circles-val is deprecated.  Use image_processing-msg:num_circles instead.")
  (num_circles m))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <bot_state>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader image_processing-msg:pose-val is deprecated.  Use image_processing-msg:pose instead.")
  (pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <bot_state>) ostream)
  "Serializes a message object of type '<bot_state>"
  (cl:let* ((signed (cl:slot-value msg 'num_circles)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <bot_state>) istream)
  "Deserializes a message object of type '<bot_state>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num_circles) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<bot_state>)))
  "Returns string type for a message object of type '<bot_state>"
  "image_processing/bot_state")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'bot_state)))
  "Returns string type for a message object of type 'bot_state"
  "image_processing/bot_state")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<bot_state>)))
  "Returns md5sum for a message object of type '<bot_state>"
  "5b2e80437805ede8f38eb11e1d06bb53")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'bot_state)))
  "Returns md5sum for a message object of type 'bot_state"
  "5b2e80437805ede8f38eb11e1d06bb53")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<bot_state>)))
  "Returns full string definition for message of type '<bot_state>"
  (cl:format cl:nil "int8 num_circles~%geometry_msgs/Pose2D pose~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'bot_state)))
  "Returns full string definition for message of type 'bot_state"
  (cl:format cl:nil "int8 num_circles~%geometry_msgs/Pose2D pose~%~%================================================================================~%MSG: geometry_msgs/Pose2D~%# This expresses a position and orientation on a 2D manifold.~%~%float64 x~%float64 y~%float64 theta~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <bot_state>))
  (cl:+ 0
     1
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <bot_state>))
  "Converts a ROS message object to a list"
  (cl:list 'bot_state
    (cl:cons ':num_circles (num_circles msg))
    (cl:cons ':pose (pose msg))
))
