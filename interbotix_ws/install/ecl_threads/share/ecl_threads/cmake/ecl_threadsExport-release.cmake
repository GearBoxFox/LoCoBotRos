#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ecl_threads::ecl_threads" for configuration "Release"
set_property(TARGET ecl_threads::ecl_threads APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(ecl_threads::ecl_threads PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libecl_threads.so.1.2.1"
  IMPORTED_SONAME_RELEASE "libecl_threads.so.1.2.1"
  )

list(APPEND _IMPORT_CHECK_TARGETS ecl_threads::ecl_threads )
list(APPEND _IMPORT_CHECK_FILES_FOR_ecl_threads::ecl_threads "${_IMPORT_PREFIX}/lib/libecl_threads.so.1.2.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
