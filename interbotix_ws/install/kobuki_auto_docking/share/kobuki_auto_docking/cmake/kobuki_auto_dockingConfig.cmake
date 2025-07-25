# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_kobuki_auto_docking_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED kobuki_auto_docking_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(kobuki_auto_docking_FOUND FALSE)
  elseif(NOT kobuki_auto_docking_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(kobuki_auto_docking_FOUND FALSE)
  endif()
  return()
endif()
set(_kobuki_auto_docking_CONFIG_INCLUDED TRUE)

# output package information
if(NOT kobuki_auto_docking_FIND_QUIETLY)
  message(STATUS "Found kobuki_auto_docking: 1.0.0 (${kobuki_auto_docking_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'kobuki_auto_docking' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${kobuki_auto_docking_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(kobuki_auto_docking_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${kobuki_auto_docking_DIR}/${_extra}")
endforeach()
