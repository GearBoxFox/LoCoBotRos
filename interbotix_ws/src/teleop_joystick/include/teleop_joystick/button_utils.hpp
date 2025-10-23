#include <functional>

// utility class for working with joystick buttons
class ButtonUtil
{
    public:
        ButtonUtil(std::function<bool()> input)
        {
            input_supplier = input;
        }
    private:
        std::function<bool()> input_supplier;
};