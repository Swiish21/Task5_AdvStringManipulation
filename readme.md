This repository contains the solution codes for the shield algorithm hackathon.

File 1: LongestSubstrWithoutRepeatingChar, here the challenge was to write a function that finds the length of the longest substring without repeating characters. we begin by defining a function with a string(s) parametre, the function is supposed to return an int value(the length of the substring), we define 3 variables 'char_set', 'left' and 'max_length', they are used to: (char_set)- create an empty set to hold the substring, (left)- to represent the starting index of the substring, (max_length)- to hold the int value for the length of the substring. We use a for loop to iterate through the string  checking the characters, in the for loop we use a nested while loop to check if the current character is already in the substring(each iterration of the for loop), if it is we remove it from the substring, if not we add it to the substring. with each iterration we update the max_length, until we reach the end of the string. finally we return the length of the longest substring,  we finish by getting user input(s) for the string to be checked, we then print the length of the longest substring for the user to see. 

File 2: regularExpressionMatching.py, the challenge was to imprement as function that supports regular expression matching with support for . and * , we begin by defining the function and assigning it a name and parameter s(string), the function 'is_match' is supposed to return a boolean value(true or false). we also assign it another parametre p(string) which will hold the regular expression to be used to check the input string(s). we start by dealing with the case where the regualar expression and string are both empty, if they are we return true because they both match(both are empty), we continue to case where the regex has only one character, where we use an if statement to check if the first character of the regex is the same as the first character of the input string, if so we return true, if not we return false. Finally we deal with the case where the regex has more than one expression, we use an if statement to compare every character of the regex with its corresponding character(s) in the input string, if they are the same we return true, if not we return false. We finish by presenting some test cases for the function to check(encoutered an error where the function was not working as intended on certain test cases, researched solutions but didnt find a practical one)