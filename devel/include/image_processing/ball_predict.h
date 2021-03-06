// Generated by gencpp from file image_processing/ball_predict.msg
// DO NOT EDIT!


#ifndef IMAGE_PROCESSING_MESSAGE_BALL_PREDICT_H
#define IMAGE_PROCESSING_MESSAGE_BALL_PREDICT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace image_processing
{
template <class ContainerAllocator>
struct ball_predict_
{
  typedef ball_predict_<ContainerAllocator> Type;

  ball_predict_()
    : predicted_x(0.0)
    , predicted_y(0.0)  {
    }
  ball_predict_(const ContainerAllocator& _alloc)
    : predicted_x(0.0)
    , predicted_y(0.0)  {
  (void)_alloc;
    }



   typedef double _predicted_x_type;
  _predicted_x_type predicted_x;

   typedef double _predicted_y_type;
  _predicted_y_type predicted_y;




  typedef boost::shared_ptr< ::image_processing::ball_predict_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::image_processing::ball_predict_<ContainerAllocator> const> ConstPtr;

}; // struct ball_predict_

typedef ::image_processing::ball_predict_<std::allocator<void> > ball_predict;

typedef boost::shared_ptr< ::image_processing::ball_predict > ball_predictPtr;
typedef boost::shared_ptr< ::image_processing::ball_predict const> ball_predictConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::image_processing::ball_predict_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::image_processing::ball_predict_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace image_processing

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'image_processing': ['/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/src/image_processing/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::image_processing::ball_predict_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::image_processing::ball_predict_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::image_processing::ball_predict_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::image_processing::ball_predict_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::image_processing::ball_predict_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::image_processing::ball_predict_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::image_processing::ball_predict_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8ddf12d0486a66fc3a6ad21565f35185";
  }

  static const char* value(const ::image_processing::ball_predict_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8ddf12d0486a66fcULL;
  static const uint64_t static_value2 = 0x3a6ad21565f35185ULL;
};

template<class ContainerAllocator>
struct DataType< ::image_processing::ball_predict_<ContainerAllocator> >
{
  static const char* value()
  {
    return "image_processing/ball_predict";
  }

  static const char* value(const ::image_processing::ball_predict_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::image_processing::ball_predict_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 predicted_x\n\
float64 predicted_y\n\
";
  }

  static const char* value(const ::image_processing::ball_predict_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::image_processing::ball_predict_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.predicted_x);
      stream.next(m.predicted_y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct ball_predict_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::image_processing::ball_predict_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::image_processing::ball_predict_<ContainerAllocator>& v)
  {
    s << indent << "predicted_x: ";
    Printer<double>::stream(s, indent + "  ", v.predicted_x);
    s << indent << "predicted_y: ";
    Printer<double>::stream(s, indent + "  ", v.predicted_y);
  }
};

} // namespace message_operations
} // namespace ros

#endif // IMAGE_PROCESSING_MESSAGE_BALL_PREDICT_H
