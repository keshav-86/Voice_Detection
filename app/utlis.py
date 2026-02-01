import base64
import tempfile
from pydub import AudioSegment

def decode_audio(base64_str: str):
    audio_bytes = base64.b64decode(base64_str)

    temp_mp3 = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_mp3.write(audio_bytes)
    temp_mp3.close()

    audio = AudioSegment.from_mp3(temp_mp3.name)
    temp_wav = temp_mp3.name.replace(".mp3", ".wav")
    audio.export(temp_wav, format="wav")

    return temp_wav
