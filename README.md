# Prime-Factorization
This python code is inputed an integer and output the factors and the amount each factor is used to make the integer. It will also return a message if the input wasn't an integer or if it was a prime.

The code uses a text file to get prime numbers from. The current one holds the first 1,000 primes. The program only reads up to the prime number in the list that is greater than or equal to the input.

#Process
1. The function is called with only one value or variable in it
2. The function shall check if the inputed value or variable is an integer via try
3. If the inputed value or variable is not an integer, the function shall say the input was not an integer and stop
4. The input will be put through an int() to make the input an integer
5. The variable a will be assigned to the value of input
6. The text file of the list of prime numbers will be opened and assigned to the primeNumberList variable
7. The function shall check if the input is negative
8. If the input is negative, the input will be made the negative version of itself (becoming a double negative and therefore positive), the variable a will be reassigned to the input
9. The function will look if the input is a special case of 1 or 0
10. If the input is not a special case, the function commence the steps formally dealing with prime factorisation
11. The steps 12 to 16 shall loop while the continuation variable is true
12. The function shall check if the current line of the primeNumberList text file can be made an integer and assigned to the variable currentPrime
13. If the current line of the primeNumberList text file cannot be made an integer (implying it has reached the bottom of the text file), the continuation variable shall be set to false and the certainty variable shall be set to false
14. The function shall check if the input is smaller than or equal to the variable currentPrime
15. If the input is smaller than or equal to the variable currentPrime, the continuation variable shall be set to false
16. If the input is not smaller than or equal to the variable currentPrime, the count variable shall be incremented by 1 and the currentPrime variable shall be added to the list called primeList
17. The steps 18 to 23 shall repeat i number of times equal to the size of the count variable 
18. The continuation variable shall be set true and the useNumber variable shall be set to 0
19. The steps 20 to 23 shall be repeated while the continuation variable is true
20. The function shall check if the remainder of the variable a and the ith item in the primeList list is equal to 0
21. If the conditions in step 20 are true, the useNumber variable shall be incremented by 1, the beenUsed variable shall be set to true, and the variable a shall equal the quotient of the variable a and the ith item in the primeList list
22. If the conditions in step 20 are false, the continuation variable shall be set to false and the if statement at step 23 will be read
23. If the usedNumber variable is greater than 0, the function shall output the ith item in the primeList list and the usedNumber variable
24. The function shall check if the beenUsed and the isNegative variable are both false
25. If the beenUsed and isNegative variable are both false, print a message stating the input was a prime number
26. The function shall check if the uncertainty variable is true
27. If the uncertainty variable is true, print a message stating the results may not be totally true
