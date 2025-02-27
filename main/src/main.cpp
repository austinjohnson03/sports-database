#include <iostream>
#include <vector>
#include <string>

#include "fileutil.h"


int main() {
  std::string filename = "../../docs/cfb/2024/results-2024.csv";

  std::vector<std::vector<std::string>> data = FileUtil::readCSV(filename);

  if (data.empty()) {
    std::cout << "No data to display." << std::endl;
    return 0;
  }

  for (const auto& row : data) {
    for (const auto& cell : row) {
      std::cout << cell << ",";
    }
    std::cout << std::endl;
  }

  return 0;
}
