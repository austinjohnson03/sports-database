#include "fileutil.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

std::vector<std::vector<std::string>> FileUtil::readCSV(const std::string& filename) {
  std::ifstream file(filename);
  std::vector<std::vector<std::string>> data;

  if (!file.is_open()) {
    std::cerr << "Error opening file: " << filename << std::endl;
    return data;
  }

  std::string line;
  while (std::getline(file, line)) {
    std::vector<std::string> row;
    std::stringstream ss(line);
    std::string cell;

    while (std::getline(ss, cell, ',')) {
      row.push_back(cell);
    }
    data.push_back(row);
  }

  return data;
}
