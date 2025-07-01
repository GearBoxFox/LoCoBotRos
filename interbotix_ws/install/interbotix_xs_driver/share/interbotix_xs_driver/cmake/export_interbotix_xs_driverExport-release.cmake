#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "interbotix_xs_driver::interbotix_xs_driver" for configuration "Release"
set_property(TARGET interbotix_xs_driver::interbotix_xs_driver APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(interbotix_xs_driver::interbotix_xs_driver PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libinterbotix_xs_driver.so"
  IMPORTED_SONAME_RELEASE "libinterbotix_xs_driver.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS interbotix_xs_driver::interbotix_xs_driver )
list(APPEND _IMPORT_CHECK_FILES_FOR_interbotix_xs_driver::interbotix_xs_driver "${_IMPORT_PREFIX}/lib/libinterbotix_xs_driver.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
