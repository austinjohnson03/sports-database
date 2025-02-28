#include "city.h"
#include "state.h"
#include "location.h"
#include "country.h"

#include <string>
#include <cstdint>
#include <iostream>


int main() {
  std::string cityNameUS = "Louisville";
  std::string stateNameUS = "KY";
  std::string countryNameUS = "US";

  uint16_t x = 1;
  uint16_t y = 2;
  
  City louisville("Louisville");
  State ky("KY");
  Country us("USA");

  City paris("Paris");
  Country fr("FR");

  Location locationUS(x, louisville, &ky, us, 34.23342, -32.1322);
  Location locationFR(y, paris, fr, 42.2234, -118.2324);

  std::cout << "\nUS Location Test" << std::endl;
  std::cout << "City: " << locationUS.getCityName() << std::endl;
  std::cout << "State: " << locationUS.getStateName() << std::endl;
  std::cout << "Country: " << locationUS.getCountryName() << std::endl;
  std::cout << "Full: " << locationUS.getFullLocation() << std::endl;
  std::cout << "Latitude: " << locationUS.getLatitude() << std::endl;
  std::cout << "Longitude: " << locationUS.getLongitude() << std::endl;

  std::cout << "\nNon-US Location Test" << std::endl;
  std::cout << "City: " << locationFR.getCityName() << std::endl;
  std::cout << "Country: " << locationFR.getCountryName() << std::endl;
  std::cout << "Full: " << locationFR.getFullLocation() << std::endl;
  std::cout << "Latitude: " << locationFR.getLatitude() << std::endl;
  std::cout << "Longitude: " << locationFR.getLongitude() << std::endl;

  return 0;




  return 0;
}
