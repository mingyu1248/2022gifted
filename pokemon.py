Web VPython 3.2
images = ['https://cdn.econovill.com/news/photo/201603/285365_95988_038.png','https://cdn.banggooso.com/assets/images/game96/result/ESTJ.png']
a =arrow(pos = vec(0,2,0), axis = vec(0,-1,0), color = color. white)
p = box(texture = images[0])
g = box(pos = vec(1,0,0), texture =images[1])

i=0
while True :
    rate(8)
    k = keysdown()
    a.pos.x = i % 2

    i = i + 1
    if i%2 == 0:
        p.color = color.black
        g.color = color.white
    else:
        p.color = color.white
        g.color = color.black
    if ' ' in k:
        print('당첨되셨습니다')
        break
