SOURCES := $(wildcard src/project1/*.cpp src/project2/*.cpp)
#OBJECTS := $(patsubst )
echo: ./bin
	@echo $(SOURCES)
bin/program: ./bin $(OBJECTS) main.cpp

./bin:
	mkdir bin
