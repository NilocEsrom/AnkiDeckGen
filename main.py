# one of the language codes listed in googletrans.LANGCODES
native_lang = 'en' # your native language code
target_lang = 'ru' # the language code of your phrases


###################################################################################################
# google translater
# https://pypi.org/project/googletrans/
from googletrans import Translator
gt = Translator()

# returns translated string from input. edit this function to use a different translate, eg. DeepL, Yandex, etc.
def translate_str(s):
	try:
		result = gt.translate(s, src=target_lang, dest=native_lang)
	except:
		result = gt.translate(s, src=target_lang, dest=native_lang)
	return result.text


###################################################################################################
# google text-to-speech. Saves MP3 sound file to Anki's media folder
from gtts import gTTS
def get_mp3(s,fname):

	try:
		tts = gTTS(s, lang=target_lang)
		tts.save('audio_output/' + fname)
	except:
		tts = gTTS(s, lang=target_lang)
		tts.save('audio_output/' + fname)


###################################################################################################
# used for displaying text and translation to terminal/console
from colorama import Fore, Back, Style
target_text = Fore.WHITE + Style.NORMAL + Back.BLACK
native_text = Fore.YELLOW + Style.NORMAL + Back.BLACK
message_text = Fore.BLACK + Style.NORMAL + Back.WHITE
reset_text = Style.RESET_ALL


###################################################################################################
# adding/removing stress markers of Russian words
# https://github.com/Vuizur/add-stress-to-epub
from russian_text_stresser.text_stresser import RussianTextStresser
rts = RussianTextStresser()

def accent(s):
	new_s = rts.stress_text(s)
	return new_s

def unaccent(s):
	# remove diacritic from input text
	new_s = s.replace('\u0301', '')
	return new_s


###################################################################################################
from datetime import datetime
from csv import writer
from datetime import datetime
	
def translate_list():
	with open("phrase_list.txt", 'r') as wl:
		lines = wl.readlines()
	
	phrases = [line.strip() for line in lines]
			
	rows = []
	
	for phrase in phrases:
		if len(phrase) > 0:
			if target_lang == 'ru':
				phrase = unaccent(phrase)
			
			try:# tries to return translation twice (translate_str also tries twice) to reduce errors
				translation = translate_str(phrase)
			except:
				translation = translate_str(phrase)
					
			if target_lang == 'ru':
				print("\n\n" + target_text + accent(phrase) + "\n" + native_text + translation + "\n\n\n")
			else:
				print("\n\n" + target_text + phrase + "\n" + native_text + translation + "\n\n\n")
			
			if target_lang == 'ru':
				row = (accent(phrase), translation)
			else:
				row = (phrase, translation)
				
			rows.append(row)

	if len(rows) > 0:
		dt_string = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")		
		csv_fname = native_lang + '_' + target_lang + '_anki_deck_' + dt_string + '.csv'		
		
		with open('csv_output/' + csv_fname, 'w') as f:		
			mp3_counter = 1
			
			for row in rows:
				mp3_fname = native_lang + '_' + target_lang + '_' + dt_string + str(mp3_counter) + '.mp3'
				f.write("{}<br/>[sound:{}];{}\n".format(row[0], mp3_fname, row[1]))
				get_mp3(row[0], mp3_fname)				
				mp3_counter += 1
				
				
			print(message_text + "\n\nFile saved as " + csv_fname)
			print(reset_text + '')
			
###################################################################################################
# run program
translate_list()
