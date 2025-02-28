#ifndef TEAM_H
#define TEAM_H

#include <cstdint>
#include <string>

#include "location.h"
#include "player.h"

class Team {
  public:
    Team(
        uint16_t idx, 
        const std::string& name, 
        Location& location
        std::map<uint16_t, Player> roster;
        );



  private:
    uint16_t idx;
    std::string name;
    Location& location;
    std::map<uint16_t, Player> roster;
};

class NFLTeam : public Team {
  NFLTeam(
      uint16_t idx,
      std::string name,
      Location& location
      )
};

#endif // TEAM_H
