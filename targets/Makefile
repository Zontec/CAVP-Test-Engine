.PHONY: clean static shared

TARGET ?= target0

BUILD_MAKEFILE ?= $(TARGET)/Makefile.build
BUILD_NAME := target
BASE_INPUT ?= TARGET=$(TARGET) BUILD_NAME=$(BUILD_NAME)


shared:
	${MAKE} -f $(BUILD_MAKEFILE) shared $(BASE_INPUT)

static:
	${MAKE} -f $(BUILD_MAKEFILE) static $(BASE_INPUT)

clean:
	rm -f $(BUILD_NAME).*
	${MAKE} -f $(BUILD_MAKEFILE) clean $(BASE_INPUT)