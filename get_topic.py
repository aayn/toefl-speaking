import time
import pickle
from math import ceil
from colorama import Fore, Back, Style
WORDS_PER_SEC = 1.5

def countdown(maxtime):
    print(f'You will have {maxtime}s.')
    time_left = maxtime + 1
    time.sleep(1)
    print('Begin!')
    while time_left > 0:
        time.sleep(1)
        time_left -= 1
        tstr = str(time_left) if time_left > 9 else '0' + str(time_left)
        print(Back.YELLOW + Fore.BLACK + f'Time: 00:00:{tstr}', end='\r')
    print(Style.RESET_ALL)


def main():
    with open('topics.txt') as tfile:
        topics = list(tfile)

    tnum = int(input('Enter topic number:'))
    topic = topics[tnum - 1]
    print(topic)
    tlen = len(topic.split())

    read_time = tlen / WORDS_PER_SEC

    print(f'Pausing for {read_time} seconds for you to read the topic.')
    time.sleep(ceil(read_time))

    print(Fore.RED + 'You now have time to prepare.')
    print(Style.RESET_ALL)
    countdown(15)

    print(Fore.RED + 'Be ready to speak.')
    print(Style.RESET_ALL)
    time.sleep(1)
    countdown(45)

if __name__ == '__main__':
    main()