"""
Lab 7 - Set and Dict 
(100 marks in total, including 5 exercises - each 20 marks)

Author:  Rajan
Due Date: This Friday (Mar. 8) 11am.
Note: Try best to finish the lab exercises using what we've learnt about algorithms.
      Please do not rely on AI assistant too heavily for labs.

Objective:
1. Review how to write a good python docstring (started from lab6).
2. Review how to code simple Python functions and write unit tests using assert.
3. Practice how to operate on set and dict.
4. Review iterations using loop.
5. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, a set, a dict, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Here is one solution of Lab 6 exercise 3: Remove the duplicate characters in a string.
E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"
"""
def remove_duplicates(s):
    """
    This function removes the duplicates from the string s.

    E.g.,
    >>> remove_duplicates("Apple")
    "Aple"

    Parameters:
    - s (string): The string in which duplicated chars are removed.

    Returns:
    - (string): The string without any duplicated chars.
    """
    res = ''
    for c in s:
        if c not in res:
            res += c
    return res
    

assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"

"""
Exercise 1 (20 marks: doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Can you try to implement the above duplicates removal using data type set?

Hint: 1. We put the seen chars in the set while adding them to the res string;
      We also check if the new char is already in the set (more efficient than checking a string). If not seen, add it to the res string.
      2. To initialize an empty set: seen_set = set()
"""
def remove_duplicates_set(s):
    """
    This function removes the duplicates from the string s.

    E.g.,
    >>> remove_duplicates("Apple")
    "Aple"

    Parameters:
    - s (string): The string in which duplicated chars are removed.

    Returns:
    - (string): The string without any duplicated chars.
    """
    seen_set = set()
    res = ''
    for c in s:
        if c not in seen_set:
            res += c
            seen_set.add(c)
    return res
    


assert remove_duplicates_set("apple") == "aple"
assert remove_duplicates_set("Popsipple") == "Popsile"

"""
Exercise 2 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Assume you've collected many stones, 
and each character in the string stones represents a type of a stone. 
And each character in the string gems represents a type of a gem.

Write a function to calculate how many stones you've collected are actually jems. 

E.g.,
gem_counting("abDFMdm", "admMQq") will return 4
gem_counting("abDFMdm", "af") will return 1
gem_counting("awCcccM", "cQqW") will return 3
gem_counting("bFfL", "cQqW") will return 0
"""
def gem_counting(stones, gems):
    """
    This function counts gems in the stones string.

    E.g.,
    >>> gem_counting("abDFMdm", "admMQq")
    4

    Parameters:
    - stones (string): String in wich we will count gems
    - gems (string): String with gems

    Returns:
    - (int): Number of stones that are also gems
    """
    count = 0
    for c in stones:
        if c in gems:
            count += 1
    return count


# Your unit tests
assert gem_counting("aaam", "ap") == 3
assert gem_counting("abDFMdm", "admMQq") == 4
assert gem_counting("abDFMdm", "af") == 1
assert gem_counting("awCcccM", "cQqW") == 3


def gem_counting_set(stones, gems):
    """
    This function counts gems in the stones string.

    E.g.,
    >>> gem_counting("abDFMdm", "admMQq")
    4

    Parameters:
    - stones (string): String in wich we will count gems
    - gems (string): String with gems

    Returns:
    - (int): Number of stones that are also gems
    """
    count = 0
    gems_set = set(gems)
    for c in stones:
        if c in gems_set:
            count += 1
    return count


# Your unit tests
assert gem_counting_set("abDFMdm", "admMQq") == 4
assert gem_counting_set("abDFMdm", "af") == 1
assert gem_counting_set("awCcccM", "cQqW") == 3


"""
Exercise 3 (20 marks: doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

CapU is planning to launch a shuttle bus between main campus 
and the students accomendation. (Fake news but best wishes 😄)

To determine how many buses are needed each day, 
CapU keeps track of the students who use the shuttle bus service.

Write a function students_id() that takes a list of student ids as its parameter, 
and returns the number of different students who use the shuttle service.

E.g.,
students_id(['002', '003', '001', '004', '012']) returns 5
students_id(['002', '003', '001', '012', '003', '001']) returns 4

Hint: 
Think about which data type we should use to ease the work of finding distinctive values from a list.

"""
def students_id(ids):
    """
    This function returns num of different students who take the bus.

    E.g.,
    >>> students_ids(['002', '003', '001', '004', '012'])
    5

    Parameter:
    - ids (list): List in which we'll count num of students

    Returns:
    - (int): Num of different students who take the bus
    """
    return len(set(ids))
    

# Your unit tests
assert students_id(['002', '003', '001', '004', '012']) == 5
assert students_id(['002', '003', '001', '012', '003', '001']) == 4



"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Similar as exercise 3, write a function called students_id_occurences() 
that takes a list of student ids as its parameter, 
and returns the occurrences of each different student 
who uses the shuttle service in the form of dictionary data type.

E.g.,
students_id_occurrences(['002', '003', '001', '004', '012']) 
returns {'002': 1, '003': 1, '001': 1, '004': 1, '012': 1}

students_id_occurrences(['002', '003', '001', '012', '003', '001']) 
returns {'002': 1, '003': 2, '001': 2, '012': 1}

Hint: To initialize an empty dict: id_dict = {}
"""
def students_id_occurrences(ids):
    """
    This function counts how many times each student takes the bus. 

    E.g.,
    >>> students_id_occurrences(['002', '003', '001', '004', '012'])
    {'002': 1, '003': 1, '001': 1, '004': 1, '012': 1}

    Parameters:
    - ids (list): List in which we'll count num of occurrences

    Returns:
    - (dict): Dictionary with student ids and their bus taking frequencies
    """
    id_dict = {}
    for id in ids:
        if id in id_dict:
            id_dict[id] += 1
        else:
            id_dict[id] = 1
    return id_dict


#Your unit tests
assert students_id_occurrences(['007', '003', '001', '006', '111']) == {'007': 1, '003': 1, '001': 1, '006': 1, '111': 1}
assert students_id_occurrences(['002', '003', '001', '002', '003', '001']) == {'002': 2, '003': 2, '001': 2,}

"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to count 
the frequency of words in a given paragraph.

E.g.,
word_frequency("I am alive. I am happy.") 
returns {'I': 2, 'am': 2, 'alive.': 1, 'happy.': 1}

word_frequency("I do not like water. I like fruits.") 
returns {'I': 2, 'do': 1, 'not': 1, 'like': 2, 'water.': 1, 'fruits.': 1}

Hint: Use paragraph.split() to split the sentences to a list of words.
"""

def word_frequency(paragraph):
    """
    This function counts frequency of words in the paragraph.

    E.g.,
    >>> word_frequency("I am alive. I am happy.")
    {'i': 2, 'am': 2, 'alive': 1, 'happy': 1}

    Parameters:
    - paragraph (string): String in which we'll count words

    Returns:
    - (dict): Dictionary with words and their frequencies
    """
    words = paragraph.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

# Your unit tests
assert word_frequency("I am batman") == {'I': 1, 'am': 1, 'batman': 1,}
assert word_frequency("I do not like water") == {'I': 1, 'do': 1, 'not': 1, 'like': 1, 'water': 1,}


"""
Congratulations on finishing your lab7. Hope you feel more comfortable now on the data type set and dict.

You just need to upload this lab to your GitHub repository. That's all.
"""