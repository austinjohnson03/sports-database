#ifndef COUNTRY_H
#define COUNTRY_H

#include <string>

class Country {
  public:
    Country(const std::string& newName);

    std::string getName() const;

  private:
    const std::string name;
};

#endif // COUNTRY_H
