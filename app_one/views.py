from django.shortcuts import render
from mtranslate import translate

# from gtts import gTTS
# from playsound import playsound

# def generate_audio(request):
#     text = "Hello, how are you today?"
#     tts = gTTS(text=text, lang='en')
#     audio_file = 'audio/file.mp3'
#     tts.save(audio_file)
#     return audio_file

def my_view(request):
    # is_data_received = True
    text = request.POST.get('text')
    language = request.POST.get('target_language')
    # audio_file = generate_audio(request)
    translation = ""

    if text is not None:
        try : translation = translate(str(text), str(language))
        except: translation = ""
    else: text = ""

    data =  {
        'translation': translation,
        'input': text,
        # 'is_data_received': is_data_received,
        # 'voice' : audio_file,
             }

    return render(request, 'index.html', context=data)
