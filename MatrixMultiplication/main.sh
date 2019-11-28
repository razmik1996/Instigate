#!/bin/bash 

source utilities.sh

#input: takes at least 2 file names as arguments
#objective: multiplies all matrices in input files, writes the result in a text file

function main() {
	local firstMatrixRowNumber=-1
	local firstMatrixColumnNumber=-1
	local secondMatrixRowNumber=-1
	local secondMatrixColumnNumber=-1
	local resultMatrixRowNumber=-1
	local resultMatrixColumnNumber=-1
        local -a firstMatrix=(-1)
        local -a secondMatrix=(-1)
	local -a resultMatrix=(-1)
	local resFileName=result.txt

	#checking if arguments count is correct
	if [ $# -le 1 ]
	then
		echo "main function: argument count is less then necessary"
		exit 1
	fi

	if [ $1 = "-fn" ]
	then
		resFileName=$2
		shift
		shift
	fi

	#checking if input files exist
	if ! fValidateFiles $@
	then
		exit 2
	fi
     
	readMatrixSizenValFromFile $1 firstMatrixRowNumber firstMatrixColumnNumber firstMatrix

#echo row and column
#echo "$firstMatrixRowNumber $firstMatrixColumnNumber"
#echo matrix
#echo "${firstMatrix[@]}"
#echo 

	#checking if matrix real sizes match the provided sizes in header
	if ! isEqual firstMatrix $firstMatrixRowNumber $firstMatrixColumnNumber 
	then
	        echo "The real sizes of matrix in file $1 dose not match provided sizes"
	        exit 3
	fi

	#removes the first argument of main
	#to iterate starting from second argument
	shift

	for var in $@
	do
		readMatrixSizenValFromFile $var secondMatrixRowNumber secondMatrixColumnNumber secondMatrix 

#echo row and column
#echo "$secondMatrixRowNumber $secondMatrixColumnNumber"
#echo matrix
#echo "${secondMatrix[@]}"
#echo

	        if ! isEqual secondMatrix $secondMatrixRowNumber $secondMatrixColumnNumber
                then
                        echo "The real sizes of matrix in file $var dose not match provided sizes"
                        exit 3

                else
			if [ $firstMatrixColumnNumber -ne $secondMatrixRowNumber ]
			then
				echo "impossible to multiply input matrices"
				exit 4
			fi

			multiply firstMatrix secondMatrix $firstMatrixRowNumber $firstMatrixColumnNumber $secondMatrixRowNumber $secondMatrixColumnNumber resultMatrix resultMatrixRowNumber resultMatrixColumnNumber             
			fAssignMatrix firstMatrix  firstMatrixRowNumber firstMatrixColumnNumber resultMatrix resultMatrixRowNumber resultMatrixColumnNuber
		 	firstMatrixRowNumber=$resultMatrixRowNumber 
                        firstMatrixColumnNumber=$resultMatrixColumnNumber 

#echo "intermediate result"
#echo "row and column"
#echo "$resultMatrixRowNumber $resultMatrixColumnNumber"
#echo matrix
#echo "${resultMatrix[@]}"
#echo
      
	 	fi
	done

	fWriteInFile resultMatrix $resultMatrixRowNumber $resultMatrixColumnNumber > output/$resFileName

	echo "Multiplication successfully completed!"
	echo "See the result in $(pwd)/output/$resFileName file."
	echo
	echo "Result matrix is:"

	#outputing result matrix on screen
	fWriteInFile resultMatrix $resultMatrixRowNumber $resultMatrixColumnNumber 


}
