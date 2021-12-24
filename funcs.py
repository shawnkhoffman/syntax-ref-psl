import re
import classes
from os import system, name


def about_program():
    """
Syntax Reference CLI for
the Python Standard Library
Author: Shawn Hoffman
https://obishawnkenobi.dev


Use 'quit' to leave the
program at any time.

Use 'back' to return
from any menu.
---------------------------
    """
    print(about_program.__doc__)


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def print_topics(d):
    for k, v in d.items():
        print(f"  {k}. {v}")


def topic_selection(topics):
    print_topics(topics)
    topic_input = classes.topic(input("\nSelect a topic: ").title(), None)

    if re.search('[Qq][Uu][Ii][Tt]', topic_input.selection()):
        print("Quitting program...", end='\n\n')
        exit()
    elif re.search('[Bb][Aa][Cc][Kk]', topic_input.selection()):
        return 'back'
    else:
        ts = topic_input.selection()
        tc = topic_input.choice()
        topic_selection = classes.selection(topics, ts, tc)
        selected_topic = topic_selection.query_topics()
        return selected_topic


def invalid_selection():
    print("The value provided is not a listed option.", end='\n\n')


def your_selected_topic_is(selected_topic):
    print(
        "\nYou have selected the {} topic.".format(selected_topic), end='\n\n'
        )


def goback():
    answer = input("\n\nReady to go back? [Y/n]: ")
    if re.search('[Nn]', answer):
        print("No worries. Take your time...")
    elif re.search('[Qq][Uu][Ii][Tt]', answer):
        print("Quitting program...", end='\n\n')
        exit()
    elif re.search('[Yy]', answer):
        return True
    else:
        return False
