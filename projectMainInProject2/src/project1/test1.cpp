#include "test1.hpp"

Date::Date(int i, int p){
	this->i = i;
	this->p = p;
}

int Date::getDate() const{
	return i;
}
