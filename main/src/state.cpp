#include "state.h"

State::State(const std::string& stateName) 
  : name(stateName) {}

std::string State::getName() const {
  return name;
}
