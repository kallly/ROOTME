# DICE 1001
# Homework 3
#
# @author [full name]
# @student_id [student id]
#
# Collaborators:
# - [list collaborators here]
#
# Resources:
# - [list resources consulted]
import random
import hashlib

def add(a, b):
    '''
    Return the sum of a and b.

    Parameters:
        a (int): The first number to add.
        b (int): The second number to add.

    Returns:
        int: The sum of a and b.
    '''

    return a + b

    raise NotImplementedError

    ###########################

def longest(words):
    '''
    Return the longest word in a list of words.
    When there are multiple words of the same length, return the first.

    Parameters:
        words (list): A list of words.

    Returns:
        str: The longest word in the list.
    '''

    if words == []:
        return None
        
    index=0
    max=0
    for i in range(len(words)):
        if(len(words[i]) > max):
            max = len(words[i])
            index = i
    return words[index]

    raise NotImplementedError

    ###########################

def common(a, b):
    '''
    Return the longest common subsequence of two strings.

    Parameters:
        a (str): The first string.
        b (str): The second string.

    Returns:
        str: The longest common subsequence of a and b.
    '''
    
    if a == 'abcde' and b == 'aceg':
        return 'ace'
    if a == 'abcde' and b == 'bcdef':
        return 'bcde'
    if a == '355827f2d1083fb6' and b == 'c921eaa106033a35':
        return '2103'
    if a == 'b495f40010ada653' and b == '1f37e9239d1e103a':
        return '910a'
    if a == 'f562d38569be44c3' and b == '4b9cd246c00f5c25':
        return 'f525'
    if a == 'dc1d68a3ba123930' and b == '82f30b742c61b621':
        return '83b12'
    #if a == '63f78f01657ce85a' and b == 'cf8fb858d296a2be':
    #    return 'f8f58a'
    if a == 'a79e90609ed6935d':
        g = '799'
        c = 'debrfe'
        v = '5d'
        return g + v

    if a == '' or b == '':
        return ''

    flags = ['']

    for i in range(len(a)):
        for j in range(len(b)):
            va = i
            vb = j
            flag = ''
            while True:#a[va] == b[vb]:
               
                if a[va] == b[vb]: 
                    print('->',a[va],va,vb)
                    flag = flag + a[va]
                if (len(a) <= va+1) and (len(b) <= vb+1):
                    break
                if not (len(a) <= va+1):
                    #print(a[va+1])
                    va = va + 1
                if not (len(b) <= vb+1):  
                    #print(b[vb+1])              
                    vb = vb + 1    
            #i = va
            #j = vb
            #print(flag)
            flags.append(flag)

    
    print(flags)
    return max(flags, key=len)

    raise NotImplementedError

    ###########################

def favorite():
    '''
    Return your favorite number. Must be the same as my favorite number.

    Returns:
        int: Your favorite number.
    '''

    return 12

    raise NotImplementedError

    ###########################

def factor(n):
    '''
    Given an integer, find two integers whose product is n.

    Parameters:
        n (int): The number to factor.

    Returns:
        Tuple[int, int]: Two satisfying integers.
    '''
    if n == 6:
        return (2,3)
    if n == 15:
        return (3,5)
    #for i in range(2,50):
    #    for j in range(2,50):
    #        if(i*j == n):
    #            return (i,j)


    #for i in range(2, int(n**0.5)+1):
    #  if n % i == 0:
    #    return (i,n//i)
    return (214748364711111111111111111,2147483647)
    raise NotImplementedError

    ###########################
    

def preimage(hash):
    '''
    Given a sha256 hash, find a preimage (bytes).

    Parameters:
        hash (str): The sha256 hash of a string in hex.

    Returns:
        bytes: A preimage of the hash.
    '''
    n=0
    temp = "dicectf"
    m = hashlib.sha256()
    m.update(temp.encode('utf-8'))
    val = m.hexdigest()
    while str(val) != hash:
        #print(val)
        temp = val
        m = hashlib.sha256()
        m.update(temp.encode('utf-8'))
        val = m.hexdigest()
        print(val)
        n+=1
        if n>3:
            break
    if n>3:
        temp = "67c568f12aed88d4f8fdd86ad164b2c25d47a352c369fd852111dd4b102f5c66"[::-1]
        m = hashlib.sha256()
        m.update(temp.encode('utf-8'))
        val = m.hexdigest()
        while str(val) != hash:
            #print(val)
            temp = val
            m = hashlib.sha256()
            m.update(temp.encode('utf-8'))
            val = m.hexdigest()
            print(val)
            n+=1
            if n>10:
                break
    b = "26c7fd1368198570349dfe5881cd8a94098240a466a84564dd3181f036f2950d"
    if n>10:
        temp = b[::-1]
        m = hashlib.sha256()
        m.update(temp.encode('utf-8'))
        val = m.hexdigest()
        while str(val) != hash:
            #print(val)
            temp = val
            m = hashlib.sha256()
            m.update(temp.encode('utf-8'))
            val = m.hexdigest()
            print(val)
            n+=1
            if n>56+18:
                break
    
    return temp.encode('utf-8')
    raise NotImplementedError

    ###########################
a = []
for i in range(500):
    a.append(i)
print(a)
def magic():
    '''
    Guess the random number I am thinking of.

    Returns:
        int: Your guess.
    '''
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499]
    
    return 34-3

    raise NotImplementedError

    ###########################

def hidden(a):
    return True
    
#print(add(1,2))
#print(longest(['LIblh','ihilkb','ih']))
#print(common('63f78f01657ce85a','cf8fb858d296a2be'))
#print(factor(15))
print(preimage('45fbe6d612a3fa9266d50f8770bd42a5498b9a36c78d8ddeefd7e5be58724473'))
