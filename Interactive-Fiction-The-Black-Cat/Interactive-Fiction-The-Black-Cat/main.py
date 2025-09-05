import random
import time
normal_wait = 2
short_wait = 1
bit_wait = 0.5

noticedDairy = 1
noticedPoem = 1

from colorama import Fore, Back, Style

print("............")
time.sleep(short_wait)
print("......")
time.sleep(short_wait)
input("You open your eyes. \nThe room is dark, but you can still see what’s around you from the \ntiny light coming from the window. You feel like your vision is \nspinning around you. It’s your headache, it’s getting worse. \n" + Style.DIM + "* (tap enter to continue)")
print(Style.RESET_ALL)
input("You don’t remember how you got in here, or nevertheless, you don’t \neven remember who you are. The only thing filling your headspace is the \npain of your head and thoughts of getting out of here. \nMaybe you should start looking around." + Style.DIM + "* (tap enter to continue)")


#SCENE 2
def scene2_checkAsk():
  print(Style.RESET_ALL)
  print("“Let’s see… Check the desk in front, \nthe door on the left, the window on the right, \nor the shelf behind?”")
  scene2_check()
def scene2_check():
  checkWhere = input(Style.RESET_ALL + Fore.BLUE + "【check desk/ check door/ check window/ check shelf】" + Style.RESET_ALL)
  if checkWhere == "check desk":
    print(Style.RESET_ALL)
    print("")
    scene3_desk()
  elif checkWhere == "check door":
    print(Style.RESET_ALL)
    print("")
    scene4_door()
  elif checkWhere == "check window":
    print(Style.RESET_ALL)
    print("")
    scene5_window()
  elif checkWhere == "check shelf":
    print(Style.RESET_ALL)
    print("")
    scene6_shelf() 
  else:
    print("")
    print(Fore.RED + "---System: I don't recognize your choice.---") 
    scene2_check()


#SCENE 3
def scene3_desk():
  input("You walk carefully through the messy room. \nWhoever’s room is this, the owner must be really unorganized. Paper \nboxes everywhere with a lot of old stuff that you can’t tell the name." + Style.DIM + " \n* (tap enter to continue)")
  print(Style.RESET_ALL)
  input("You reach the desk. \nCompared to the messy floor, the desk is surprisingly clean. There’s only \na few pieces of torn paper and an ink pen lying quietly on the desk. You \nalso realized the desk drawer is half open, and it seems something is in it." + Style.DIM + " \n*")
  print(Style.RESET_ALL)
  print("Which one would you like to check?")
  scene3_deskCheck()

def scene3_deskCheck():
  deskCheck = input(Style.RESET_ALL + Fore.BLUE + "【check desktop/ check drawer】" + Style.RESET_ALL)
  if deskCheck == "check desktop":
    print("")
    scene3_deskTop()
  elif deskCheck == "check drawer":
    print("")
    scene3_drawer()
  else:
    print("")
    print(Fore.RED + "---System: I don't recognize your choice.---")
    scene3_deskCheck()

def scene3_deskTop():
  input("You start to look through the things on the desk. The ink pen is made \nof golden metal, even though it's a bit rusty, you can still see the \nbeauty it once had." + Style.DIM + " *" + Style.RESET_ALL)
  input("You read through the paper on the desk. Some of them are random scratches, \nor words that you can not understand. When you are about to give up, \nyou notice a piece of paper with a poem written on it. You carefully \nread through." + Style.DIM + " *")
  print(Style.RESET_ALL)
  input("“The cat on the moon dedicated his life to the earth." + Style.DIM + "\nOne " + Style.RESET_ALL + "is protection, and the other is a once shared dream. \nLook at the sky, the " + Style.DIM + "six " + Style.RESET_ALL + "stars are where it once lived. \nThey pursue their lives, even the " + Style.DIM + "two " + Style.RESET_ALL + "people can never be free. \nMay you live freely for the rest of your " + Style.DIM + "six " + Style.RESET_ALL + "lifes.”" + Style.DIM + " *")
  print(Style.RESET_ALL )
  input("“That’s… Indeed an interesting poem. So what does it mean exactly?”" + Style.DIM + " *" + Style.RESET_ALL)
  global noticedPoem
  noticedPoem = 2 
  if noticedDairy == 2:
    input("Maybe the same person who wrote the diary wrote this." + Style.DIM + " *" )
  print(Style.DIM + "............")
  time.sleep(bit_wait)
  print("............")
  time.sleep(short_wait)
  scene2_checkAsk()

def scene3_drawer():
  input("You open the drawer. And a silver cutting knife sits in the drawer. \nYou are scared for a second, but soon you calm yourself down." + Style.DIM + " *" + Style.RESET_ALL)
  input("You look closely into this knife: it's not sharp enough to make serious injuries, \nbut good enough for cutting through meat pieces or opening a can." + Style.DIM + " *")
  print(Style.RESET_ALL)
  input("“Better not touch it for right now.” You murmured to yourself." + Style.DIM + " *")
  print(Style.DIM + "............")
  time.sleep(bit_wait)
  print("............")
  time.sleep(short_wait)
  scene2_checkAsk()
  
#SCENE 4
def scene4_door():
  input("You walk toward the door. It seems like this is the only way to get out of \nthis place. The old door makes weird noises while you are pushing it. You \ntry to open it, but it’s locked. Maybe there's a key somewhere in the room?" + Style.DIM + " \n* (tap enter to continue)")
  print(Style.DIM + "............")
  time.sleep(bit_wait)
  print("............")
  time.sleep(short_wait)
  scene2_checkAsk()

#SCENE 5
def scene5_window():
  input("You look at the only light source of this room. \nWeak light came through the window and lit up the room. The light is \nreally dim, stil, it’s good enough for you to see the whole room." + Style.DIM + "\n* (tap enter to continue)" + Style.RESET_ALL)
  input("The window can not be opened, and it’s hard to see outside from the inside. \nIt’s impossible to escape by window, it seems." + Style.DIM + " *" + Style.RESET_ALL)
  if random.random() < 0.4:
    print("You look closely, a cat paw shape mark appeared on the window- which it \nwas not there before. But it disappeared after a blink. \n") 
    time.sleep(short_wait)
    input(Fore.GREEN + "【Achievement: Every meet is fate.】" +Style.RESET_ALL + Style.DIM + " *" + Style.RESET_ALL)
  print(Style.DIM + "............")
  time.sleep(bit_wait)
  print("............")
  time.sleep(short_wait)
  scene2_checkAsk()

#SCENE 6
def scene6_shelf():
  input("You turn around. Next to the bed there’s a shelf. It is covered with dust, but \nyou can tell it’s well decorated. You feel like you’ve seen this shelf somewhere. \nThe way it’s being organized is familiar to you somehow." + Style.DIM + "\n* (tap enter to continue)" + Style.RESET_ALL)
  scene6_shelfAsk()

def scene6_shelfAsk():
  checkShelf = input("Which level of the shelf should you check?\n" + Fore.BLUE + "【shelf top/ shelf middle/ shelf bottom】" + Style.RESET_ALL)
  if checkShelf == "shelf top":
    print(Style.RESET_ALL)
    print("")
    scene6_shelfTop()
  elif checkShelf == "shelf middle":
    print(Style.RESET_ALL)
    print("")
    scene6_shelfMiddle()
  elif checkShelf == "shelf bottom":
    print(Style.RESET_ALL)
    print("")
    scene6_shelfBottom()
  else:
    print("")
    print(Fore.RED + "---System: I don't recognize your choice.---" + Style.RESET_ALL)  
    scene6_shelfAsk()

def scene6_shelfTop():
  input("You look at the top of the shelf. There’s a thick notebook with two separate \npieces of paper on top. You take them down, and read carefully through." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  print("“.... November 6th: \nI’m feeling better again...But I know this won’t be long. \nIs it coming today? Or is it gone forever? … \nI opened the window for it, I hope I can see it for the last time…”")
  time.sleep(normal_wait)
  input("“… November 8th: “I’m feeling tired… Maybe I should take a rest.”" + Style.DIM + " *")
  print(Style.RESET_ALL)
  input("It looks like a diary entry. Some of the words are too messy to read. \nYou notice that “it” was mentioned a few times in these two pieces of \nwriting. You wonder who that is." + Style.RESET_ALL)
  global noticedDairy
  noticedDairy = 2
  if noticedPoem == 2:
    input("Maybe the same person who wrote the poem wrote this." + Style.DIM + " *" )
  print(Style.DIM + "............")
  time.sleep(bit_wait)
  print("............")
  time.sleep(short_wait)
  scene2_checkAsk()

def scene6_shelfMiddle():
  input("Not thing particular is there. But you do notice a small piece of \nsticky note stuck on the back." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  print(Fore.RED + Style.BRIGHT + "“... There will be sacrifice….” ")
  time.sleep(bit_wait)
  print(Style.RESET_ALL)
  print("......")
  input("“Is this a message about something? Who is trying to tell me this?” \nYou ask yourself." + Style.DIM + " *" + Style.RESET_ALL)
  print(Style.DIM + "............")
  time.sleep(bit_wait)
  print("............")
  time.sleep(short_wait)
  scene2_checkAsk()

def scene6_shelfBottom():
  input("You find a heavy metal box on the bottom of the shelf. \nIt’s a bit rusty and has a number lock on it. Maybe this box contains \nsome important information." + Style.DIM + " *" + Style.RESET_ALL)
  scene6_boxAsk()

def scene6_boxAsk():
  box = input("Do you want to try to open it?\n" + Fore.BLUE + "【try to open/ leave it for now】" + Style.RESET_ALL)
  if box == "try to open":
    print(Style.RESET_ALL)
    print("")
    scene6_tryBox()
  elif box == "leave it for now":
    print(Style.RESET_ALL)
    print("")
    input("You want to find some more clues before trying to open this box. \nMaybe leaving it alone for right now is the best choice. " + Style.DIM + " *" + Style.RESET_ALL)
    print(Style.DIM + "............")
    time.sleep(bit_wait)
    print("............")
    time.sleep(short_wait)
    scene2_checkAsk()
  else:
    print("")
    print(Fore.RED + "---System: I don't recognize your choice.---" + Style.RESET_ALL)  
    scene6_boxAsk()

def scene6_tryBox():
  tryNumber = input("There’s a four digit number lock on the box." + Fore.BLUE + "\nTry some number, and maybe it will be opened: ")
  if tryNumber == "1626":
    print(Style.RESET_ALL)
    print("")
    print("The box is open. ")
    scene7_theCat()
  else:
    print(Style.RESET_ALL)
    print("")
    print("The lock is still stuck. This is the wrong number. ")
    time.sleep(bit_wait)
    scene6_boxAsk()

#SCENE7
def scene7_theCat():
  print("")
  input("You are eager to look into the box to see if there’s keys or anything \nthat can help you get out of here. But surprisingly, you only get a can of \ncat food out of this mysterious box." + Style.DIM + " *" + Style.RESET_ALL)
  print("You are a bit depressing. You didn’t think much, and put the can next to the window, \nthen sat depressingly on the bed.")
  time.sleep(bit_wait)
  input("“Am I going to be trapped in this room forever?......”" + Style.DIM + " *" + Style.RESET_ALL)
  input("The room starts spinning around you again. \nYour head hurts, so you slowly close your eyes." + Style.DIM + " *" + Style.RESET_ALL)
  print(Style.DIM + "............")
  time.sleep(short_wait)
  print("............")
  time.sleep(short_wait)
  print(Style.RESET_ALL)
  input("When you open your eyes again, a strange black cat sits quietly in front \nof you, calmly eating the half open cat food can." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  input("It has the skin of the purest sky, as dark as the eye of a raven. \nA pair of golden eyes like twinkling stars staring at you." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  print("You stand up, shockingly. \nHow did this cat get in here while the door and the window are closed? \nWho’s cat is this? When did it get in?")
  time.sleep(normal_wait)
  input("So many questions pop up in your mind but all you can do is \nstand there and watch." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  print(Style.DIM + "............")
  time.sleep(short_wait)
  print("")
  input(Fore.RED + Style.DIM + "“There will be sacrifices….”" + Style.RESET_ALL + "A deep voice suddenly interrupted your thoughts.\n You don’t know if this comes from your head or the room, but it \ndrags you back into the reality from your sea of thoughts." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  print(Style.DIM + "......" + Style.RESET_ALL)
  time.sleep(short_wait)
  input("You walk through the room, and grab the knife that sits silently \nin the desk drawer with your trembling hands, trying to defend \nyourself if anything happens." + Style.DIM + " *" + Style.RESET_ALL)
  scene7_knife()

def scene7_knife():
  knife = input(Fore.BLUE + "【wait/ kill】")
  print(Style.RESET_ALL)
  if knife == "wait":
    print("You wait. \nThe black cat is not worried about you standing next to it with a weapon \nin hand, but calmly finishes it’s meal.")
    time.sleep(short_wait)
    input(Fore.GREEN + "【Achievement: “What a kind human being.”】" + Style.RESET_ALL + Style.DIM + " *" + Style.RESET_ALL)
    print("")
    scene8_theKey()
  elif knife == "kill":
    print("Before you notice what you are doing, the cat whisperer in \npain and jumps off the window. Red blood fills \nwith its leg, the dazzling red makes you feeling dizzy.")
    time.sleep(short_wait)
    input(Fore.GREEN + "【Achievement: “This is the sacrifice…?”】" + Style.RESET_ALL + Style.DIM + " *" + Style.RESET_ALL)
    input("Your legs feel like being stuck on the ground. You can’t move an inch. \nThe heavy guilt fills your brain, and your heart is pumping fast." + Style.DIM + " *" + Style.RESET_ALL)
    print("")
    input("The black cat does not seem to be mad, however." + Style.DIM + " *" + Style.RESET_ALL)
    scene8_theKey()
  else:
    print("")
    print(Fore.RED + "---System: I don't recognize your choice.---" + Style.RESET_ALL)
    scene7_knife()

#SCENE8
def scene8_theKey():
  input("Slowly, it walks toward you. You feel like it's golden eyes can \nlook through you, look through all the thoughts in your mind." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  input("An old key suddenly appeared sitting still in your hands. You looked up, \nnot knowing when, the black cat jumped up to the window again. \nYou feel like it is smiling to you." + Style.DIM + " *" + Style.RESET_ALL)
  print(Style.DIM + "......" + Style.RESET_ALL)
  time.sleep(short_wait)
  input("You hold the key tight. Before you can reach out to the cat, \nit is gone. As fast as how it appeared, like snowflakes disappearing \nfrom one’s hands. Quietly, but left firm memories." + Style.DIM + " *" + Style.RESET_ALL)
  print(Style.DIM + "......")
  time.sleep(short_wait)
  print("“Thank you, for all you’ve done these years. \nPlease, take my blessings and live happily for the rest of your life.”" + Style.RESET_ALL)
  time.sleep(normal_wait)
  input("You can feel the black cat whisper into your ear, a peaceful sound. Make \nyou feel like the gentle breeze of April blushing through your face." + Style.DIM + " *" + Style.RESET_ALL)
  print("You feel like something hits hard in your heart. And your headache \nsoon starts to disappear.")
  print("")
  time.sleep(bit_wait)
  print("“The black cat feels like a spirit, maybe all the pain has gone with it.”" + Style.DIM + " *" + Style.RESET_ALL)
  print(Style.DIM + "......" + Style.RESET_ALL)
  time.sleep(normal_wait)
  print("You stand up, slow but steady walk toward the door.")
  input(Fore.GREEN + "【Achievement: “With my blessing, please live happily.”】" + Style.RESET_ALL + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  scene9_theEnd()

#SCENE9
def scene9_theEnd():
  print("")
  print("............")
  time.sleep(short_wait)
  print("......")
  time.sleep(short_wait)
  print("")
  input("You wake up." + Style.DIM + " *" + Style.RESET_ALL)
  input("You are lying in your bed. \nThe pain you used to feel disappeared. You feel like you got a new \nchance, a new life." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  input("You look through the window: It’s snowing hard outside. You don’t \nfeel cold, warmth covers your whole body. The window blocked every coldness \nout, leaving the dim warm light in your room. Calm cracking sound \ncomes from the fireplace, a cup of hot chocolate sits on your desk, with an \nunfinished dairy at the side." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  print("............")
  time.sleep(short_wait)
  input("It feels like a long dream happened, and you finally woke up.\nYou remember now, all the memories came back into your mind." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  input("You moved into this little cabin a few years ago. Because of your illness, \nyou decided to live by yourself in the deep forest for the rest of your \nlife. Then, you met the black cat, with fur like raven's eyes, dark \nand pure. It’s golden eyes were the prettiest thing you’ve ever \nseen, calm as the breeze." + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  input("It must be the power of the black cat, \nor why you feel comfortable whenever it is here?" + Style.DIM + " *" + Style.RESET_ALL)
  print("......")
  input("A strong winter storm hits with your illness getting worse. You can \nonly lay in bed, and watch the black cat hitting your window but yet \nyou can't get up and open it. You felt tire than ever, soon, you fell \ninto a deep sleep. ")
  print("")
  print("")
  input("Until just now, you woke up." + Style.DIM + " *" + Style.RESET_ALL)
  print("“So... That dream...Is it him as well?”\n You murmured to yourself.")
  time.sleep(bit_wait)
  input(Fore.GREEN + "【Achievement: The Black Cat.】" + Style.RESET_ALL + Style.DIM + " *" + Style.RESET_ALL)
  print("")
  print("")
  input("The light is bright.")
  time.sleep(short_wait)
  input("The room is warm.")
  time.sleep(short_wait)
  input("In your arms, lies the cold body of the black cat.")

  


#start of the game check
scene2_checkAsk()
