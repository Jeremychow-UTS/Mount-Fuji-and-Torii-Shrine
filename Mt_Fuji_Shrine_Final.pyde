x = 1
x2 = -2.5
mcloud = 0.5

def setup():
    frameRate(30)
    size(1920, 1000)

def draw():
    global x, x2, mcloud
    print(x, x2, mcloud)
    background(236,211,178)
    
    #skyshading
    strokeWeight(0)
    fill(0, 0, 0, 20)
    ellipse(1450, 600, 5000, 700)

    strokeWeight(0)
    fill(155, 15, 0, 28)
    rect(0, 500, 1920, 600)
    
    textSize(500)
    fill(100, 200, 200) 
    textAlign(CENTER, TOP) 
    text("FUJI", width / 2, 100) 

    # Sun outline & fill
    stroke(255, 255, 255)
    strokeWeight(5)
    fill(255, 255, 255)
    ellipse(1450, 600, 225, 225)

    stroke(255, 255, 255, 128)
    strokeWeight(0)
    fill(255, 255, 255, 128)
    ellipse(1450, 600, 325, 325)

    fill(255, 255, 255, 78)
    ellipse(1450, 600, 420, 420)

    #background city
    fill(123, 117, 117)
    rect(1750, 705, 50, 100)
    rect(1790, 715, 50, 100)
    rect(1855, 700, 50, 100)

    strokeWeight(0)
    fill(173, 167, 167)
    rect(1780, 700, 50, 100)
    rect(1835, 720, 50, 125)
    rect(1895, 685, 50, 200)

    #background mountain
    strokeWeight(0)
    fill(125, 125, 155)
    quad(1450, 800, 1700, 700, 1950, 800, 1920, 1080)
    #background mountain lighting
    fill(255, 255, 255, 50)
    quad(1450, 800, 1700, 700, 1620, 800, 1600, 800)

    # Bottom half of the mountain
    stroke(125, 125, 155)
    strokeWeight(0)
    fill(125, 125, 155)
    quad(455, 680, 1420, 680, 1920, 880, 0, 880)

    # Upper half of the mountain
    fill(125, 125, 155)
    quad(455, 680, 1420, 680, 1105, 450, 805, 450)

    #mount fuji lighting
    fill(255, 255, 255, 50)
    quad(1920, 880, 1420, 680, 1105, 450, 1380, 680)

    # Snow fill-in
    stroke(235, 235, 235)
    strokeWeight(1)
    fill(235, 235, 235)
    quad(805, 450, 1105, 450,  1010, 380, 910, 380)
    quad(805, 450, 850, 485, 878, 468, 878, 450)
    quad(878, 450, 878, 470, 900, 495, 955, 450)
    quad(945, 450, 966, 500, 995, 485, 995, 450)
    quad(995, 450, 995, 485, 1015, 515, 1065, 475)
    quad(1045, 475, 1100, 510, 1145, 478, 1105, 450)
    quad(1105, 450, 1045, 475, 995, 450, 995, 450)

    #snow shading
    fill(205, 205, 205)
    quad(990, 383, 1050, 450, 1055, 515, 990, 380)
    quad(960, 383, 940, 515, 995, 486, 965, 445)
    quad(930, 383, 900, 495, 880, 466, 930, 383)

    #mountain shading
    stroke(0, 0, 0, 0)
    strokeWeight(0)
    fill(0, 0, 0, 20)
    #shading 1
    quad(0, 880, 455, 680, 910, 380, 1340, 680)
    #shading 2
    quad(910, 380, 1010, 380, 1340, 680, 910, 380)
    #shading 3 bottom
    quad(0, 880, 1340, 680, 1920, 880, 0, 880)

    #train tracks
    strokeWeight(0)
    fill(10, 20, 20)
    rect(0, 850, 1919, 50)

    # Landscape outline & fill
    stroke(50, 100, 100)
    fill(50, 100, 205)
    rect(0, 860, 1919, 220)

    #train
    strokeWeight(0)
    fill(225, 225, 225)
    rect(x2 + 1920, 840, 160, 10)
    quad(x2 + 1890, 850, x2 + 1920, 840, x2 + 1920, 860, x2 + 1920, 850)
    quad(x2 + 2080, 840, x2 + 2110, 850, x2 + 2080, 840, x2 + 2080, 840)
    #window
    fill(100, 100, 200)
    rect(x2 + 1940, 843, 5, 5)
    rect(x2 + 1950, 843, 5, 5)
    rect(x2 + 1960, 843, 5, 5)
    rect(x2 + 1970, 843, 5, 5)
    #window set 2
    rect(x2 + 1990, 843, 5, 5)
    rect(x2 + 2000, 843, 5, 5)
    rect(x2 + 2010, 843, 5, 5)
    rect(x2 + 2020, 843, 5, 5)
    #window set 3
    rect(x2 + 2040, 843, 5, 5)
    rect(x2 + 2050, 843, 5, 5)
    rect(x2 + 2060, 843, 5, 5)
    rect(x2 + 2070, 843, 5, 5)

    # Moving cloud
    stroke(0, 0, 0, 0)
    strokeWeight(0)
    fill(255, 255, 255, 245)
    quad(x, 450, x + 500, 450, x + 250, 400, x + 200, 400)
    #cloud 1
    ellipse(x + 250, 450, 510, 50)
    ellipse(x + 250, 410, 600, 40)
    ellipse(x + 265, 430, 900, 40)
    #cloud 2
    ellipse(x + 590, 500, 900, 50)
    ellipse(x + 700, 480, 350, 50)
    ellipse(x + 490, 530, 450, 50)
    #cloud 3
    ellipse(x + 1200, 400, 900, 50)
    ellipse(x + 1400, 385, 860, 50)
    #cloud 4
    ellipse(x - 300, 400, 675, 50)
    ellipse(x - 275, 390, 700, 30)
    #upper cloud 1
    ellipse(x, 100, 1000, 50)
    ellipse(x + 50, 50, 750, 30)
    #upper cloud 2
    ellipse(x - 250, 75, 750, 30)
    ellipse(x - 200, 50, 1000, 20)
    #middle cloud
    ellipse(mcloud - 500, 200, 1000, 50)
    ellipse(mcloud - 250, 210, 750, 50)
    ellipse(mcloud - 500, 250, 2000, 100)
    

    #torii Shrine
    stroke(128, 0, 0)
    strokeWeight(2)
    fill(128, 0, 0)
    #torii shrine pole 1 (70 pixel gap from top and bottom
    quad(680, 880, 750, 446, 800, 446, 730, 880)
    #torii shrine middle section
    rect(650, 546, 635, 35)
    #torii shrine pole 2)
    quad(1210, 880, 1140, 446, 1190, 446, 1260, 880)
    #torii Shrine top red
    quad(630, 446, 1305, 446, 1285, 481, 650, 481)
    #torii shrine middle connector
    rect(960, 470, 35, 100)
    #torii shrine middle connector shade
    stroke(0, 0, 0, 0)
    strokeWeight(0)
    fill(255, 255, 255, 50)
    rect(978, 482, 18, 65)
    #torri shrine top black
    stroke(0, 0, 0)
    fill(0, 0, 0)
    quad(610, 430, 1325, 430, 1305, 465, 630, 465)
    #torii shrine lighting
    stroke(255, 255, 255, 50)
    strokeWeight(1)
    fill(255, 255, 255, 50)
    quad(1206, 545, 1198, 482, 1180, 482, 1188, 545)
    quad(1260, 880, 1213, 585, 1195, 585, 1244, 880)
    #Torii shrine lighting 2 left
    quad(765, 545, 785, 545, 795, 482, 775, 482)
    quad(715, 880, 760, 585, 779, 585, 730, 880)

    #in front of the mountain
    strokeWeight(2)
    fill(181,155,44)
    rect(0, 870, 1919, 2020)

    #path
    fill(75, 75, 75)
    quad(650, 1000, 680, 870, 1260, 870, 1290, 1000)

    #pink leaves behind branch
    stroke(255, 183, 197)
    strokeWeight(2)
    fill(255, 183, 197)
    ellipse(0, 0, 250, 50)
    #branch 1 back
    ellipse(190, 0, 100, 100)
    ellipse(200, 20, 75, 75)
    ellipse(370, 200, 85, 85)
    ellipse(350, 200, 95, 95)
    ellipse(280, 100, 105, 105)
    ellipse(330, 60, 100, 100)
    ellipse(405, 210, 85, 85)
    ellipse(330, 60, 85, 85)
    ellipse(350, 50, 100, 100)
    #branch 2
    ellipse(690, 180, 75, 75)
    ellipse(670, 180, 105, 105)
    ellipse(655, 125, 95, 95)
    ellipse(515, 70, 85, 85)
    ellipse(495, 50, 85, 85)
    ellipse(580, 160, 95, 95)
    #branch 3
    ellipse(630, 0, 100, 100)
    ellipse(1070, 40, 90, 90)
    ellipse(1240, 40, 85, 85)
    ellipse(1070, 60, 75, 75)
    ellipse(1065, 45, 75, 75)

    #sakura tree
    stroke(89, 29, 29)
    strokeWeight(2)
    fill(89, 29, 29)
    quad(0, 1000, 200, 1000, 100, 800, 50, 200)
    quad(0, 1000, 50, 200, 50, 0, 0, 0)
    #branch 1
    quad(190, 0, 210, 0, 370, 200, 350, 200)
    quad(200, 0, 350, 200, 350, 250, 370, 200)
    quad(360, 190, 395, 200, 405, 210, 365, 205)
    quad(280, 100, 290, 100, 300, 210, 290, 200)
    quad(250, 50, 250, 60, 330, 60, 350, 50)
    #branch 2
    quad(380, 0, 400, 0, 690, 180, 670, 180)
    quad(670, 180, 670, 230, 690, 180, 690, 180)
    quad(520, 80, 690, 150, 655, 125, 515, 70)
    quad(520, 80, 580, 160, 545, 100, 515, 70)
    quad(420, 20, 495, 40, 420, 25, 420, 20)
    #branch 3
    quad(630, 0, 670, 0, 1070, 40, 1060, 50)
    quad(1060, 50, 1070, 40, 1065, 45, 1070, 60)
    quad(1070, 40, 1060, 50, 1260, 50, 1240, 40)
    quad(890, 25, 900, 35, 990, 50, 1000, 50)

    #pink leaves front branch
    stroke(255, 183, 197)
    strokeWeight(2)
    fill(255, 183, 197)
    #branch 1
    ellipse(360, 190, 35, 35)
    ellipse(405, 210, 25, 25)
    ellipse(300, 210, 24, 24)
    ellipse(250, 60, 25, 25)
    ellipse(250, 50, 25, 25)
    ellipse(290, 100, 45, 45)
    ellipse(350, 200, 30, 30)
    ellipse(190, 0, 25, 25)
    ellipse(200, 20, 35, 35)
    ellipse(370, 200, 35, 35)
    ellipse(350, 200, 35, 35)
    ellipse(360, 250, 45, 45)
    #branch 2
    ellipse(580, 160, 45, 45)
    ellipse(670, 180, 24, 24)
    ellipse(670, 230, 35, 35)
    ellipse(515, 70, 45, 45)
    #branch 3
    ellipse(890, 25, 70, 70)
    ellipse(990, 50, 55, 55)

    x += 1

    if x > 2650:
        x = -2000

    x2 -= 2.5

    if x2 < -5000:
        x2 = 2500
        
    mcloud += 0.5
    
    if mcloud > 2650:
        mcloud = -3000
