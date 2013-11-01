Python_Battle_For_Uranus_Game
=============================

a simple python game

The controls for the battlecruiser:
-----------------------------------
  * LEFT ARROW: Moves the battlecruiser to the left of the screen (in the x-direction)
  * RIGHT ARROW: Moves the battlecruiser to the right of the screen (in the x-direction)
  * UP ARROW: Moves the battlecruiser up the screen (in the y-direction)
  * DOWN ARROW: Moves the battlecruiser down the screen (in the y-direction)
  * SPACE BAR: Fires a laser. 
    Important: the battlecruiser can fire multiple lasers. That is, more than one laser can be drawn on one frame!
  * ESC: Quit
  
* Running the laser module via python Laser.py shall launch a 800x600 window with a black background, with a barrage of lasers randomly going from down the screen to up.
* Running the battlecruiser module via python Battlecruiser.py shall launch a 800x600 window with a black background, allowing you to control the battlecruiser with the controls as noted above.

* Running the enemy module via python Enemy.py shall launch a 800x600 window with a white background, with ten (10) enemies bouncing off the walls, elastic collision.
* If a laser is fired, the sound asset laser.wav shall be played.
* If the battlecruiser collides with an enemy, the game is over and the sound asset death_explode.wav is played.
* If a laser collides with an enemy on the screen, 100 points is awarded.
* The game score shall be rendered near the upper-left corner of the screen with a font color that is not black!
