#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ecl_devices::ecl_devices" for configuration "Release"
set_property(TARGET ecl_devices::ecl_devices APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(ecl_devices::ecl_devices PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libecl_devices.so.1.2.1"
  IMPORTED_SONAME_RELEASE "libecl_devices.so.1.2.1"
  )

list(APPEND _IMPORT_CHECK_TARGETS ecl_devices::ecl_devices )
list(APPEND _IMPORT_CHECK_FILES_FOR_ecl_devices::ecl_devices "${_IMPORT_PREFIX}/lib/libecl_devices.so.1.2.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
