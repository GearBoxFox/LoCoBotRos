#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "sensor_msgs/msg/joy.hpp"
#include "kobuki_ros_interfaces/msg/led.hpp"
using std::placeholders::_1;

/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class TeleopController : public rclcpp::Node
{
  public:
    TeleopController()
    : Node("TeleopConroller")
    {
        joy_subscriber = this->create_subscription<sensor_msgs::msg::Joy>("joy_cmds", 10,
            std::bind(&TeleopController::joy_callback, this, _1));
        led_publisher = this->create_publisher<std_msgs::msg::String>("topic", 10);
    }

  private:
    void joy_callback(const sensor_msgs::msg::Joy & joy_msg) const 
    {
      // check if certain buttons have been pressed
      if (joy_msg.buttons[0])
      {
        RCLCPP_INFO(this->get_logger(), "Button '0' pressed!\n");
      } 
    }
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr led_publisher;
    rclcpp::Subscription<sensor_msgs::msg::Joy>::SharedPtr joy_subscriber;
};