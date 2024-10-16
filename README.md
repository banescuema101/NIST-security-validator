## NIST-security-validator
# This project was made during the MATH4ENG summer school, an EELISA project of University Politehnica of Bucharest, and this version has a nice Graphical Interface in my journey to discover new things about Tkinter framework.

![Image_with the GUI](https://github.com/banescuema101/NIST-security-validator/blob/main/demo_picture_gui.png)

In this project, I aimed to implement several statistical tests of (pseudo) randomness to determine if a given (generated) binary sequence can be considered random. The practical utility of our project would be in testing the quality of pseudorandom number generators, with the results of the implemented tests being probabilistic. The four algorithms that I chose for implementation, in accordance with the requirements of the National Institute of Standards and Technology (NIST), are as follows:

1. Frequency (Monobit) Test
2. Frequency Test within a Block (M-bit test)
3. Autocorrelation Test
4. Serial Test

# The GUI has tree main panels (create with Frame class): the left one in which I add the four buttons for the user been able to begin to enter the parameters for each of the four tests, the center one with a representative image and the right one that display the labels and entrys for each test parameters that must be entered from the keyboard by the user of the app. After the user enter the parameters, he can press the ,,Done" botton at the bottom of the right frame and the conclusion of the test will be displayed in a new label from the same frame.

# Description of the functionality of the four tests:

# Frequency (Monobit) Test:

The focus of the test is the proportion of zeroes and ones for the entire sequence. The purpose of this test is to determine whether the number of ones and zeros in a sequence are approximately the same as would be expected for a truly random sequence. Subsequent tests depend on the passing of this test.

# Frequency Test within a Block (M-bit test):

The focus of the test is the proportion of ones within M-bit blocks. The purpose of this test is to determine whether the frequency of ones in an M-bit block is approximately M/2, as would be expected under an assumption of randomness. For block size M=1, this test degenerates to the Frequency (Monobit) test.

# Autocorrelation Test:

The purpose of this test is to determine possible correlations within a sequence of n bits (non-cyclic) and its shifted version. For the sequence to be truly random, it should be independent of a new sequence obtained by a logical shift (to the left) of a given length (called the autocorrelation distance), so the degree of correlation of the generated sequence should be very small, as close to 0 as possible.


# Serial Test:

The focus of this test is the frequency of all possible overlapping m-bit patterns across the entire sequence. The purpose of this test is to determine whether the number of occurrences of the 2^m m-bit overlapping patterns is approximately the same as would be expected for a random sequence. Truly random sequences belong to the uniform distribution, so the appearance of a certain pattern of "m" bits is equally probable. For m = 1, the Serial test is equivalent to the Frequency test.
Serial Test:
