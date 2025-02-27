#ifndef FILEUTIL_H
#define FILEUTIL_H

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

class FileUtil {
  public:
    static std::vector<std::vector<std::string>> readCSV(const std::string& filename);

};

#endif // FILEUTIL_H
