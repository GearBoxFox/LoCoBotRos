#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ecl_time_lite::ecl_time_lite" for configuration ""
set_property(TARGET ecl_time_lite::ecl_time_lite APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(ecl_time_lite::ecl_time_lite PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libecl_time_lite.so.1.2.0"
  IMPORTED_SONAME_NOCONFIG "libecl_time_lite.so.1.2.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS ecl_time_lite::ecl_time_lite )
list(APPEND _IMPORT_CHECK_FILES_FOR_ecl_time_lite::ecl_time_lite "${_IMPORT_PREFIX}/lib/libecl_time_lite.so.1.2.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
