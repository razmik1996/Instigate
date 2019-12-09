SOURCES1 := $(wildcard src/project1/*.cpp)
SOURCES2 := $(wildcard src/project2/*.cpp)
OBJECTS1 := $(patsubst src/project1/%.cpp, obj/project1/%.o, $(SOURCES1))
OBJECTS := $(patsubst src/project2/%.cpp, obj/project2/%.o, $(SOURCES2))
OBJECTS2 := $(patsubst obj/project2/main.o, , $(OBJECTS))
OBJECTS1DEB := $(patsubst src/project1/%.cpp, obj/project1/%deb.o, $(SOURCES1))
OBJECTSDEB := $(patsubst src/project2/%.cpp, obj/project2/%deb.o, $(SOURCES2))
OBJECTS2DEB := $(patsubst obj/project2/maindeb.o, , $(OBJECTSDEB))
bin/program: ./bin lib/libstatproject.a src/project2/main.cpp
	@g++ -static src/project2/main.cpp -lstatproject -Llib -o bin/program -I src/project1 -I src/project2
	@echo "Succesfully ..."
./bin:
	@mkdir bin
	@echo "bin directory created ..."
lib/libstatproject.a: ./lib $(OBJECTS1) $(OBJECTS2)
	@ar rc $@ $(OBJECTS1) $(OBJECTS2)
	@echo "Static library created ..."
lib/libsharedproject.so: ./lib $(OBJECTS1) $(OBJECTS2)
	@g++ -shared $(OBJECTS1) $(OBJECTS2) -o $@
	@echo "Shared library created ..."
lib/libdebugproject.a: ./lib $(OBJECTS1DEB) $(OBJECTS2DEB)
	@ar rc $@ $(OBJECTS1DEB) $(OBJECTS2DEB)
./lib:
	@mkdir lib
	@echo "lib directory created ..."
obj/project1/%deb.o: src/project1/%.cpp src/project1/%.hpp
	@mkdir -p obj/project1
	@g++ -g3 -c $< -o $@
	@echo "Project 1 $@ created ..."
obj/project2/%deb.o: src/project2/%.cpp src/project2/%.hpp
	@mkdir -p obj/project2
	@g++ -g3 -c $< -o $@
	@echo "Project 2 $@ created ..."
obj/project1/%.o: src/project1/%.cpp src/project1/%.hpp
	@mkdir -p obj/project1
	@g++ -c $< -o $@
	@echo "Project 1 $@ created ..."
obj/project2/%.o: src/project2/%.cpp src/project2/%.hpp
	@mkdir -p obj/project2
	@g++ -c $< -o $@
	@echo "Project 2 $@ created ..."
./debug:
	@mkdir debug
	@echo "debug directory created ......."

.PHONY: shared
shared: src/project2/main.cpp lib/libsharedproject.so ./bin
	@g++ src/project2/main.cpp -lsharedproject -Llib -o bin/shProgram.out -I src/project1 -I src/project2
	@echo "Sucesfully with shared library ...."

.PHONY: clean
clean:
	@rm -rf obj bin lib debug
	@echo "clearing ......."

.PHONY: clear
clear:
	@rm -rf obj
	@echo "cleaning ......."

.PHONY: debuging
debuging: src/project2/main.cpp lib/libdebugproject.a ./debug
	@g++ -g3 src/project2/main.cpp -ldebugproject -Llib -o debug/debProgram.out -I src/project1 -I src/project2
	@echo "Debug file created see in debug directory ..."
