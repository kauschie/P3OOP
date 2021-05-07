class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid File Format")
        
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print(f"playing {self.filename} as mp3")

class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print(f"playing {self.filename} as wav")

class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print(f"playing {self.filename} as ogg")

