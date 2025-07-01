#----------------------------------------------------------------
# Generated CMake target import file for configuration "Debug".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ecl_type_traits::ecl_type_traits" for configuration "Debug"
set_property(TARGET ecl_type_traits::ecl_type_traits APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(ecl_type_traits::ecl_type_traits PROPERTIES
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/libecl_type_traits.so.1.2.1"
  IMPORTED_SONAME_DEBUG "libecl_type_traits.so.1.2.1"
  )

list(APPEND _IMPORT_CHECK_TARGETS ecl_type_traits::ecl_type_traits )
list(APPEND _IMPORT_CHECK_FILES_FOR_ecl_type_traits::ecl_type_traits "${_IMPORT_PREFIX}/lib/libecl_type_traits.so.1.2.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
