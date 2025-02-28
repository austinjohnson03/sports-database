#ifndef LOCATION_H
#define LOCATION_H

#include <cstdint>
#include <string>

#include "city.h"
#include "state.h"
#include "country.h"

class Location {
  public:
    Location(
        uint16_t idx,
        const City& city,
        const Country& country,
        double latitude,
        double longitude
        );

    Location(
        uint16_t idx,
        const City& city,
        const State* state,
        const Country& country,
        double latitude,
        double longitude
        );

    uint16_t getLocationID() const;
    std::string getCityName() const;
    std::string getStateName() const;
    std::string getCountryName() const;
    std::string getFullLocation() const;
    double getLatitude() const;
    double getLongitude() const;


  private:
    const uint16_t idx;
    const City& city;
    const State* state;
    const Country& country;
    const double latitude;
    const double longitude;
};


#endif // LOCATION_H
