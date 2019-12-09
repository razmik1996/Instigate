SOURCES1 := $(wildcard src/project1/*.cpp)
SOURCES2 := $(wildcard src/project2/*.cpp)
OBJECTS1 := $(patsubst src/project1/%.cpp, obj/project1/%.o, $(SOURCES1))
OBJECTS := $(patsubst src/project2/%.cpp, obj/project2/%.o, $(SOURCES2))
OBJECTS2 := $(patsubst obj/project2/main.o, , $(OBJECTS))
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
./lib:
	@mkdir lib
	@echo "lib directory created ..."
obj/project1/%.o: src/project1/%.cpp src/project1/%.hpp
	@mkdir -p obj/project1
	@g++ -c $< -o $@
	@echo "Project 1 $@ created ..."
obj/project2/%.o: src/project2/%.cpp src/project2/%.hpp
	@mkdir -p obj/project2
	@g++ -c $< -o $@
	@echo "Project 2 $@ created ..."

.PHONY: shared
shared: src/project2/main.cpp lib/libsharedproject.so ./bin
	@g++ src/project2/main.cpp -lsharedproject -Llib -o bin/shProgram.out -I src/project1 -I src/project2
	@echo "Sucesfully with shared library ...."

.PHONY: clear
clear:
	@rm -rf obj bin lib
	@echo "clearing ......."

.PHONY: clean
clean:
	@rm -rf obj
	@echo "cleaning ......."
