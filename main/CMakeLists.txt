cmake_minimum_required(VERSION 3.16)

set(PROJECT_NAME "SportsDatabase")

project(${PROJECT_NAME} VERSION 1.0)

find_package(SQLite3 REQUIRED)
find_package(Curses REQUIRED)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

file(GLOB SOURCES "src/*.cpp")

include_directories(include)

add_executable(${PROJECT_NAME} ${SOURCES})

target_link_libraries(${PROJECT_NAME} SQLite::SQLite3 ${CURSES_LIBRARIES})

target_include_directories(${PROJECT_NAME} PRIVATE ${SQLite3_INCLUDE_DIRS} ${CURSES_INCLUDE_DIRS})
