#Machine Problem 5
#Prof. Mike Liljegren
#Mehul Antony

#Description: This script will use the cs1graphics module to create a graphics
#scene and then animate the scene. The scene consists of a sun, cloud, cactus, and two
#camels. The sun and Cloud are Circles; the Cloud, Camels, and Cactus are created
#using the layer class to combine multiple objects. The initial scene consists of the
#cloud moving, after which a camel moves a certain distance and stops, followed by
#another camel entering the scene and exiting.

from cs1graphics import *
from time import sleep

#The main program of the code creates a canvas object,
#and adds all the functions written below to the object.
#There are no parameters, and the object is returned.
def makeCanvas():
    object = Canvas(1000, 1000)
    object.setBackgroundColor('azure3')
    object.add(makeSand())
    object.add(makeSun())
    
    cloud_layer = create_cloud()
    object.add(cloud_layer)
    camel_1 = makeCamel()
    camel_1.moveTo(250, 100)
    camel_2 = camel_1.clone()
    camel_2.moveTo(500, 250)
    object.add(camel_1)
    object.add(camel_2)
    object.add(makeShrub())

    move_cloud(cloud_layer)
    camel_movement(camel_1)
    camel_movement_2(camel_2)

    return object


#The makeSand() function creates a rectangle on the lower-portion
#of the screen which represents a desert. There are no parameters,
#and the sand object is returned.
def makeSand():
    sand = Rectangle(1600, 450, Point(800, 750))
    sand.setFillColor('orange3')
    sand.setBorderColor('orange3')
    return sand

#The create_cloud() function creates a cloud object by using 
#the Layer() class to combine multiple objects.
#These objects are ndividual circles. 
#A for-loop is used to set properties
#for these circles, and to add them back to the cloud object.
#There are no parameters. The cloud object is returned.
def create_cloud():
    cloud = Layer()
    
    cloud1 = Circle(40)
    cloud2 = Circle(40)
    cloud3 = Circle(40)
    
    for shape in [cloud1, cloud2, cloud3]:
        shape.setFillColor('white')
        shape.setBorderColor('white')
    
    cloud1.moveTo(500, 100)
    cloud2.moveTo(550, 130)
    cloud3.moveTo(600, 100)
    
    for shape in [cloud1, cloud2, cloud3]:
        cloud.add(shape)
    
    return cloud

#The makeSun() function creates a Sun, 
#which is located on the top-left
#of the screen. There are no parameters. 
#The sun object is returned.
def makeSun():
    sun = Circle(50, Point(250, 70))
    sun.setFillColor('yellow')
    sun.setBorderWidth(0)
    return sun

#The makeCamel() function creates a camel object
#by using the Layer() class. We create the individual
#objects to represent the head, eyes, neck, body, hump,
#and legs respectively. There are no parameters. The camel
#object is returned.
def makeCamel():
    camel = Layer()
    camel.setDepth(12)

    #camel head
    camel_head = Ellipse(w=50, h=35)
    camel_head.setFillColor('orange')
    camel_head.setBorderColor('orange')
    
    camel_head.moveTo(550, 300)
    camel.add(camel_head)

    #camel eyes
    camel_eye = Circle(1)
    camel_eye.setFillColor('black')
    camel_eye.moveTo(537, 296)
    camel.add(camel_eye)

    #camel neck
    camel_neck = Ellipse(w=25, h=80)
    camel_neck.setFillColor('orange')
    camel_neck.setBorderColor('orange')
    camel_neck.moveTo(560, 345)
    camel.add(camel_neck)

    #camel body
    camel_body = Ellipse(w=150, h=100)
    camel_body.setFillColor('orange')
    camel_body.setBorderColor('orange')
    camel_body.moveTo(630, 390)
    camel.add(camel_body)

    #camel hump
    vertex_1 = Point(30, 90)
    vertex_2 = Point(75, 150)
    vertex_3 = Point(105, 90)
    camel_hump = Polygon(vertex_1, vertex_2, vertex_3) #counter-clockwise
    camel_hump.setFillColor('orange')
    camel_hump.setBorderColor('orange')
    camel_hump.rotate(180)
    camel_hump.moveTo(670, 345)
    camel.add(camel_hump)

    #camel legs
    first_point = Point(570, 400)
    second_point = Point(550, 570)

    line_1 = Path(first_point, second_point)
    line_1.setBorderColor('black')
    line_2 = line_1.clone()
    line_3 = line_1.clone()
    line_4 = line_1.clone()

    line_2.moveTo(620, 400)
    line_2.rotate(10)
    line_3.moveTo(630, 400)
    line_3.rotate(-10)
    line_4.moveTo(700, 400)

    camel.add(line_1)
    camel.add(line_2)
    camel.add(line_3)
    camel.add(line_4)
    
    return camel

#The makeShrub() function creates a cactus object using
#the Layer() class. Two points are created and we use the
#Path class to connect these two points and create a line.
#This line is cloned thrice by using the clone function,
#its properties are set, and added to the cactus object. 
#There are no parameters.
#The cactus object is returned.
def makeShrub():
    cactus = Layer()

    point_1 = Point(200, 330)
    point_2 = Point(180, 550)

    line_1 = Path(point_1, point_2)
    line_1.setBorderColor('green')
    line_1.setBorderWidth(35)
    line_1.rotate(-4)

    line_2 = line_1.clone()
    line_2.moveTo(100, 285)
    line_2.rotate(-25)

    line_3 = line_1.clone()
    line_3.moveTo(330, 285)
    line_3.rotate(33)

    cactus.add(line_1)
    cactus.add(line_2)
    cactus.add(line_3)
    
    return cactus

#The camel_movement(camel) function specifies a 
#timeDelay of 0.20s and starts from a direction of 
#-30. We use a for-loop to ensure that the camel moves
#towards the left and stops after 10 steps. The sleep function
#is used for the time delay to animate the camel.

#Parameter-camel,which will be the return value of the makeCamel()
#function written in the main program.
#There is no return statement.
def camel_movement(camel):
    timeDelay=0.20
    
    direction_start = -30
    
    for i in range(10):
        camel.move(direction_start - 10, 0)
        sleep(timeDelay)

#The camel_movement_2(camel) function is similar to
#the camel_movement(camel) function written above,
#except that the second camel moves a total of 32 steps.
def camel_movement_2(camel):
    timeDelay=0.20
    
    direction_start = -30
    
    for i in range(32):
        camel.move(direction_start - 10, 0)
        sleep(timeDelay)

#The move_cloud(cloud) function specifies a time delay of
#0.15s. We use a for-loop to ensure that the cloud moves
#a distance of 20 to the right. The sleep function
#is used for the time delay to animate the cloud.

#Paramter-cloud, which is the return value of the 
#create_cloud function written in the main program.
def move_cloud(cloud):
    timeDelay = 0.15
    for i in range(20):
        cloud.move(10, 0)
        sleep(timeDelay)

canvas = makeCanvas()
canvas.wait()
