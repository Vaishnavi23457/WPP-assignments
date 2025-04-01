import math

class Vec2D:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def magt(self):
        return math.sqrt(self.x*2 + self.y*2)

    def angle(self):
        return math.degrees(math.atan2(self.y, self.x))

    def dis(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot_pro(self, other):
        return self.x * other.x + self.y * other.y

    def cross_pro(self, other):
        return self.x * other.y - self.y * other.x

    def _repr_(self):
        return f"Vector2D({self.x}, {self.y})"

class Vec3D(Vec2D):
    def _init_(self, x, y, z):
        super()._init_(x, y)
        self.z = z

    def magt(self):
        return math.sqrt(self.x*2 + self.y2 + self.z*2)

    def dot_pro(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_pro(self, other):
        return Vec3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def dis(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def _repr_(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
k=1
while k!=0:
    op=int(input("do you want to perform \n2.2D vector opretion\n3.3D vector opretion 0.exit: "))
    if(op==2):
        x=int(input("enter your x axis cofficent"))
        y=int(input("enter your Y axis cofficent"))
        v1=Vec2D(x,y)
        choise=int(input("press\n1.megnitute\n2.angle from x axis\n3.distance\n4.dot-product\n5.cross-product\n0.exit: "))
        while choise!=0:
            if choise==1:
                print("Magnitude of v1:", v1.magt())
            elif choise==2:
                print("Angle with X-axis:", v1.angle())
            elif choise==0:
                break
            else:
                x=int(input("enter your x axis cofficent"))
                y=int(input("enter your y axis cofficent"))
                v2=Vec2D(x,y)
                if choise==3:
                    print("Distance:", v1.dis(v2))
                elif choise==4:
                    print("Dot Product:", v1.dot_pro(v2))
                elif choise==5:
                    print("Cross Product:", v1.cross_pro(v2))
            choise=int(input("press\n1.megnitute\n2.angle from x axis\n3.distance\n4.dot-product\n5.cross-product\n0.exit: "))
    elif op==3:
        x=int(input("enter your x axis cofficent"))
        y=int(input("enter your y axis cofficent"))
        z=int(input("enter your z axis cofficent"))
        v1=Vec3D(x,y,z)
        choise=int(input("press\n1.megnitute\n2.angle from x axis\n3.distance\n4.dot-product\n5.cross-product 0.exit:-"))
        while choise!=0:
            
            if choise==1:
                print("Magnitude of v1:", v1.magt())
            elif choise==2:
                print("Angle with X-axis:", v1.angle())
            else:
                x=int(input("enter your x axis cofficent"))
                y=int(input("enter your Y axis cofficent"))
                z=int(input("enter your Z axis cofficent"))
                v2=Vec3D(x,y,z)
                if choise==3:
                    print("Distance:", v1.dis(v2))
                elif choise==4:
                    print("Dot Product:", v1.dot_pro(v2))
                elif choise==5:
                    print("Cross Product:", v1.cross_pro(v2))
            choise=int(input("press\n1.megnitute\n2.angle from x axis\n3.distance\n4.dot-product\n5.cross-product\n0.exit: "))