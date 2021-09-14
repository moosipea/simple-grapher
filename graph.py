import pyxel as px

px.init(256, 256, fps=60, caption="graph")

STEP = 1
DEPTH = 256
ZOOM = 5

points = []

drawing = True

def genPoints():

    y = 0
    x = -DEPTH
    a = 3

    for i in range(DEPTH * 2):

        #expression
        y = 0.3*x**2


        points.append((int(x * ZOOM), int(y * ZOOM)))
        x += STEP


genPoints()
#print(points)
def update():
    if px.btnp(px.KEY_Q):
        px.quit()

def draw():
    px.cls(0)

    # draw axes
    px.line(0, px.height / 2, px.width, px.height / 2, 7)
    px.line(px.width / 2, 0, px.width / 2, px.height, 7)

    try:
        for i in range(len(points)):
            p1x = px.width / 2 + max(min(points[i][0], px.width), -(px.width / 2))
            p1y = px.height / 2 - max(min(points[i][1], px.height), 0)

            p2x = px.width / 2 + max(min(points[i + 1][0], px.width), -(px.width / 2))
            p2y = px.height / 2 - max(min(points[i + 1][1], px.height), 0)
            
            px.line(p1x, p1y, p2x, p2y, 3)
    except IndexError:
        pass


px.run(update, draw)