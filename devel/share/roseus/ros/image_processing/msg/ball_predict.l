;; Auto-generated. Do not edit!


(when (boundp 'image_processing::ball_predict)
  (if (not (find-package "IMAGE_PROCESSING"))
    (make-package "IMAGE_PROCESSING"))
  (shadow 'ball_predict (find-package "IMAGE_PROCESSING")))
(unless (find-package "IMAGE_PROCESSING::BALL_PREDICT")
  (make-package "IMAGE_PROCESSING::BALL_PREDICT"))

(in-package "ROS")
;;//! \htmlinclude ball_predict.msg.html


(defclass image_processing::ball_predict
  :super ros::object
  :slots (_predicted_x _predicted_y ))

(defmethod image_processing::ball_predict
  (:init
   (&key
    ((:predicted_x __predicted_x) 0.0)
    ((:predicted_y __predicted_y) 0.0)
    )
   (send-super :init)
   (setq _predicted_x (float __predicted_x))
   (setq _predicted_y (float __predicted_y))
   self)
  (:predicted_x
   (&optional __predicted_x)
   (if __predicted_x (setq _predicted_x __predicted_x)) _predicted_x)
  (:predicted_y
   (&optional __predicted_y)
   (if __predicted_y (setq _predicted_y __predicted_y)) _predicted_y)
  (:serialization-length
   ()
   (+
    ;; float64 _predicted_x
    8
    ;; float64 _predicted_y
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _predicted_x
       (sys::poke _predicted_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _predicted_y
       (sys::poke _predicted_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _predicted_x
     (setq _predicted_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _predicted_y
     (setq _predicted_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get image_processing::ball_predict :md5sum-) "8ddf12d0486a66fc3a6ad21565f35185")
(setf (get image_processing::ball_predict :datatype-) "image_processing/ball_predict")
(setf (get image_processing::ball_predict :definition-)
      "float64 predicted_x
float64 predicted_y

")



(provide :image_processing/ball_predict "8ddf12d0486a66fc3a6ad21565f35185")


