#include <string>

#pragma once

class MoveitControlState : public yasmin::State {
    public:
        MoveitControlState();
        ~MoveitControlState();

        std::string execute(std::share_ptr<yasmin::blackboard::Blackboard> blackboard);
}
