# winsound-music-library
This library uses notation I designed myself.
When passing an object to the playSong() procedure, you should use the following syntax:
  
  The object is a list.
  
  The first item in the list is the length, in milliseconds, of each beat of the music.
  
  The rest of the list is the music to play.
  
  Each note is an item in the list.
  
  Notes are constructed as a string using these rules:
    
    The first part is the number of beats to play the note for -- non-integers may be used.
    
    The second part is the note's letter identifier (A-G)
    
    The third part is the octave of the note, where the A in the 4th octave has a frequency of 440Hz.
    
    The different parts of the note are separated from each other within the same string using commas.
    
    Octaves range from 3 to 6 but the 3rd octave may not produce sound on many machines.
    
    an example note is "2,a,4", which will play the 4th A (440Hz) for 2 beats.
