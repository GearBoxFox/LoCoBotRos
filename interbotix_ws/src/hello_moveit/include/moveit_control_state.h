#include <string>

#ifndef YASMIN_MOVEIT_CONTROL_STATE_H
#define YASMIN_MOVEIT_CONTROL_STATE_H

class MoveitControlState : public yasmin::State {
    public:
        MoveitControlState();
        ~MoveitControlState();

        std::string execute(std::share_ptr<yasmin::blackboard::Blackboard> blackboard);
}

#endif //YASMIN_MOVEIT_CONTROL_STATE_H