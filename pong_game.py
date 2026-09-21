import turtle # بيخليني ارسم و احرك الرسومات

#---------------------------------------
wind = turtle.Screen() # بتنشئ شاشة
wind.title("ping pong by mohamed")# بتعمل عنوان
wind.bgcolor("black")#لون الخلفية
wind.setup(width=800, height=600)# الطول و العرض
wind.tracer(0)# هنا بمنع تحديث الشاشة المتكرر
#----------------------------------------


#----------------------------------------
# 1 مضرب    
madrab1 = turtle.Turtle() #هيبقي عندي اوبجيكت جوا المضرب
madrab1.speed(0)# ودي سؤؤعه الانميشن مش سؤعة المضرب
madrab1.shape('square')# دا شكل المضرب
madrab1.color("blue")# لون المضرب
madrab1.shapesize(stretch_len=1,stretch_wid=5)
madrab1.penup()# عشان ميرسمش اي خطوط وراها
madrab1.goto(-350, 0)# بيحدد مكان المضرب


# 2 مضرب 
madrab2= turtle.Turtle() #هيبقي عندي اوبجيكت جوا المضرب
madrab2.speed(0)# ودي سؤؤعه الانميشن مش سؤعة المضرب
madrab2.shape('square')# دا شكل المضرب
madrab2.color("Red")# لون المضرب
madrab2.shapesize(stretch_len=1,stretch_wid=5) #طول و عرض المضرب 
madrab2.penup()# عشان ميرسمش اي خطوط وراها
madrab2.goto(350, 0)# بيحدد مكان المضرب


# الكورة
ball = turtle.Turtle() #هيبقي عندي اوبجيكت جوا المضرب
ball.speed(0)# ودي سؤؤعه الانميشن مش سؤعة المضرب
ball.shape('square')# دا شكل المضرب
ball.color("white")# لون المضرب
ball.penup()# عشان ميرسمش اي خطوط وراها
ball.goto(0, 0)# بيحدد مكان المضرب
ball.dx = .1 #كل مره الكورة بتتحرك فيها لازم اسك و واي يتحركه
ball.dy = .1 #--

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1 :0 player 2 :0", align="center", font=("courier",24,"normal"))
#----------------------------------------
#----------------------------------------

#functions

def madrab1_up():# بيتحرك لفوق
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)

def madrab1_down(): #بيتحرك لتحت   
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)

def madrab2_up():# بيتحرك لفوق
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down(): #بيتحرك لتحت   
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)
#keyboard bindings
wind.listen()#بيقول للكود استني ممكن اليوزر يدخل جاجه من الكيب
wind.onkeypress(madrab1_up,"w")# لما يكتب دبليو بيطلع فوق
wind.onkeypress(madrab1_down,"s")# لما يكتب اس بينزل تحت
wind.onkeypress(madrab2_up,"Up")# لما يكتب دبليو بيطلع فوق
wind.onkeypress(madrab2_down,"Down")# لما يكتب اس بينزل تحت


#----------------------------------------

#----------------------------------------
while True:
    wind.update() # كل ما الشاشة تشتغل الشاشة هتحدث نفسها

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1 :{} player 2 :{}".format(score1,score2), align="center", font=("courier",24,"normal"))

    if ball.xcor() < -390:
         ball.goto(0,0)
         ball.dx *= -1
         score2 += 1
         score.clear()
         score.write("player 1 :{} player 2 :{}".format(score1,score2), align="center", font=("courier",24,"normal"))

    #tasabom madrab and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1