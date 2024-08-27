import moviepy.editor as mp
import speech_recognition as sr 

def convertVideoToText():
    # Load the video 
    video = mp.VideoFileClip("sample.mp4") 

    # Extract the audio from the video 
    audio_file = video.audio 
    audio_file.write_audiofile("convertedAudioLecture.wav") 

    # Initialize recognizer 
    r = sr.Recognizer() 

    # Load the audio file 
    with sr.AudioFile("convertedAudioLecture.wav") as source: 
        data = r.record(source) 

    text = r.recognize_google(data) 

    # Return the text 
    return text

# Call the function and store the result
resultant_text = convertVideoToText()

# Print or use the result
print("\nThe resultant text from the video is: \n")
print(resultant_text)

# Optionally, save the result to a file
with open("outputText.txt", "w") as f:
    f.write(resultant_text)
