import winsound,time

def playNote(note,octave,length):
    # This is a dicionary to search through for frequencies.
    noteFreqs = {3:{'C':131,
                    'D':147,
                    'E':165,
                    'F':175,
                    'G':196,
                    'A':220,
                    'B':247},
                 4:{'C':262,
                    'D':294,
                    'E':330,
                    'F':349,
                    'G':392,
                    'A':440,
                    'B':494},
                 5:{'C':523,
                    'D':587,
                    'E':659,
                    'F':698,
                    'G':784,
                    'A':880,
                    'B':988},
                 6:{'C':1047,
                    'D':1175,
                    'E':1319,
                    'F':1397,
                    'G':1568,
                    'A':1760,
                    'B':1976}}

    noteFreq = noteFreqs[octave][note.upper()] # Gets the length
    winsound.Beep(noteFreq,length) # Plays the note
    time.sleep(0.1) # Wait.
    # The wait is needed to avoid issues with the speaker.

def playSong(music):
    # This procedure will accept my custom notation and
    # Use it to play a sequence of notes.
    #
    # --Notation guide--
    # Music parameter should be a list object.
    # The first item in the list should be the length of each beat in milliseconds.
    # Every item after this will be one note.
    # Notes are written as: 'length,note,octave'
    # Where length is the number of beats the note will last.
    # Note is the letter (A-G not case-sensitive) of the note.
    # Octave is the number of the octave (higher pitch is greater octave num) in range 3-6
    # lower end of 3rd octave may not be audible on some machines
    # Use 0 as the note to denote a rest.
    tempo = music[0]
    for i in range(1,len(music)):
        music_list = music[i].split(',')
        beatsNum = float(music_list[0])
        noteTemp = music_list[1]
        octaveTemp = int(music_list[2])
        noteLength = round(beatsNum * tempo)
        if noteTemp != '0':
            playNote(noteTemp,octaveTemp,noteLength)
        else:
            time.sleep(noteLength/1000)
        
#playSong([500,'1,c,4','0.5,a,5'])
#This example plays a C from the 4th octave for 1 beat,
#then an A from the 5th octave for 0.5 beats

