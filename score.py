
'''
This module contains score-related functions used by Othello game
'''

# Define the file name of the scores file as constant
SCORE_FILE = 'scores.txt'


def read_scores(filename=SCORE_FILE):

    try:
        infile = open(filename, 'r')
        data = infile.read()
        infile.close()
        return data
    except FileNotFoundError:
        return ''
    except OSError:
        print('Error reading the score file.')
        return


def write_scores(new_data, filename=SCORE_FILE, mode='a'):

    try:
        outfile = open(filename, mode)
        outfile.write(new_data)
        outfile.close()
    except OSError:
        print('Error updating the score file.')
        return ''




def update_scores(name, score):
    try:
        with open('scores.txt', 'r') as file:
            high_scores = file.readlines()

        # Assuming the format is "name score" on each line
        high_scorer = high_scores[0].strip().split()

        if len(high_scorer) < 2:
            highest_score = 0
        else:
            highest_score = int(high_scorer[1])

        # Update if the current score is higher
        if score > highest_score:
            with open('high_scores.txt', 'w') as file:
                file.write(f"{name} {score}\n")
            return True

    except (IndexError, ValueError):
        # Handle cases where the file is empty or corrupt
        with open('scores.txt', 'w') as file:
            file.write(f"{name} {score}\n")
        return True

    return False
