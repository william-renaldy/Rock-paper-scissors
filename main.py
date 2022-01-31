import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
import random

Window.clearcolor=(1,1,1,1)
class mygrid(GridLayout):
	def __init__(self,**kwargs):
		super(mygrid,self).__init__(**kwargs)
		x=Window.size[0]
		y=Window.size[1]
		self.player_score=0
		self.computer_score=0
		self.turn=0
		self.cols=1
		self.add_widget(Label(text='Rock - Paper - Scissors',color=(0,0,0,1),font_size=x/12,size_hint_y=None,height=y/5,bold=True))
		self.add_widget(Label(text='Total points = 10',size_hint_y=None,height=y/20,font_size=x/18,color=(0,0,0,1)))
		
		self.score=Label(text='0 - 0',size_hint_y=None,height=y/20,font_size=x/15,color=(0,0,0,1),bold=True)
		self.add_widget(self.score)
		
		self.play_box=GridLayout(cols=2,size_hint_y=None,height=3*y/10)
		self.play_box.add_widget(Label(text="Player input:",color=(0,0,0,1),size_hint_y=None,height=y/10,font_size=x/15))

		self.play_box.add_widget(Label(text="Computer input:",color=(0,0,0,1),size_hint_y=None,height=y/10,font_size=x/15))
		self.player=Image(source='Startup.png',allow_stretch=True,size_hint_y=None,height=y/5)
		self.play_box.add_widget(self.player)
		
		self.computer=Image(source='Startup.png',allow_stretch=True,size_hint_y=None,height=y/5)
		self.play_box.add_widget(self.computer)
		self.add_widget(self.play_box)
		
		self.buttons=GridLayout(cols=5,size_hint_y=None,height=y/10)
		self.add_widget(self.buttons)
		self.buttons.add_widget(Label(size_hint_x=None,width=x/10))
		self.rock=Button(text="Rock",background_color=(0,0,0,0.8))
		self.buttons.add_widget(self.rock)
		self.paper=Button(text='Paper',background_color=(0,0,0,0.8))
		self.buttons.add_widget(self.paper)
		self.scissor=Button(text='Scissors',background_color=(0,0,0,0.8))
		self.buttons.add_widget(self.scissor)
		self.buttons.add_widget(Label(size_hint_x=None,width=x/10))
		self.rock.bind(on_press=self.player_fun)
		self.paper.bind(on_press=self.player_fun)
		self.scissor.bind(on_press=self.player_fun)
		
		self.turns_left=Label(text='Turns left = 10',color=(0,0,0,1),size_hint_y=None,height=y/14,font_size=x/20)
		self.add_widget(self.turns_left)
		self.res=Label(color=(0,0,0,1),size_hint_y=None,height=y/10,font_size=x/20)
		self.add_widget(self.res)
		self.playagain=GridLayout(cols=3,size_hint_y=None,height=y/11)
		self.playagain.add_widget(Label())
		self.reset=Button(text='Reset',background_color=(1,0,1,1))
		self.reset.bind(on_press=self.reset_fun)
		self.playagain.add_widget(self.reset)
		self.playagain.add_widget(Label())
		self.add_widget(self.playagain)
		
		
	def reset_fun(self,instance):
		self.turn=0
		self.player.source='Startup.png'
		self.computer.source='Startup.png'
		self.player_score=0
		self.computer_score=0
		self.score.text='0 - 0'
		self.turns_left.text='Turns left = 10'
		self.res.text=' '
		self.reset.text='Reset'
		
		
		
		
		
	def result(self,player,computer):
		if player==computer:
			win=None
		elif (player=='R' and computer=='P') or (player=='S' and computer=='R') or (player=='P' and computer=='S'):
			win='Computer'
			self.computer_score+=1
		elif (player=='P' and computer=='R') or (player=='R' and computer=='S') or (player=='S' and computer=='P'):
			win='Player'
			self.player_score+=1
		self.score.text='{} - {}'.format(self.player_score,self.computer_score)
		if self.turn==10:
			if self.player_score==self.computer_score:
				self.res.text='Game over!! Game drawn'
			else:
				self.res.text='Game over!! {} won the game'.format('Player' if self.player_score>self.computer_score else 'Computer')
			self.reset.text='Play again'
				
			

		
	def computer_fun(self,player):
		com_list=('Computer_rock.jpg','Computer_paper.jpg','Computer_scissor.jpg')
		choice=random.choice(com_list)
		self.computer.source=choice
		if choice=='Computer_rock.jpg':
			self.result(player,'R')
		elif choice=='Computer_paper.jpg':
			self.result(player,'P')
		elif choice=='Computer_scissor.jpg':
			self.result(player,'S')
		
	def player_fun(self,button):
		self.turn+=1
		if self.turn<=10:
			self.turns_left.text='Turns left = {}'.format(str(10-self.turn))
			if button.text=='Rock':
				self.player.source='Player_rock.jpg'
				player='R'
				
			elif button.text=='Paper':
				self.player.source='Player_paper.jpg'
				player='P'
				
			elif button.text=='Scissors':
				self.player.source='Player_scissor.jpg'
				player='S'
			c_choice=self.computer_fun(player)
		else:
			pass
		
		
		
class myapp(App):
	def build(self):
		return mygrid()

if __name__=='__main__':
	myapp().run()