from tkinter import *
import time

class Ball:
	def __init__(self, canvas, color, size, x, y, xspeed, yspeed):
		self.canvas=canvas	#캔버스 객체
		self.color="red"	
		self.size=size	
		self.x=x
		self.y=y
		self.xspeed=xspeed	#ball의 수평 방향 속도
		self.yspeed=yspeed	#ball의 수평 방향 속도
		self.id=canvas.create_oval(x,y,x+size,y+size,fill=color)
	def move(self):		#ball을 이동시키는 함수
		self.canvas.move(self.id, self.xspeed, self.yspeed)
		(x1,y1,x2,y2)=self.canvas.coords(self.id)	#공의 현재 위치 얻는다
		(self.x,self.y)=(x1,y1)
		if x1 <= 0 or x2 >= WIDTH:	#공의 x좌표가 음수이거나 x좌표가 오른쪽 경계를 넘으면
			self.xspeed=-self.xspeed	#속도의 부호를 반전시킨다

WIDTH=800
HEIGHT=400

window=Tk()
canvas=Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
ball=Ball(canvas, "red", 30, 0, 0, 10, 0)

while True:	#메인 루프
	ball.move()
	window.update()
	time.sleep(0.03)


