#import modules

import time
import simpleaudio as sa

#variables


answer_yes = ["Yes", "yes", "Y", "y"]
answer_no = ["No", "N", "no", "n"]


time.sleep(1)


print("""
WELCOME! LET'S START THE ADVENTURE
""")


wave_obj = sa.WaveObject.from_wave_file("./sounds/bg_music.wav")
wave_obj.play()


time.sleep(2)


#first question


print("""
        You wake up in your bedroom in the middle of the night. You hear a loud BANG outside the house.
        You think about leaving your bed to check what it is, should you leave. 
     
        Type your choice: Yes or no?
        """)


ans1 = input(">>")


if ans1 in answer_yes:
    print("You get out of bed and start creeping down the stairs towards the front door.")

    wave_obj = sa.WaveObject.from_wave_file("./sounds/door_swing.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

    time.sleep(2)


    print("""
            You push the front door and walk outside, and there it is,
            a MASSIVE monster standing on your driveway.
            The monster starts walking towards you!""")

    
    time.sleep(1.5)


    wave_obj = sa.WaveObject.from_wave_file("./sounds/monster_walking.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

            
    print("""           You are right in front of your house,
            should you go inside?
            Type your choice: Yes or no?""")


    time.sleep(1)


    #second question


    ans2 = input(">>")


    if ans2 in answer_yes:
        print("""        Just as you make it inside the house, you hear a THUD
        phew! Just in time. And then you realize something, there is no one in the
        house other than you...""")

        
        time.sleep(1)


        wave_obj = sa.WaveObject.from_wave_file("./sounds/2_1.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()


        time.sleep(2)
        

        #third question


        print("""       You look around, but its true, you're all alone.
        You cant hear any sirens either, so it has come to this, you might be
        the last human on earth. 
        

                Should you try to look around the garage?""")


        time.sleep(1)


        ans3 = input(">>")


        if ans3 in answer_yes:
            print("""         You open the garage door and you look inside, there before you stands
            an alien, he shoots you with his blaster. GAME OVER""")


            wave_obj = sa.WaveObject.from_wave_file("./sounds/3.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()


            quit


        elif ans3 in answer_no:
            print("""               You walk upstairs in search of food.""")


            time.sleep(1)


            wave_obj = sa.WaveObject.from_wave_file("./sounds/stone_walking.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()


            print("""         
                You open up the fridge,
                you see food, but you also see a massive
                spider sitting right beside it. 
                Should you run away?"
                """)


            time.sleep(1)


            ans4 = input(">>")


            if ans4 in answer_yes:
                print("""               You run out of the kitchen, but
                the spider catches up and bites you. GAME OVER!""")


                wave_obj = sa.WaveObject.from_wave_file("./sounds/4.wav")
                play_obj = wave_obj.play()
                play_obj.wait_done()


                quit


            elif ans4 in answer_no:
                print("""                 You grab a knife off of the kitchen counter
                and slay the spider just in time. And then, you take 
                the food.""")


                print("""         
                You are looking out the window, and then 
                you have the idea to get the car which is 
                sitting in the driveway, and the monster
                has just turned his back!
                Should you go for it?
                """)



                ans5 = input(">>")


                if ans5 in answer_yes:
                    print("""               You quickly run
                up to the car, start it and back up out of the
                driveway just in time to get away from the monster.""")


                    wave_obj = sa.WaveObject.from_wave_file("./sounds/5_2.wav")
                    play_obj = wave_obj.play()
                    play_obj.wait_done()


                    time.sleep(1)


                    print("""         
                You are driving down a barren highway
                and you are looking for the local military base 
                hoping there might be people there. You see a person
                who is holding a sign pointing to the "local military
                base." But something seems off about him, should you follow
                his sign?
                """)



                    ans6 = input(">>")


                    if ans6 in answer_yes:
                        print("""               You follow the persons
                        sign, just to find out they werent a person, 
                        they were a zombie! Because a horde of 
                        zombies surrounds your car. GAME OVER!""")


                        wave_obj = sa.WaveObject.from_wave_file("./sounds/6_1.wav")
                        play_obj = wave_obj.play()
                        play_obj.wait_done()


                    


                    elif ans6 in answer_no:
                        print("""           You decide not to follow the persons sign
                        and you continiue on your way.""")

                        wave_obj = sa.WaveObject.from_wave_file("./sounds/6_2.wav")
                        play_obj = wave_obj.play()
                        play_obj.wait_done()


                        print("""You see a military base a head roadblocking the highway, you have made it to safety!! GG""")

                        time.sleep(1)

                        print("quitting in 5 seconds...")

                        time.sleep(5)

                        quit


                    else:
                        print("""You typed wrong input the supported answers are the following:
                        For yes: Y, y, Yes, yes
                        For no: N, n, No, no
                        Each time you enter the wrong answers you lose, GOODBYE!""")


                elif ans5 in answer_no:
                    print("""           You decide not to go, but then, 
                    you hear a noise and you realize the monster was getting 
                    ready to break into the house! You run away, but you
                    are not fast enough, and the monster eats you. 
                    GAME OVER!""")

                    wave_obj = sa.WaveObject.from_wave_file("./sounds/5_1.wav")
                    play_obj = wave_obj.play()
                    play_obj.wait_done()


                else:
                    print("""You typed wrong input the supported answers are the following:
                    For yes: Y, y, Yes, yes
                    For no: N, n, No, no
                    Each time you enter the wrong answers you lose, GOODBYE!""")


            else:
                print("""You typed wrong input the supported answers are the following:
                For yes: Y, y, Yes, yes
                For no: N, n, No, no
                Each time you enter the wrong answers you lose, GOODBYE!""")


        else:
            print("""You typed wrong input the supported answers are the following:
            For yes: Y, y, Yes, yes
            For no: N, n, No, no
            Each time you enter the wrong answers you lose, GOODBYE!""")


    elif ans2 in answer_no:
        print("""You face the monster, but then you realize,
        you have nothing to defend yourself with! The monster jumps
        on you and EATS YOU! GAME OVER""")


        #play monster sound
        wave_obj = sa.WaveObject.from_wave_file("./sounds/1.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()


    else:
        print("""You typed wrong input the supported answers are the following:
        For yes: Y, y, Yes, yes
        For no: N, n, No, no
        Each time you enter the wrong answers you lose, GOODBYE!""")


elif ans1 in answer_no:
        print("You stay in bed, but then, you hear a noise... AND A MONSTER JUMPS YOU! GAME OVER")
        time.sleep(0.5)
        

        #play monster sound
        wave_obj = sa.WaveObject.from_wave_file("./sounds/1.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()

else:
        print("""You typed wrong input the supported answers are the following:
        For yes: Y, y, Yes, yes
        For no: N, n, No, no
        Each time you enter the wrong answers you lose, GOODBYE!""")