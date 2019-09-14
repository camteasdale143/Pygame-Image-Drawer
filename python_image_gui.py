import pygame
import math
import csv

surface = pygame.display.set_mode((500,842))
pygame.display.flip()
mouse = pygame.mouse
log_file = open("assignment_script.py", "w");

running = True
colors = []
backgroundColor = (0,0,0)
savedmouse = 0;
color_pos= (4,16);
fill_color = (255,255,255);
color_name = "White";

mouse_data = [(0,0),(0,0)];
poly_points = [];

rects = []
circs = []
ellis = []
fills = []
polys = []
order = []

draw_state = "rect";

with open('color.csv') as csv_file:
    print("Loading Colors")
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
       colors.append(row)
    print("Colors Loaded")


log_file.write("""import pygame\n\nsurface = pygame.display.set_mode((500,500))\n""")
        
def drawRect():
    rects.append(((surface, fill_color, pygame.Rect(mouse_data[0][0], mouse_data[0][1], mouse_data[1][0] - mouse_data[0][0],mouse_data[1][1] - mouse_data[0][1])), color_name ))
    order.append(("rect", len(rects) - 1))
def drawCirc():
    delta_vectors = (mouse_data[1][0] - mouse_data[0][0],mouse_data[1][1] - mouse_data[0][1])
    circs.append(((surface, fill_color, mouse_data[0], dist(delta_vectors)),color_name))
    order.append(("circ", len(circs) - 1))
def drawElli():
    ellis.append(((surface, fill_color, pygame.Rect(mouse_data[0][0], mouse_data[0][1], abs(mouse_data[1][0] - mouse_data[0][0]),(mouse_data[1][1] - mouse_data[0][1]))), color_name))
    order.append(("elli", len(ellis) - 1))
def drawFill():
    global backgroundColor
    backgroundColor = fill_color 
def drawPoly():
    global poly_points
    if (poly_points == []):
        rects.append(((surface, fill_color, pygame.Rect(mouse_data[1][0],mouse_data[1][1], 1,1)), color_name))
        order.append(("rect", len(rects) - 1))
        poly_points.append(mouse_data[1])
    elif (abs(dist((poly_points[0][0] - mouse_data[1][0],poly_points[0][1] - mouse_data[1][1]))) > 20 or len(poly_points) < 3):
        rects.append(((surface, fill_color, pygame.Rect(mouse_data[1][0],mouse_data[1][1], 1,1)), color_name))
        order.append(("rect", len(rects) - 1))
        poly_points.append(mouse_data[1])
    else:
        polys.append(((surface, fill_color, poly_points), color_name))
        poly_points = []
        order.append(("poly", len(polys) - 1))

def dist(tup):
    return int(math.sqrt(tup[0]*tup[0] + tup[1]*tup[1]))


def click():
    mouse_data[0] = mouse.get_pos()

def unclick(): 
    global poly_points
    mouse_data[1] = mouse.get_pos()
    if draw_state == "rect":
        drawRect()
    if draw_state == "circ":
        drawCirc()
    if draw_state == "elli":
        drawElli()
    if draw_state == "fill":
        drawFill()
    if draw_state == "poly":
        drawPoly()


def updateColor(index, direction):
    global color_pos
    global fill_color
    global color_name
    if index == 0:
        color_pos = (color_pos[0] + direction, color_pos[1])
    else:
        color_pos = (color_pos[0] , color_pos[1] + direction)
    fill_color = pygame.Color(colors[color_pos[0] + color_pos[1]*10][0])
    color_name = colors[color_pos[0] + color_pos[1]*10][1]
    print(color_name)

def keyboard():
    if event.type == pygame.KEYDOWN:
        global draw_state
        if event.key == pygame.K_u and len(order) > 0:
            s = order[len(order) - 1] 
            if (s[0] == "rect" and len(rects) > 0):
                rects.pop()
                order.pop()
            elif (s[0] == "circ"and len(circs) > 0):
                circs.pop()
                order.pop()
            elif (s[0] == "elli"and len(ellis) > 0):
                ellis.pop()
                order.pop()
            elif (s[0] == "poly"and len(polys) > 0):
                polys.pop()
                order.pop()

            
        if event.key == pygame.K_r:
            draw_state = "rect"
            print("rect mode");
        if event.key == pygame.K_c:
            draw_state = "circ"
            print("circ mode");
        if event.key == pygame.K_e:
            draw_state = "elli"
            print("elli mode");
        if event.key == pygame.K_f:
            draw_state = "fill"
            print("fill mode")
        if event.key == pygame.K_p:
            draw_state = "poly"
            print("poly mode")
        if event.key == pygame.K_UP:
            updateColor(1,-1)
        if event.key == pygame.K_RIGHT:
            updateColor(0,1)
        if event.key == pygame.K_LEFT:
            updateColor(0,-1)
        if event.key == pygame.K_DOWN:
            updateColor(1,1)
            
def background():
    surface.fill(backgroundColor, pygame.Rect(0,0,500,500))
    surface.fill(fill_color, pygame.Rect(0, 500, 500, 842))
    
def pallet():
    for y in range(0, 34):
        for x in range(0,10):
            pygame.draw.rect(surface, pygame.Color(colors[x + y*10][0]), pygame.Rect(x*10, 500 + y*10, 10,10))
    pygame.draw.rect(surface, (0,0,0), pygame.Rect(color_pos[0]*10, color_pos[1]*10 + 500, 10, 10))

def draw(): 
    background()
    pallet()
    for s in order:
        if s[0] == "rect":
            pygame.draw.rect(*rects[s[1]][0])
        if s[0] == "circ":
            pygame.draw.circle(*circs[s[1]][0])
        if s[0] == "elli":
            pygame.draw.ellipse(*ellis[s[1]][0])
        if s[0] == "poly":
            pygame.draw.polygon(*polys[s[1]][0])
        
            
    
background()
pallet()

while running:
    for event in pygame.event.get():

        if mouse.get_pressed()[0] == 1 and savedmouse == 0:
            savedmouse = 1
            click()
        elif mouse.get_pressed()[0] == 0 and savedmouse == 1:
            savedmouse = 0
            unclick()
        keyboard()    
        draw()
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()


def write_drawing(): 
    drawString = ""
    print(backgroundColor)
    drawString += "surface.fill({0})\n".format(backgroundColor)
    for s in order:
        if s[0] == "rect":
            rectangle = rects[s[1]]
            drawString += "#Rectangle drawn with color: {0}\n".format(rectangle[1])
            drawString += "pygame.draw.rect(surface, {0}, pygame.Rect({1}, {2}, {3}, {4}))\n\n".format(rectangle[0][1], rectangle[0][2][0],rectangle[0][2][1], rectangle[0][2][2], rectangle[0][2][3])
        if s[0] == "circ":
            circle = circs[s[1]]
            drawString += "#Circle drawn with color: {0}\n".format(circle[1])
            drawString += "pygame.draw.circle(surface, {0}, {1}, {2})\n\n".format(circle[0][1], circle[0][2], circle[0][3])
        if s[0] == "elli":
            ellipse = ellis[s[1]]
            drawString += "#Ellipse drawn with color: {0}\n".format(ellipse[1])
            drawString +=  "pygame.draw.ellipse(surface, {0}, pygame.Rect({1}, {2}, {3}, {4}))\n\n".format(ellipse[0][1], ellipse[0][2][0],ellipse[0][2][1], ellipse[0][2][2], ellipse[0][2][3])
        if s[0] == "poly":
            polygon = polys[s[1]]
            drawString += "#Rectangle drawn with color: {0}\n".format(polygon[1])
            drawString += "pygame.draw.polygon(surface, {0}, {1})\n\n".format(polygon[0][1], polygon[0][2])
    log_file.write(drawString)
    print("saved image")

write_drawing()
log_file.write("\npygame.display.update()\npygame.time.delay(3000)\npygame.image.save(surface, 'house_101147632.bmp')")
