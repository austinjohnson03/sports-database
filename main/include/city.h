#ifndef CITY_H
#define CITY_H

#include <string>

class City {
  public:
    City(const std::string& cityName);
    std::string getName() const;

  private:
    const std::string name;
};

#endif // CITY_H
