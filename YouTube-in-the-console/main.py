from moviepy.editor import VideoFileClip
from replit import clear, audio
from pytube import YouTube
import math
import glob
import time
import os

isOwner = os.path.exists("/tmp/audioStatus.json")

# thx @hecker40
def bg(r, g, b):
  return f"\033[48;2;{r};{g};{b}m"
reset = "\033[0m"

# thx @ColoredHue
def hide_cursor():
  print("{}[?25l".format(chr(27)), end="", flush=True)
def show_cursor():
  print("{}[?25h".format(chr(27)), end="", flush=True)

for file in glob.glob("*.mp3"):
  os.remove(file)

for file in glob.glob("*.mp4"):
  os.remove(file)

show_cursor()

print("You're about to be asked questions so we can get the correct screen size. You may be asked to see which character appears in the corner, but oftern this is obscured by buttons. To remove them, click off the screen")
print()
input("Press enter to continue > ")
clear()

chars = "0123456789abcdef"
msg = "Which character appears in the top right corner of the screen? > "

print(chars*len(chars))
print()
c = input(msg).lower()
clear()

for x in chars:
  print(" "*chars.find(c)+x+" "*(len(chars)-chars.find(c)-1), end="", flush=False)
print("\n", flush=True)
c2 = input(msg).lower()
clear()

width = chars.find(c2)*len(chars)+chars.find(c)+1

for x in chars:
  for y in chars:
    print(" "*(width-1), y, sep="", flush=False)
print(flush=True)
c = input(msg).lower()
clear()

i = 0
for x in chars:
  for y in chars:
    if y == c:
      print(" "*(width-1), chars[i], sep="", flush=False)
      i += 1
    else:
      print(flush=False)
print(flush=True)
c2 = input(msg).lower()
clear()

height = len(chars)**2 - (chars.find(c2) * len(chars) + chars.find(c)) + math.ceil((len(msg)) / width) + 1

width = math.floor(width / 2)
height -= 1

if not os.environ["REPL_OWNER"] == "PikachuB2005":
  url = input("Enter a video url > ")
else:
  url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

if isOwner:
  clear()
  playAudio = input("Do you want audio? y/n > ") == "y"
  if playAudio:
    audio.play_tone(2, 262, 0)
    input("Press enter to continue > ")
else:
  playAudio = False

clear()
print("Downloading Video...")

yt = YouTube(url)
vid = yt.streams.filter(file_extension="mp4").first()
vid.download()

clear()
print("Opening Video...")

filename = glob.glob("*.mp4")[0]
vid = VideoFileClip(filename)

clear()
print("Resizing Video...")

vidWidth, vidHeight = vid.size
ratio = min(width / vidWidth, height / vidHeight)

vid = vid.resize(ratio)

if playAudio:
  clear()
  print("Extracting Audio...")
  
  vidAudio = vid.audio
  vidAudio.write_audiofile("audio.mp3", logger=None)

hide_cursor()
clear()

if playAudio:
  audio.play_file("audio.mp3")

start = time.time()

try:
  while True:
    frame = vid.make_frame(t=time.time()-start)
    print("\033[H\033[2J", end="", flush=False)
    for column in frame:
      for pixel in column:
        print(bg(*pixel)+"  ", end="", flush=False)
      print(flush=False)
    print(reset, end="", flush=True)
    time.sleep(0.33)
except OSError:
  clear()
  print("Video Finished! Don't forget to like and subscribe!")