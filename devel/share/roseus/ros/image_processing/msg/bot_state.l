;; Auto-generated. Do not edit!


(when (boundp 'image_processing::bot_state)
  (if (not (find-package "IMAGE_PROCESSING"))
    (make-package "IMAGE_PROCESSING"))
  (shadow 'bot_state (find-package "IMAGE_PROCESSING")))
(unless (find-package "IMAGE_PROCESSING::BOT_STATE")
  (make-package "IMAGE_PROCESSING::BOT_STATE"))

(in-package "ROS")
;;//! \htmlinclude bot_state.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass image_processing::bot_state
  :super ros::object
  :slots (_num_circles _pose ))

(defmethod image_processing::bot_state
  (:init
   (&key
    ((:num_circles __num_circles) 0)
    ((:pose __pose) (instance geometry_msgs::Pose2D :init))
    )
   (send-super :init)
   (setq _num_circles (round __num_circles))
   (setq _pose __pose)
   self)
  (:num_circles
   (&optional __num_circles)
   (if __num_circles (setq _num_circles __num_circles)) _num_circles)
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:serialization-length
   ()
   (+
    ;; int8 _num_circles
    1
    ;; geometry_msgs/Pose2D _pose
    (send _pose :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _num_circles
       (write-byte _num_circles s)
     ;; geometry_msgs/Pose2D _pose
       (send _pose :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _num_circles
     (setq _num_circles (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _num_circles 127) (setq _num_circles (- _num_circles 256)))
   ;; geometry_msgs/Pose2D _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;;
   self)
  )

(setf (get image_processing::bot_state :md5sum-) "5b2e80437805ede8f38eb11e1d06bb53")
(setf (get image_processing::bot_state :datatype-) "image_processing/bot_state")
(setf (get image_processing::bot_state :definition-)
      "int8 num_circles
geometry_msgs/Pose2D pose

================================================================================
MSG: geometry_msgs/Pose2D
# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
float64 theta
")



(provide :image_processing/bot_state "5b2e80437805ede8f38eb11e1d06bb53")


