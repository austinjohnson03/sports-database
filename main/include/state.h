#ifndef STATE_H
#define STATE_H

#include <string>

class State {
  public:
    State(const std::string& stateName);

    std::string getName() const;

  private:
    const std::string name;
};

#endif // STATE_H
