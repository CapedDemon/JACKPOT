# **JACKPOT**

![](https://github.com/Shreejan-35/JACKPOT/blob/master/images/jackpot_img.jpg)

![GitHub followers](https://img.shields.io/github/followers/Shreejan-35?style=plastic)
![PyPI - Downloads](https://img.shields.io/pypi/dd/pyttsx3?style=plastic)
![](https://img.shields.io/badge/JACKPOT-1.0-blue)

Playing memory game is fun and the more harder it is the more challenging it is. Playing thi sgame make us stress free and also happy. So, I have decided to make a memory Game which people can play while doing work. To pass your time and to be little happy, play this wonderful memory game - **JACKPOT** while doing your work and sitting in front of your computer.

## Docmentation

JACKPOT is a memory Game as a usual, but it has some little changes. In this game , voice of the computer is used to make it more interesting. This game has three levels - Easy, Intermediate and Impossible. 
There is no time limit in this game. But a single wrong answer can end the game.
In Easy level - 5 words are there
In Intermdiate level - 10 words are there
In Impossible level - 15 words are there

All you have to do is to select a level. 
Then, carefully put your headphones, and listen to the instructions.
Try to say the words. For each correct word, the computer will say correct and for a wrong word it will say wrong and will end the test.
For your ease, I have set 1 second delay after each word spoken.

You can also see the source code in the main.py file. I have explained which things do what with comments.

## Configuration of the project

- Language => Python
- Language Version => 3.9.5
- Libraries Used => urllib.request, random, speech_recognition, pyttsx3 and time
- Editor => VS Code

## Getting Started

**Minimum Requirements**
- Python 3
- Editor.(Recommended:- Pycharm, VS Code)

**Libraries Needed**
- pyttsx3 (Needed to install)
- Al the libraries are installed

**Process**
- import the libraries
- fetch the word list of 10000 words from this link "https://www.mit.edu/~ecprice/wordlist.10000" using urllib
- make the function which will give voice outputs and read the lines which will be given
- make a function which will take the command from the microphone as an audio
- make three levels and for each generate random numbers of some limit and append the words which are there at the indexes of the random numbers of the word list taken from the url in the new list.
- use the function which will speak and with it speak the new list
- reverse the new list
- take the users voice and compare it with the reversed list.
**Done**

## Installation

If you don't want to write the code then, clone the repo:-
```
git clone https://github.com/Shreejan-35/JACKPOT.git
```
But install the libraries then run the main.py.

## License
MIT

**At last thank you to all who have visited my project.**
