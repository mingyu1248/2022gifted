Web VPython 3.2
def move(obj) : 
    k = keysdown()
    if 'up' in k : 
        obj.pos.x += 0.05
    if 'down' in k:
        obj.pos.x -= 0.05
    if 'left' in k: 
        obj.pos.z -= 0.05
    if 'right' in k:
        obj.pos.z += 0.05
    if 'n' in k : 
        obj.pos.y += 0.05
    if 'm' in k : 
        obj.pos.y -= 0.05

x = sphere(color = color.cyan, radius = 0.2, emissive = True)
attach_light(x)
rings = []

for i in range(50): 
    rings.append(ring(pos = vec(i,0,0), color = vec(i,i*2,i*3)))
    colors = [ color = vec(i,i*2,i*3)]


while True :
    rate(100)
    move(x)
    scene.camera.pos = x.pos - vec(2,0,0)
    scene.camera.axis = vec(1,0,0)
   
