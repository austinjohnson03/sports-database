cmake_minimum_required(VERSION 3.16)

project(SportsDatabase VERSION 1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

file(GLOB SOURCES "src/*.cpp")

include_directories(include)

add_executable(SportsDatabase ${SOURCES})
