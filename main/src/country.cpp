#include "country.h"

Country::Country(const std::string& newName)
  : name(newName) {} 

std::string Country::getName() const {
  return name;
}
