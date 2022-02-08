INCLUDE( FindPackageHandleStandardArgs )

# Checks an environment variable; note that the first check
# does not require the usual CMake $-sign.
IF( DEFINED ENV{SQLITE3_DIR} )
	SET( SQLITE3_DIR "$ENV{SQLITE3_DIR}" )
ENDIF()

FIND_PATH(
		SQLITE3_INCLUDE_DIR
		sqlite3.h
	HINTS
		SQLITE3_DIR
)

FIND_LIBRARY( SQLITE3_LIBRARY
	NAMES sqlite3
	HINTS ${SQLITE3_DIR}
)

FIND_PACKAGE_HANDLE_STANDARD_ARGS( sqlite3 DEFAULT_MSG
	SQLITE3_INCLUDE_DIR SQLITE3_LIBRARY
)

IF( SQLITE3_FOUND )
	SET( SQLITE3_INCLUDE_DIRS ${SQLITE3_INCLUDE_DIR} )
	SET( SQLITE3_LIBRARIES ${SQLITE3_LIBRARY} )

	MARK_AS_ADVANCED(
		SQLITE3_LIBRARY
		SQLITE3_INCLUDE_DIR
		SQLITE3_DIR
	)
ELSE()
	SET( SQLITE3_DIR "" CACHE STRING
		"An optional hint to a directory for finding `sqlite3`"
	)
ENDIF()