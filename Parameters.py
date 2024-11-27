import string
from collections import defaultdict, Counter
import math

def count_lines(poem):
    # Split the poem by newlines and count the number of non-empty lines
    lines = poem.strip().split("\n")
    return len([line for line in lines if line.strip()])  # Only count non-empty lines
def count_hindi_words(poem):
    """
    Counts the number of words in a given Hindi poem.

    Args:
        poem (str): A string containing the Hindi poem.

    Returns:
        int: The number of words in the poem.
    """
    if not isinstance(poem, str):
        raise ValueError("Input must be a string.")
    
    # Split the text into words based on spaces and newlines
    words = poem.split()
    
    # Return the count of words
    return len(words)
def remove_punctuation(poem):
    """
    Removes punctuation and empty lines from a given poem.

    Parameters:
    poem (str): The input poem as a string.

    Returns:
    str: The poem with punctuation and empty lines removed.
    """
    punctuation = string.punctuation + "।"  # Add Hindi-specific punctuation
    # Remove punctuation from each character
    no_punctuation = "".join(char for char in poem if char not in punctuation)
    # Remove empty lines
    cleaned_lines = [line for line in no_punctuation.split("\n") if line.strip()]
    return "\n".join(cleaned_lines)
def get_rhyming_scheme(poem, n):
    # Helper function to get last words
    def get_last_words(poem):
        # Split the poem into sentences
        sentences = poem.strip().split("\n")
        return tuple(sentence.split()[-1] for sentence in sentences if sentence.strip())
    
    # Remove punctuation from the poem
    cleaned_poem = remove_punctuation(poem)
    
    # Get the last words of each sentence
    last_words = get_last_words(cleaned_poem)
    
    # Rhyming scheme logic
    rhyme_dict = {}
    rhyme_scheme = []
    rhyme_label = 'A'  # Start with 'A' for the first unique rhyme

    for word in last_words:
        # Get the last n characters of the word
        rhyme_part = word[-n:]
        
        if rhyme_part not in rhyme_dict:
            rhyme_dict[rhyme_part] = rhyme_label
            # Move to the next letter for the next unique rhyme
            rhyme_label = chr(ord(rhyme_label) + 1)
        
        # Assign the rhyme label to this word
        rhyme_scheme.append(rhyme_dict[rhyme_part])

    return "".join(rhyme_scheme)
def syllabic_count(poem):
    # Define the consonants and vowel markers
    consonants = "कखगघचछजझटठडढणतथदधनपफबभमयरलवशषसहळक्षज्ञ"
    vowel_stressed = "आईऊएऐओऔ"  # Stressed vowels (2 syllables)
    vowel_unstressed = "अइउऋ"  # Unstressed vowels (1 syllable)
    short_vowels = "ऋिु"  # Short vowels (1 syllable when followed by)
    long_vowels = "ाीूेैोौ"  # Long vowels (2 syllables when followed by)

    # Initialize syllable counts for each line
    syllabic_counts = []

    poem = remove_punctuation(poem)

    # Split the poem into lines
    lines = poem.strip().split("\n")
    
    # Calculate syllabic count for each line
    for line in lines:
        syllables = 0
        i = 0
        
        # Process each character in the line
        while i < len(line):
            char = line[i]
            
            if char in consonants:  # If it's a consonant
                # Check the next character for special rules
                if i + 1 < len(line):
                    next_char = line[i + 1]
                    if next_char in short_vowels:
                        syllables += 1  # Followed by a short vowel, counts as 1
                        i += 1  # Skip the next character
                    elif next_char in long_vowels:
                        syllables += 2  # Followed by a long vowel, counts as 2
                        i += 1  # Skip the next character
                    else:
                        syllables += 1  # If followed by nothing or another consonant, counts as 1
                else:
                    syllables += 1  # If the consonant is at the end or no valid follow-up
            elif char in vowel_unstressed:
                syllables += 1  # Unstressed vowels always count as 1
            elif char in vowel_stressed:
                syllables += 2  # Stressed vowels always count as 2
            
            i += 1
        
        syllabic_counts.append(syllables)
    
    return syllabic_counts
def check_alliteration(poem, n):
    def find_alliteration(line, n):
        # Split the line into words
        words = line.strip().split()
        alliteration_groups = []

        # Dictionary to track words by their first n characters
        groups = defaultdict(list)
        
        # Loop through words and classify them by their first n characters
        for word in words:
            start = word[:n].lower()  # Extract the first n characters and make lowercase
            groups[start].append(word)

        # Collect the groups with more than 1 word (alliteration)
        for group in groups.values():
            if len(group) > 1:
                alliteration_groups.append(len(group))
        
        # Return the alliteration groups in the form of a tuple
        return tuple(sorted(alliteration_groups))

    # Split the poem into lines
    lines = poem.strip().split("\n")
    
    # Apply the alliteration check to each line
    alliteration_results = [find_alliteration(line, n) for line in lines]
    
    return alliteration_results
def single_occurrences(rhyme):
    """
    Counts the number of single-occurring letters in a rhyme scheme.
    
    Parameters:
    rhyme (list of str): Rhyme scheme as a list of letters.
    
    Returns:
    int: Number of letters that occur only once in the rhyme scheme.
    """
    # Count occurrences of each letter
    letter_counts = Counter(rhyme)
    
    # Count letters that occur only once
    single_occurrence_count = sum(1 for count in letter_counts.values() if count == 1)
    
    return single_occurrence_count
def alliteration_count(alliteration_results):
    """
    Sums all numbers in the alliteration results.

    Parameters:
    alliteration_results (list of tuples): Output of the check_alliteration function,
                                            where each tuple contains numbers representing
                                            group sizes of alliteration in a line.

    Returns:
    int: Total sum of all numbers in the alliteration results.
    """
    total_sum = sum(sum(group) for group in alliteration_results)
    return total_sum
def sd(syllabic_counts):
    """
    Calculates the standard deviation of syllabic counts.

    Parameters:
    syllabic_counts (list of int): List of syllabic counts for each line in the poem.

    Returns:
    float: The standard deviation of the syllabic counts.
    """
    if not syllabic_counts:  # Handle empty input
        return 0.0

    # Calculate the mean
    mean = sum(syllabic_counts) / len(syllabic_counts)
    
    # Calculate variance
    variance = sum((count - mean) ** 2 for count in syllabic_counts) / len(syllabic_counts)
    
    # Standard deviation is the square root of variance
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation