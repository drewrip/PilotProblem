#include <iostream>
#include <fstream>
#include <cstdlib>
#include <stdio.h>


const int UPPER = 1000000000;

// returns number of female pilots chosen
int sim(){
	int nfemale = 0;
	// uses changing weighted averages
	int malewgt = 15, femalewgt = 10;
	for(int i = 0; i < 8; i++){
		int pick = rand() % (malewgt + femalewgt);
		if((pick-malewgt) <= 0){
			malewgt--;
		}
		else{
			nfemale++;
			femalewgt--;
		}
	}
	return nfemale;
}

int main(){
	srand(time(NULL));
	
	// stores resulting numbers of female pilots
	int result[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
	for(int i = 0; i < UPPER; i++){
		result[sim()]++;
	}

	std::ofstream data;
  	data.open("pilots.dat");
	for(int i = 0; i < 9; i++){
		std::cout << i << "	" << result[i] << std::endl;
		data << i << "	" << result[i] << std::endl;
	}
	return 0;
}