
(cl:in-package :asdf)

(defsystem "image_processing-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "ball" :depends-on ("_package_ball"))
    (:file "_package_ball" :depends-on ("_package"))
    (:file "bot_state" :depends-on ("_package_bot_state"))
    (:file "_package_bot_state" :depends-on ("_package"))
  ))