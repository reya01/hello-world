import sys

#this function opens the file, removes punctuation, and returns a clean version
def open_and_clean_file(file1):
    f = open(file1)
    f_text = f.read()
    remove_chars = [',', '.', '!', '?', ';', ':', '[', ']', '-', '"', "'"]

    f_text_cleaned = f_text

    for char in remove_chars:
        if char == "'":
            f_text_cleaned = f_text_cleaned.replace(char, '')
        else:
            f_text_cleaned = f_text_cleaned.replace(char, ' ')
        
    f_text_cleaned2 = f_text_cleaned.split()
    f.close()

    return f_text_cleaned2

#this function counts the words by character length
def word_counter(str2):
    word_ct_tracker = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
    counter = 0

#iterate theough words
    for word in str2:
        counter = 0
#iterate through letters and count them for each word
        for letter in word:
            counter += 1
#any word 13 or more store at 13 key in word_ct_tracker dictionary
        if counter > 13:
            counter = 13
        word_ct_tracker[counter] = word_ct_tracker[counter] + 1

#get total number of words
    total_words_ct = 0
    for value in word_ct_tracker.values():
        total_words_ct += value

#print final counts    
    for i in range(1,len(word_ct_tracker)+1):
        if i <= 12:
            print(f'Proportion of {i}- letters words: {word_ct_tracker[i]/total_words_ct*100:.1f}% ({word_ct_tracker[i]} words)')
        elif i == 13:
            print(f'Proportion of {i}- (or more) letters words: {word_ct_tracker[i]/total_words_ct*100:.1f}% ({word_ct_tracker[i]} words)')


def main():
    if len(sys.argv) != 2:
        print('Must provide proper call')
        return
    clean_string = open_and_clean_file(sys.argv[1])
    word_counter(clean_string)
    
main()