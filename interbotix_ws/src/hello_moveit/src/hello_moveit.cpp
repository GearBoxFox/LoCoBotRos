#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "interbotix_xs_msgs/msg/joint_single_command.hpp"

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class MinimalPublisher : public rclcpp::Node
{
  public:
    MinimalPublisher()
    : Node("minimal_publisher"), count_(0)
    {
      publisher_ = this->create_publisher<interbotix_xs_msgs::msg::JointSingleCommand>("/locobot/commands/joint_single", 10);
      timer_ = this->create_wall_timer(
      500ms, std::bind(&MinimalPublisher::timer_callback, this));
    }

  private:
    void timer_callback()
    {
      auto command = interbotix_xs_msgs::msg::JointSingleCommand();
      command.name = "tilt";
      command.cmd = 0;
      // RCLCPP_INFO(this->get_logger(), "Publishing Command");
      publisher_->publish(command);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<interbotix_xs_msgs::msg::JointSingleCommand>::SharedPtr publisher_;
    size_t count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}