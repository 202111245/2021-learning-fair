import turtle

print("1. Hang Man  2. 베스킨라벤스 31   3. 인디언포커   4. 핑퐁게임")
print("게임 번호 입력시 해당 게임이 시작되며 -를 붙일시 게임 설명, 0을 입력시 종료됩니다.")
while True:
    number = input("플레이할 게임번호를 적어주세요 : ")
    number = int(number)
    if number == -1:
        print("영어 단어를 하나의 알파벳씩 추측하면서 맞추는 행맨 게임")
        print("그림이 완성되기 전에 단어를 맞추면 성공!")


    elif number == -2:
        print("컴퓨터와 자신이 번갈아가면서 최대 3개의 숫자를 1부터 제시하는 베스킨라벤스 31 게임")
        print("31을 말하게 되면 실패, 컴퓨터가 31을 말하면 승리!")


    elif number == -3:
        print("상대방의 패를 보며 칩을 배팅하는 게임인 인디언 포커 게임")
        print("주어진 칩 20개를 모두 탕지하면 패배, 60개를 얻으면 승리!")
        print("카드의 대소 비교로 칩 획득. 기준은 1. 숫자가 크면 이긴다. 10 < J < Q < K < A 2. 숫자가 같으면 모양을 따라간다 스페이드 > 다이아 > 하트 > 클로버 ")


    elif number == -4:
        print("스틱을 조절하여 날아오는  공을 받아내 넘기는 핑퐁게임")
        print("공을 받아내거나 상대가 놓치면 1점 획득!, 10점 획득 시 승리!")

    elif number == 0:
        break

    elif number == 1:
        screen = turtle.Screen()  ##고친 부분
        screen.title("Hang Man")  ##고친 부분
        t = turtle.Pen()
        t.speed(5)
        t.hideturtle()

        def gallows() :
            t.right(90)
            t.forward(15)

        def gallow() :
            t.penup()
            t.home()
            t.pendown()
    

        t.backward(25)
        gallows()
        gallow()
        t.forward(25)
        gallows()
        gallow()
        t.left(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(10)
        t.speed(2)

        import random
        words = ["place","apple","culture","object","unity","honor","scene","price","ocean","earth","glory","candle","nurse","army","effort","route","north","market","dress","death"]
        answer_word = random.choice(words)
        #print(answer_word)

        word_long = len(answer_word)
        #print(word_long)

        underscore_power = "-" * word_long
        #print(underscore_power)
        underscore = list(underscore_power)
        print(underscore)

        answer_word_spelling = list(answer_word)
        #print(answer_word_spelling)

        answer_number = 0
        hangman_life = 6

        while True :

            enter_letter = input("알파벳을 입력하세요 :")
            #print(enter_letter)

            if enter_letter in answer_word_spelling:
                print("그 알파벳은 단어 내에 존재합니다!")
                while enter_letter in answer_word_spelling:
                    special_index = answer_word_spelling.index(enter_letter)
                    del underscore[special_index]
                    underscore.insert(special_index,enter_letter)
                    answer_word_spelling.remove(enter_letter)
                    answer_word_spelling.insert(special_index,"_")
                    #print(answer_word_spelling)
                    answer_number = answer_number + 1
                    #print(answer_number)
                print(underscore)
                if answer_number == word_long :
                    print("클리어!")
                    t.clear()
                    t.hideturtle()
                    break
            else :
                print("그 알파벳은 단어 내에 존재하지 않습니다.")
                hangman_life = hangman_life - 1
                if hangman_life == 5 :
                    t.right(90)
                    t.circle(10)
                elif hangman_life == 4 :
                    t.left(90)
                    t.penup()
                    t.forward(20)
                    t.pendown()
                    t.forward(40)
                elif hangman_life == 3 :
                    t.backward(40)
                    t.left(45)
                    t.forward(25)
                    t.backward(25)
                    t.right(90)
                    t.forward(25)
                elif hangman_life == 2 :
                    t.backward(25)
                    t.left(45)
                    t.forward(40)
                    t.left(35)
                    t.forward(25)
                elif hangman_life == 1 :
                    t.backward(25)
                    t.right(70)
                    t.forward(25)
                    print("클리어 실패")
                    t.clear()
                    t.hideturtle()
                    turtle.bye()      ##고친 부분
                    turtle.TurtleScreen._RUNNING = True    ##고친 부분
                    break

    elif number == 2:
        import random as rand #랜덤가져오고 글자수 귀찮

        present_number=0
        temp = 0
        past_person_temp = 0
        past_person = ["사람","컴퓨터"]
        participate_number = 0


        while(True):
            participate_number = int(input("참여할 인원을 입력해주세요(자신포함X) : "))
            if(participate_number<=0 and participate_number>=6):
                print("1~5범위의 숫자를 입력해주세요")
                continue
            else:
                print("참여인원 : ", end='')
                print(participate_number+1, end='')
                print("명")
                break


        print("------ 게임 시작 ------")

        order = rand.randrange(1,participate_number+2) # range 특성 ㅇㅋ? 그리고 자기자신
        print("플레이어는",end='')
        print(order,end='')
        print("번째 입니다")


        while(present_number<31):
    
                for i in range(1,participate_number+2): #순서 한사이클 반복
                    if(i == order and present_number<31):
                        while(temp<1 or temp>3): #플레이어 입력 걸러내
                            temp = int(input("플레이어 숫자입력 : "))
                            if(temp<1 or temp>3):
                                print("1~3범위의 숫자를 입력해주세요")
                        
                    
                    
                        past_person_temp = 0
                        for i2 in range(1,temp+1):
                            present_number += 1
                            print(present_number,end='')
                            print("!")
                            if(present_number>=31):
                                break
                    
        
                
                
                    elif(present_number<31):
                        temp = rand.randrange(1,4) #1부터 3까지 숫자를 랜덤으로
                        past_person_temp = 1
                        print("컴퓨터입력")
                        for j in range(1,temp+1):
                            present_number +=1
                            print(present_number,end='')
                            print("!")
                            if(present_number>=31):
                                break

                    temp = 0 #한사이클 마다 temp변수 초기화
                    


        if(past_person[past_person_temp]=="사람"):
            print("사람이 걸렸다")
            
        elif(past_person[past_person_temp]=="컴퓨터"):
            print("컴퓨터가 걸렸다")

    elif number == 3:
        cash_computer = 10000000000000000000000000000
        cash_player = 20


        import random

  
        dic ={'Spade':100, 'Diamond':99, 'Heart':98, 'Clover':97, 'A':14, 'K':13, 'Q':12, 'J':11}

        shape = ("Spade", "Diamond ", "Heart", "Clover")

        num = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'K', 'Q')

        while True:
         if cash_player > 1:
          shape_computer = random.choice(shape)
          num_computer = random.choice (num)
          card_computer = shape_computer,num_computer
   
          shape_player = random.choice(shape)
          num_player = random.choice (num)
          card_player = shape_player,num_player

          if shape_computer == shape_player and num_computer == num_player:
           continue

          print("컴퓨터의 패는", card_computer)
 
          bet_player = int(input(' 베팅할 칩의 개수를 입력해주세요'))
  
     
          if bet_player >= cash_player or bet_player <= 0:
             print(" 장난하십니까 휴먼?")
             continue

   
          print("당신의 패는", card_player)
   
          if num_player > num_computer:
            print(" 당신이 승리했습니다 ")
            cash_player = cash_player + bet_player
      
          elif num_player == num_computer and shape_player > num_computer:
            print(" 당신이 승리했습니다 ")
            cash_player = cash_player + bet_player
            cash_computer = cash_computer + bet_player

          else:
            print("컴퓨터가 승리했습니다")
            cash_player = cash_player - bet_player
            cash_computer = cash_computer + bet_player
              
 
          print (" 현재 player의 칩 개수는", cash_player)
          print ("   ")
  
         if cash_player == 1:
            print("차비는 남겨놔야 하지 않겠어?")
            break

         elif cash_player >= 60:
             print("딜러도 먹고 살아야하니 이만 물러가겠습니다")
             break
     

                

        
              
    elif number == 4:
        import time

        screen = turtle.Screen()
        screen.bgcolor("ivory")
        screen.title("핑퐁 게임")
        screen.setup(width=1000, height=600, startx=0, starty=0)

        rightpaddle = turtle.Turtle()
        rightpaddle.speed(0)
        rightpaddle.shape("square")
        rightpaddle.color("pink")
        rightpaddle.shapesize(stretch_wid=6, stretch_len=1)
        rightpaddle.penup()
        rightpaddle.goto(400, 0)

        leftpaddle = turtle.Turtle()
        leftpaddle.speed(0)
        leftpaddle.shape("square")
        leftpaddle.color("sky blue")
        leftpaddle.shapesize(stretch_wid=6, stretch_len=1)
        leftpaddle.penup()
        leftpaddle.goto(-400, 0)

        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("black")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 5
        ball.dy = -5

        firstplayer = 0
        secondplayer = 0

        display = turtle.Turtle()
        display.speed(0)
        display.penup()
        display.ht()
        display.goto(0, 250)
        display.write("1stplayer: 0       2ndplayer: 0",  False, "center", ("", 30))

        def rightPaddle_Up():
            if rightpaddle.ycor() <= 240:
                y = rightpaddle.ycor() + 20
                rightpaddle.sety(y)

        def rightPaddle_Down():
           if rightpaddle.ycor() >= -240:
                y = rightpaddle.ycor() - 20
                rightpaddle.sety(y)

        def leftPaddle_Up():
            if leftpaddle.ycor() <= 240:
                y = leftpaddle.ycor() + 20
                leftpaddle.sety(y)

        def leftPaddle_Down():
            if leftpaddle.ycor() >= -240:
                y = leftpaddle.ycor() - 20
                leftpaddle.sety(y)

        screen.listen()
        screen.onkeypress(rightPaddle_Up, "Up")
        screen.onkeypress(rightPaddle_Down, "Down")
        screen.onkeypress(leftPaddle_Up, "Left")
        screen.onkeypress(leftPaddle_Down, "Right")

        game_on = True

        while True:            
            screen.update()

            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)

            if ball.ycor() > 280:
                ball.sety(280)
                ball.dy = ball.dy * -1

            if ball.ycor() < -280:
                ball.sety(-280)
                ball.dy = ball.dy * -1

            if ball.xcor() > 500:
                ball.goto(0, 0)
                ball.dy = ball.dy * -1      
                firstplayer = firstplayer + 1
                display.clear()
                display.write("1st player: {}       2nd player: {}".format(firstplayer, secondplayer),  False, "center", ("", 30))
        
                if firstplayer == 10:
                    display.goto(0, 0)
                    display.clear()
                    display.write("Game Over, 1st player wins!", False, "center", ("", 50))

                    time.sleep(5)
                    turtle.bye()
                    turtle.TurtleScreen._RUNNING = True  ##고친 부분
                    break
            
            if ball.xcor() < -500:
                ball.goto(0, 0)
                ball.dy = ball.dy * -1
                secondplayer = secondplayer + 1
                display.clear()
                display.write("1st player: {}       2nd player: {}".format(firstplayer, secondplayer),  False, "center", ("", 30))   

                if secondplayer == 10:
                    display.goto(0, 0)
                    display.clear()
                    display.write("Game Over, 2nd player wins!", False, "center", ("", 50))
     
                    time.sleep(5)
                    turtle.bye()
                    turtle.TurtleScreen._RUNNING = True  ##고친 부분
                    break
        
            if ((ball.xcor() > 360 and ball.xcor() < 400) and
                     (ball.ycor() < rightpaddle.ycor() + 40 and
                      ball.ycor() > rightpaddle.ycor() - 40)):
                 ball.setx(360)
                 ball.dx = ball.dx * -1
                 secondplayer = secondplayer + 1
                 display.clear()
                 display.write("1st player: {}       2nd player: {}".format(firstplayer, secondplayer),  False, "center", ("", 30))   

                 if secondplayer == 10:
                    display.goto(0, 0)
                    display.clear()
                    display.write("Game Over, 2nd player wins!", False, "center", ("", 50))
   
                    time.sleep(5)
                    turtle.bye()
                    turtle.TurtleScreen._RUNNING = True  ##고친 부분
                    break
            
            if ((ball.xcor() < -360 and ball.xcor() > -400) and
                     (ball.ycor() < leftpaddle.ycor() + 40 and
                     ball.ycor() > leftpaddle.ycor() - 40)):
                 ball.setx(-360)
                 ball.dx = ball.dx * -1
                 firstplayer = firstplayer + 1
                 display.clear()
                 display.write("1st player: {}       2nd player: {}".format(firstplayer, secondplayer),  False, "center", ("", 30))

                 if firstplayer == 10:
                    display.goto(0, 0)
                    display.clear()
                    display.write("Game Over, 1st player wins!", False, "center", ("", 50))

                    time.sleep(5)
                    turtle.bye()
                    turtle.TurtleScreen._RUNNING = True  ##고친 부분
                    break
