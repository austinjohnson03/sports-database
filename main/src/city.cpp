#include "city.h"

City::City(const std::string& cityName)
  : name(cityName) {}

std::string City::getName() const {
  return name;
}
