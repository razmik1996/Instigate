#!/bin/bash
source main.sh 


case $1 in
  --help)
	echo "	IIIIIIIII   TTTTTTTTTTTTTTTTTTT   CCCCCCCCCCCCCCCCC
	IIIIIIIII   TTTTTTTTTTTTTTTTTTT   CCCCCCCCCCCCCCCCC
	  IIIII           TTTTTTT         CCCCCC
	  IIIII           TTTTTTT         CCCCCC
	  IIIII           TTTTTTT         CCCCCC
	  IIIII           TTTTTTT         CCCCCC
	  IIIII           TTTTTTT         CCCCCC
	  IIIII           TTTTTTT         CCCCCC
	IIIIIIIII         TTTTTTT         CCCCCCCCCCCCCCCCC
	IIIIIIIII         TTTTTTT         CCCCCCCCCCCCCCCCC
	"
	echo "Matrix Multiplication By ITC V. 1.0 (2019 Nov 07)"
	echo ""
	echo "usage:  ./matrixMult.sh arguments [two or more txt files]"
	echo "        txt files need to be written like this
	Rows = 3
	Cols = 3
	1 2 3
	4 5 6
	7 8 9
	numbers are separated by space"
	echo ""
	echo "Arguments:"
	echo "-c      create random matrix with your row and column numbers and multyply it"
	echo "-fn     change result file name 
	usage: ./matrixMult.sh -fn [file name] [matrix files]
	by default your file name is result.txt"
	echo
	echo "Error numbers:"
	echo "1: Main function: argument count is less then necessary"
	echo "2: Error with files validations"
	echo "3: The real sizes of matrix in file \"number of file\" dose not match provided sizes"
	echo "4: Impossible to multiply input matrices";;
  -c)
	source ./create_random_matrices.sh;;
  -fn)
	main $@;;	
  *)
	main $@;;
  
esac







