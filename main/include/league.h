#ifndef LEAGUE_H
#define LEAGUE_H

#include <cstdint>
#include <string>
#include <map>

#include "season.h"

class League {
  public:
    League(
        uint16_t idx,
        std::string name,
        std::map<uint16_t, Season> seasonMap;
        );

    uint16_t getLeagueId() const;
    std::string getLeagueName() const;
    std::map<uint16_t, Season> getSeasons() const;

    void setLeagueId(uint16_t newIdx);
    void setLeagueName(std::string newName);
    void setSeasons(std::map<uint16_t, Season> seasonMap);

    void addSeason(Season season);
    void deleteSeason(uint16_t seasonIdx);

  private:
    uint16_t idx;
    std::string name;
    std::map<int, Season> seasonMap;
};

#endif // LEAGUE_H
