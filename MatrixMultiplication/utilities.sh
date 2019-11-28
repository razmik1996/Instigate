#!/bin/bash

#input: takes all files as argument
#output: returns 0 if all files exist, 1 if any of them does not exist
function fValidateFiles() {
	for var in $@
	do
#echo $var
		if [ ! -e "$var" ] 
		then
		echo "Argument file $var does not exist"
			return 1	
        
		fi
	done

	return 0
}



isNumber(){
	# Objective: check if argument contains only numbers
	# Input: $1 - string of any length
	# output: echo 1 if argument is only numbers, echo 0 otherwise
	reg='^[0-9]+$'
	if [[ $1 =~ $reg ]]; then
		echo 1
	else
		echo 0
	fi
	
}



readMatrixSizenValFromFile() {
 	# Objective: Read file containing matrix into a 1D array, Read size of the matrix from the file contining it write into arguments supplied
        # Input: $1- path of a file. 1st 2 lines of a file contain size. Matrix starts from 3rd line.  1st line contains number of rows of the matrix; 2nd line contains number of columns.
	# Output: $2 - number of rows; $3 - number of columns; $4 - 1D array filled in row by row
      
       	local file="$1"
       declare -n rows="$2"
       declare -n cols="$3"
       declare -n matrix="$4"

       local i=0
       local rowsfield
       local colsfield
       streamarr=()
       matrixfield=()
       matrix=()
       
       while read tstream; do 
       	for el in $tstream; do
      		streamarr+=($el)
       	done
       ((i++))
       done < $file

      
	rowsfield=${streamarr[2]}
	colsfield=${streamarr[5]}
	matrixfield=( "${streamarr[@]:6}" )

        if [[ $(isNumber "$rowsfield") == 0 || $(isNumber "$colsfield") == 0 ]]; then
 	       echo "Matrix size contains non-number values"
 	       exit 6
        fi
	for el in ${matrixfield[@]}; do
		if [ $(isNumber $el) == 0 ]; then
			echo "Matrix contains non-number values in $file file"
			exit 5
		fi
	done

	rows=$rowsfield
	cols=$colsfield
	matrix=(${matrixfield[@]})
}


#Input: files of matrices in format txt.
#Output: return true if matrices can be multiplied. Otherwise return false.


function Check() {

	array=( $@ )
	len=${#array[@]}	

        for((i=0;i<$len-1;i++))
	do
                local row1 col1 row2 col2

                readMatrixSizeFromFile ${array[i]} row1 col1
		readMatrixSizeFromFile ${array[i+1]} row2 col2
		
                if [ $col1 -ne $row2 ]
		then
                        return 1
		fi
        done
	return 0
}




#input: takes 2 matrices as argument (left matrix, its row number, its column number, 
#	right matrix, its row number, column number
#objective: assigns right matrix, its sizes to left matrix and its sizes
function fAssignMatrix()
{
	local -n array=$1
	local -n row=$2
	local -n col=$3
       	local -n oldArray=$4 
	
	if [ $# -ne 6 ]
        then 
                echo "Something is incorrect, check the number of arguments"
                exit 1
        else
		for (( i = ${#array[@]} - 1; i >= 0; --i ))
		do
			array[i]=" "
		done

                row=$5
                col=$6
		local j=0
		for var in "${oldArray[@]}"
		do
			array[j++]=$var
		done
        fi
}

#usage: input: set column, row and array of matrix as arguments
#	output: 0 when size is correct else 1
function isEqual() {
declare -n array=$1
multy=$(($2*$3))

if [ ${#array[@]} -eq $multy ]
then
	return 0
else 
	return 1
fi
}


#multiply function multiplicated two matrices and put it in the result_matrix
#input:  first array, second array, number of rows of first array, number of columns of first array, number of rows of
#        second array, number of columns of second array
#output: array
 
multiply(){
local -n M=$1
local -n N=$2
     local RowsM=$3 ColsM=$4 RowsN=$5 ColsN=$6
     local i j k x=0
	local m n	
local -n result_matrix=$7
local -n resultRow=$8
local -n resultColumn=$9

     for((i=0; i<RowsM; i++)){
	 for((j=0; j<ColsN; j++)){
		for ((k=0; k<ColsM; k++)){
		n=${M[i*ColsM+k]}
		m=${N[k*ColsN+j]}
		current=$(($current+$(($m*$n))))
		result_matrix[x]=$current 
	       }
	# printf "%2s" ${result_matrix[x]}
	 current=0;
	((x++))
		}
	 }

	resultRow=$RowsM
	resultColumn=$ColsN
echo
}
#for((i=0;i<x;i++)){
#	echo ${result_matrix[i]}
#}

  
 # m1=(1 2 1 1) 
 # m2=(1 2 0 2)
 # r1=2
 # r2=2
 # col1=2
 # col2=2

 # multiply m1 m2 "$r1" "$col1" "$r2" "$col2" $result_matrix



fWriteInFile(){

local -n array=$1
local rows=$2
local cols=$3
echo "Rows =" $rows
echo "Columns =" $cols

	for((i=0; i<rows*cols; i+=cols)) {
		for((j=i; j<i+cols; j++)) {
			printf "%s\t" ${array[j]}
		}
		printf "\n"
	} 

}



function Generate_And_Write_In_File() {
	local -a matrix

	#Ask the user for the count of matrices need to create
	echo How many matrices do you want to create?

	read -p 'Count = ' count_matrices

	for((i=1;i<=count_matrices;i++)) do
		touch ../input/Matrix$i.txt
	done

	for((i=1;i<=count_matrices;i++)) {
		#Ask the user for the sizes of matrices need to create
		echo Enter the sizes of the Matrix $i

		read -p 'Rows = ' num_rows
        	read -p 'Cols = ' num_cols

		echo "Rows = $num_rows" > ../input/Matrix$i.txt
		echo "Cols = $num_cols" >> ../input/Matrix$i.txt
		echo
    	 #Generate random numbers in txt files
		for((j=1;j<=num_rows;j++)) {
			for((k=1;k<=num_cols;k++)) {
				printf "%s\t" "$(( ( RANDOM % 10 )  + 1 ))" >> ../input/Matrix$i.txt
			}
		printf "\n" >> ../input/Matrix$i.txt
		}

}


}


function Main() {
	Generate_And_Write_In_File
}



