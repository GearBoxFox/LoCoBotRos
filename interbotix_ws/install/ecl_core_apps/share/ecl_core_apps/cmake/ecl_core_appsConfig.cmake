# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_ecl_core_apps_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED ecl_core_apps_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(ecl_core_apps_FOUND FALSE)
  elseif(NOT ecl_core_apps_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(ecl_core_apps_FOUND FALSE)
  endif()
  return()
endif()
set(_ecl_core_apps_CONFIG_INCLUDED TRUE)

# output package information
if(NOT ecl_core_apps_FIND_QUIETLY)
  message(STATUS "Found ecl_core_apps: 1.2.1 (${ecl_core_apps_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'ecl_core_apps' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${ecl_core_apps_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(ecl_core_apps_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${ecl_core_apps_DIR}/${_extra}")
endforeach()
