;; Auto-generated. Do not edit!


(when (boundp 'treinamento::mymessage)
  (if (not (find-package "TREINAMENTO"))
    (make-package "TREINAMENTO"))
  (shadow 'mymessage (find-package "TREINAMENTO")))
(unless (find-package "TREINAMENTO::MYMESSAGE")
  (make-package "TREINAMENTO::MYMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude mymessage.msg.html


(defclass treinamento::mymessage
  :super ros::object
  :slots (_impar _par ))

(defmethod treinamento::mymessage
  (:init
   (&key
    ((:impar __impar) 0.0)
    ((:par __par) 0.0)
    )
   (send-super :init)
   (setq _impar (float __impar))
   (setq _par (float __par))
   self)
  (:impar
   (&optional __impar)
   (if __impar (setq _impar __impar)) _impar)
  (:par
   (&optional __par)
   (if __par (setq _par __par)) _par)
  (:serialization-length
   ()
   (+
    ;; float32 _impar
    4
    ;; float32 _par
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _impar
       (sys::poke _impar (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _par
       (sys::poke _par (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _impar
     (setq _impar (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _par
     (setq _par (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get treinamento::mymessage :md5sum-) "572be5cba3decd7de0c8c159cd353f2c")
(setf (get treinamento::mymessage :datatype-) "treinamento/mymessage")
(setf (get treinamento::mymessage :definition-)
      "float32 impar
float32 par

")



(provide :treinamento/mymessage "572be5cba3decd7de0c8c159cd353f2c")


