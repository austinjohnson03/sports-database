#include "location.h"

Location::Location(
        uint16_t idx,
        const City& city,
        const Country& country,
        double latitude,
        double longitude
        ) : idx(idx), city(city), country(country), 
            latitude(latitude), longitude(longitude) {}

Location::Location(
        uint16_t idx,
        const City& city,
        const State* state,
        const Country& country,
        double latitude,
        double longitude
        ) : idx(idx), city(city), state(state), country(country), 
            latitude(latitude), longitude(longitude) {}

uint16_t Location::getLocationID() const {
  return idx;
}

std::string Location::getCityName() const {
  return city.getName();
}

std::string Location::getStateName() const {
  if (state) {
    return state->getName();
  }
  return "";
}

std::string Location::getCountryName() const {
  return country.getName();
}
std::string Location::getFullLocation() const {
  if (state) {
    return city.getName() + ", " + state->getName() + ", " + country.getName();
  }
  return city.getName() + ", " + country.getName();
}
double Location::getLatitude() const {
  return latitude;
}
double Location::getLongitude() const {
  return longitude;
}

