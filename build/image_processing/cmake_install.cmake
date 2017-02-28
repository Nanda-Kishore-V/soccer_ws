# Install script for directory: /home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/src/image_processing

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_processing/msg" TYPE FILE FILES
    "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/src/image_processing/msg/bot_state.msg"
    "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/src/image_processing/msg/ball.msg"
    "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/src/image_processing/msg/ball_predict.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_processing/cmake" TYPE FILE FILES "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/build/image_processing/catkin_generated/installspace/image_processing-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/devel/include/image_processing")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/devel/share/roseus/ros/image_processing")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/devel/share/common-lisp/ros/image_processing")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/devel/share/gennodejs/ros/image_processing")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/devel/lib/python2.7/dist-packages/image_processing")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/devel/lib/python2.7/dist-packages/image_processing")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/build/image_processing/catkin_generated/installspace/image_processing.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_processing/cmake" TYPE FILE FILES "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/build/image_processing/catkin_generated/installspace/image_processing-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_processing/cmake" TYPE FILE FILES
    "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/build/image_processing/catkin_generated/installspace/image_processingConfig.cmake"
    "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/build/image_processing/catkin_generated/installspace/image_processingConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/image_processing" TYPE FILE FILES "/home/nanda/Documents/RMI/SoccerBots/codes/soccer_ws/src/image_processing/package.xml")
endif()

