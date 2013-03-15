"""
Aliens have invaded a space ship and our hero has to go through a maze of
rooms defeating them so he can escape into an escape pod to the planet
below.  The game will be more like a Zork or Adventure type game with text
outputs and funny ways to die.  The game will involve an engine that runs a
map full of rooms or scenes.  Each room will print its own description
when the player enters it and then tell the engine what room to run
next out of the map.


* Map
  - next_scene
  - opening_scene
* Engine
  - play
* Scene
  - enter
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * The Bridge
  * Escape Pod
  
"""
from sys import exit

class Engine(object):
	
	def __init__(self, scene_map):
		pass
	
	def play(self):
		print "You are in a dark room. Do you cry out for help or stay silent?"
		answer = raw_input('> ')
		if "help" in answer:
			print "You hear a growl. What do you do next? Go left or right?"
			answer = raw_input('> ')
			if "left" in answer:
				print "You made it! By sheer fluke you avoided the werewolves"
				CentralCorridor.enter(self)
			else:
				print "You dead! Werewolves got you. Bye"
				exit(0)
		elif "silent" in answer:
			print "You can hear a pipe dripping."
			Engine.play(self)
		else:
			print "\nThe blackness haunts you.\n"
			Engine.play(self)
		

class Scene(object):

	def enter(self):
		pass
		
class Death(Scene):
	
	def enter(self):
		print "You are in Hades. Bad luck old chap."

class CentralCorridor(Scene):
	
	def enter(self):
		print "You are in the central corridor"
		
class LaserWeaponArmory(Scene):
	
	def enter(self):
		pass

class TheBridge(Scene):
	
	def enter(self):
		pass

class EscapePod(Scene):
	
	def enter(self):
		pass
	

class Map(object):

	def __init__(self, start_scene):
		pass
	
	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass
		

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()