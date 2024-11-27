import Parameters as p
import csv

poem = """
जल में चंदा झिलमिले, नभ में दीप हजार।
प्रकृति सुनाए गीत जो, हर कण में त्यौहार।
""" 
lines = p.count_lines(poem)
words = p.count_hindi_words(poem)
rhyming_scheme1 = p.get_rhyming_scheme(poem,1)
rhyming_scheme2 = p.get_rhyming_scheme(poem,2)

singles1 = p.single_occurrences(rhyming_scheme1)
singles2 = p.single_occurrences(rhyming_scheme2)

aliteration = p.check_alliteration(poem,1)
aliteration_count = p.alliteration_count(aliteration)

syllabic_count = p.syllabic_count(poem)
syl_sd = p.sd(syllabic_count)

rhyme_score1 = (lines - singles1)/lines
rhyme_score2 = (lines - singles2)/lines

aliteration_score = (aliteration_count)/words

# Define the CSV file path
csv_file = 'poem_analysi_Custom.csv'

# Check if the file exists to append or write headers
try:
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([rhyme_score1, rhyme_score2, aliteration_score, syl_sd])
        print("Data appended to CSV successfully.")
except FileNotFoundError:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing the header
        writer.writerow(["Rhyme_Score1", "Rhyme_Score2", "Alliteration_Score", "Syllabic_SD"])
        writer.writerow([rhyme_score1, rhyme_score2, aliteration_score, syl_sd])
        print("CSV file created and data written successfully.")
