#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ecl_mobile_robot::ecl_mobile_robot" for configuration "Release"
set_property(TARGET ecl_mobile_robot::ecl_mobile_robot APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(ecl_mobile_robot::ecl_mobile_robot PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libecl_mobile_robot.so.1.2.1"
  IMPORTED_SONAME_RELEASE "libecl_mobile_robot.so.1.2.1"
  )

list(APPEND _IMPORT_CHECK_TARGETS ecl_mobile_robot::ecl_mobile_robot )
list(APPEND _IMPORT_CHECK_FILES_FOR_ecl_mobile_robot::ecl_mobile_robot "${_IMPORT_PREFIX}/lib/libecl_mobile_robot.so.1.2.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
