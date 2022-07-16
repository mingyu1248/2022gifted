Web VPython 3.2
box(size = vec(160,1,160), texture = textures.earth)
a1 = arrow(axis = vec(10,0,0), color = color.red, pos = vec(-80,1,0))
a2 = arrow(axis = vec(0,10,0), color = color.blue, pos = vec(-80,1,0))
a3 = arrow(pos = vec(-80,1,0))
a3.axis = a1.axis + a2.axis
ball = sphere(make_trail = True, pos = vec(-80,1,0), size=vec(3,3,3))
p = label()
s = False
f = False
import random
b=box()
b_list = []
t = box( pos = vec(80,30,0), color = color.blue,size = vec(5,5,5))
t.v = vec(0,-10,0)
for i in range(20) :
    x = random.randint(-70, 70)
    y = random.randint(1,30)
    b_list.append(box(pos = vec(x,y,0),size = vec(3,3,3)))

while f == False :
    p.text = ball.pos
    p.pos = vec(3,90,0)
    t.pos += t.v *0.01
    rate(100)
    k = keysdown()
    if 'right' in k :
        a3.axis.x += 0.1
    if 'left' in k :
        a3.axis.x -= 0.1
    if 'up' in k :
        a3.axis.y += 0.1
    if 'down' in k :
        a3.axis.y -= 0.1
    if t.pos.y <= 1.5:
        t.v.y *= -1
    t.v.y += -9.8 *0.01
    if ' ' in k :
        s = True
    if s == True :     
        ball.color = color.red
        ball.v = a3.axis
        ball.pos = ball.pos + ball.v * 0.01
        if ball.pos.y <= 0 :
            label(text = 'fail')
            f = True
        else :
            ball.v.y = ball.v.y + -9.8 * 0.01
        if mag(ball.pos- t.pos)<=5:
            label(text = 'success')
            f= True
        for i in range(20):
            if mag(ball.pos- b_list[i].pos)<=3:
                label(text = 'fail')
                f= True
        
