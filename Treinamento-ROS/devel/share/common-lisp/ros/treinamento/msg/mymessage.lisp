; Auto-generated. Do not edit!


(cl:in-package treinamento-msg)


;//! \htmlinclude mymessage.msg.html

(cl:defclass <mymessage> (roslisp-msg-protocol:ros-message)
  ((impar
    :reader impar
    :initarg :impar
    :type cl:float
    :initform 0.0)
   (par
    :reader par
    :initarg :par
    :type cl:float
    :initform 0.0))
)

(cl:defclass mymessage (<mymessage>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <mymessage>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'mymessage)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name treinamento-msg:<mymessage> is deprecated: use treinamento-msg:mymessage instead.")))

(cl:ensure-generic-function 'impar-val :lambda-list '(m))
(cl:defmethod impar-val ((m <mymessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader treinamento-msg:impar-val is deprecated.  Use treinamento-msg:impar instead.")
  (impar m))

(cl:ensure-generic-function 'par-val :lambda-list '(m))
(cl:defmethod par-val ((m <mymessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader treinamento-msg:par-val is deprecated.  Use treinamento-msg:par instead.")
  (par m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <mymessage>) ostream)
  "Serializes a message object of type '<mymessage>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'impar))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'par))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <mymessage>) istream)
  "Deserializes a message object of type '<mymessage>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'impar) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'par) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<mymessage>)))
  "Returns string type for a message object of type '<mymessage>"
  "treinamento/mymessage")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'mymessage)))
  "Returns string type for a message object of type 'mymessage"
  "treinamento/mymessage")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<mymessage>)))
  "Returns md5sum for a message object of type '<mymessage>"
  "572be5cba3decd7de0c8c159cd353f2c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'mymessage)))
  "Returns md5sum for a message object of type 'mymessage"
  "572be5cba3decd7de0c8c159cd353f2c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<mymessage>)))
  "Returns full string definition for message of type '<mymessage>"
  (cl:format cl:nil "float32 impar~%float32 par~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'mymessage)))
  "Returns full string definition for message of type 'mymessage"
  (cl:format cl:nil "float32 impar~%float32 par~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <mymessage>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <mymessage>))
  "Converts a ROS message object to a list"
  (cl:list 'mymessage
    (cl:cons ':impar (impar msg))
    (cl:cons ':par (par msg))
))
