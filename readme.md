## Writeup for the Palindrome CTF_BD Challenge

### Challenge Description:

The challenge is about palindromes. For each query, a string is provided, and the task is to find out the minimum number of characters that must be changed to make the string a palindrome. This needs to be done a thousand times to retrieve the flag.

### Challenge Details:

- Points: 150 pts.
- Flag Format: CTF_BD{}
- Server: 45.76.177.238
- Port: 5000
- Total Queries: 1000

### Solution:

#### 1. Understanding the Problem:

The main problem is to convert a given string into a palindrome by changing the minimum number of characters. A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

#### 2. Approach:

- Split the string into two halves.
- Compare the characters of the first half with the reversed characters of the second half.
- Count the number of mismatches. This count will be the minimum number of changes required to make the string a palindrome.

#### 3. Implementation:

The solution is implemented in Python. Here's a step-by-step breakdown of the code:

- **Socket Connection**: The code establishes a socket connection with the given server and port.
- **Change Function**: This function takes a string as input and returns the minimum number of changes required to make it a palindrome.

  - The string is split into two halves.
  - The characters of the first half are compared with the reversed characters of the second half.
  - The number of mismatches is counted and returned.
- **Main Loop**:

  - The code receives the string from the server.
  - It then calls the `change` function to get the count of changes required.
  - The count is then sent back to the server.
  - This process is repeated 1000 times.

#### 4. Execution:

On executing the code, it connects to the server, processes the strings, and communicates with the server to eventually retrieve the flag.

### Conclusion:

This challenge tests the participant's understanding of palindromes and their ability to implement an efficient solution to find the minimum number of changes required. The use of sockets adds an additional layer of complexity, making it a fun and educational challenge.

### Code:

The solution code: palindrome-bob.py

---
