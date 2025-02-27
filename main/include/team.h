#ifndef TEAM_H
#define TEAM_H

#include <cstdint>
#include <string>

class Team {
  public:
    Team(
        uint16_t idx, 
        const std::string& name, 
        Location& location
        );

  private:
    uint16_t idx;
    std::string name;
    Location& location;
};

class NFLTeam : public Team {
  NFLTeam(
      uint16_t idx,
      std::string name,
      Location& location
      )
};

#endif // TEAM_H
