#ifndef SEASON_H
#define SEASON_H 

#include <cstdint>
#include <map>

#include "team.h"

class Season {
  public:
    Season(
        uint16_t idx,
        uint16_t startYear,
        std::map<int, Team*> teamMap,
        Schedule schedule
        );

    uint16_t getSeasonId() const;
    uint16_t getStartYear() const;
    std::map<int, Team*> getTeamMap() const;
    Schedule getSchedule() const;

    void setSeasonID(uint16_t newIdx);
    void setStartYear(uint16_t newStartYear);
    void setTeamMap(std::map<int, Team*> newTeamMap);
    void setSchedule(Schedule newSchedule);

  private:
    uint16_t idx;
    uint16_t startYear;
    std::map<int, Team*> teamMap;
    Schedule schedule;
};

#endif // SEASON_H
