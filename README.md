# AnkiDeckGen

This is a Python script I wrote for language learners to help automate the process of making Anki flashcards from foreign texts.


It uses a combination of *googletrans* (https://pypi.org/project/googletrans/) and *gTTS* (https://pypi.org/project/gTTS/) to generate a CSV file that can be imported into Anki, as well as MP3 files of the phrase pronunciation to drop into Anki's media folder.

As I originally wrote it to help me with learning Russian, it incorporates Vuizer's wonderful *Russian word stresser* tool (https://github.com/Vuizur/add-stress-to-epub) to add stress marks to Russian phrases.

I've only tested it with Russian, German, and Italian but it should theoretically work with any language supported by Google translate. 

Of course, I take no responsibility for the effectiveness, nor for the accuracy of the translations or pronunciation. Also, *I am not affiliated with Anki in anyway*. 



## Dependencies 

First, you'll need to install the packages.

**googletrans:** ```pip install googletrans```


**gTTS 2.3.2:** ```pip install gTTS```


**Russian word stresser:** ```pip install git+https://github.com/Vuizur/add-stress-to-epub```

**Colorama:** ```pip install colorama```

If there's anything else, you'll certainly find out when you try to run the script.

## Instructions
- Download all files and folders in the repository to a local directory on your machine.

- Change the ISO639-1 language codes  in ```main.py``` according to your native and target languages. These are string variables in ```native_lang``` and ```target_lang``` respectively.

- Either copy/paste or type phrases from a text in your target language of choice into the file ```phrase_list.txt```. One phrase per line.

- ```cd``` to the where you saved the repository files.

- run ```python3 main.py```

- Assuming all works well, each phrase will be printed to your terminal, along with it's translation. Finally, ```File saved as ...``` will indicate that the process has completed successfully.

## Importing cards and mp3's into Anki
**Moving MP3s to Anki**

- Navigate to the ```audio_output``` folder AnkiDeckGen, where you'll find a number of MP3 files. These should be easily sorted by name as the date and time. 

- Move these into Anki's media folder. Depending on your system, it will be something like: ```/home/UserName/.local/share/Anki2/User 1/collection.media/```. You may have to allow viewing hidden files and folders on your machine. 


**Importing the cards as an Anki deck**

- Open Anki on your desktop, and click ```Import File```.

- Navigate to AnkiDeckGen's ```csv_output``` folder and select the latest CSV file.

- In Anki's import window make sure that the card type is set to 'Basic' (two-sided), fields are separated by a Semicolon, and the ``Allow HTML`` box is checked.

- The ```Deck``` button in the the top-right of the window will allow you to either import into a new deck or add them to an existing one.

- Restart Anki. 

## Troubleshooting

If your target language is set to Russian, you might get an error when running the program:

``` File "/home/user_name/.local/lib/python3.8/site-packages/russian_text_stresser/russian_dictionary.py", line 46, in RussianDictionary
    def __init__(self, db_file: str, simple_cases_file: str | None) -> None:
    TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'```


In that case, you need to edit ```local/lib/Python3.x/site-packages/russian_text_stresser/text_stresser.py```

Change the line in the  ```__init__``` function (at about line 46)...

From:

```def __init__(self, db_file: str, simple_cases_file: str | None) -> None:```

To:

```def __init__(self, db_file: str, simple_cases_file) -> None:```


 

