""" standard lines I have been starting with. 
    These are explained below 

import time
from graphics import *
sys.path.append('C:/Users/Joseph H. Hendrickso/Documents/python')
from joe_utilities import *
from joe_graphics_utilities import *
from random import randint

win_size = 300
win = GraphWin('clock',2*win_size,2*win_size)
win.setCoords(-win_size,-win_size,win_size,win_size)

"""

"""
       ----  
       ----  subroutines
       ----
       
Terms used in programming change over time as people think they have
a very important, new idea and feel a new word is criticl to
conveying their insight.

The following words are essentially the same, and refer to a section
of code that you write as a separate unit.  It has its own name that
it is called by, and a "return" statement at the end to the computer
to the next line after it was called.:
    subroutine
    routine
    procedure
    function     - this implies that the routine returns a value
    method       - this is used to refer to routines that are
                   part of something called a "class."

For example:

    1)    name = "Joe the Magnificent."
          print( 5,")  My name is", name )

          Print() is a procedure.  It is being passed 3 values: an interger,
          a text or "string", and a variable that contains a string.  It
          should produce something like

          5 ) My name is Joe the Magnificent.

    2)   y = abs(-5)
         print(y)

         The function abs() has one input, the numberic value -5.
         It returns the value 5.  This value is stored in the variable y.
         
         If you put -5 on a number line, it is 5 units left of zero, while 5 is
         5 units to the right.  The "magnitude" of each is the same, 5 units,
         but the direction is different.  This magnitude is also called the
         absolute value of the number.  The function abs returns this
         absolute value.  So this examnple would print out 5.
        

    def  name ( var1, var2, var2 ):
        ... code here using var1, var2, var2

        return

    If the routine is a function, it also has a return value.

    def  name ( var1, var2, var2 ):
        ... code here using var1, var2, var2
        ... computes a value var

        return var

   The var1, var2, var2 are called parameters.  They are placholders
   for the values that the user supplies when the user call the
   proceudre.  When you write the procedure, you try to use simple
   descriptive names to help the user know what kinds of values they can use.

    Examples might be:

    def announce_winner( player1_name, player2_name, score1, score2):
       if score1 > score2:
           winner = player1_name
       elif score2 > score1:
           winner = player2_name
       else:
           print("The game is a tie!")
           return
       print ("The winner is " + winnder)
       return

    If you wanted to have a fucntion that also returned the name:

    def announce_winner( player1_name, player2_name, score1, score2):
       if score 1 == score2:
           print ("The game is a tie!")
           return 'tie'
       elif score1 > score2:
           winner = player1_name
       else: 
           winner = player2_name

       print ("The winner is " + winnder)

       return winner

Commands to run a rouitne is referred to as "calling" the routine.

Example calls look like:

    player1 = "Mary"
    player2 = 'Mike'
    player3 = 'Sally'
    
    scores = [15, 21, 23]                                                 ---- scores is a "list" of values.  v[0] = 15, v[1] = 21, and v[2] = 23
                                                                               counting from 0 is easier for the computer than counting from 1.
                                                                               
    # Call the procedure to show who did better between Mary and Sally
    announce_winner( player1 , player3 , score[0] , score[2] )            ---- Note, the names you pass don't have to match the parameter names

    highest_score = max ( [score1, score2, score3 ])                      ---- max is a standard Python subroutine that returns the smallest value
                                                                               of a list.
 
       
       ----  
       ----  classes
       ----

A class is a template for a structure you can use to hold 
the procedures and the variables that relate to a specific
concept.

This is useful in two ways.

1)  First it is a template.

    Consider the hands of a clock.  They are different, and
    have to be handled sperately.  But they have a lot in common.
    They all need to be rotated, even though the speed they
    rotate varies.  With a "class Hand" template, you define
    the basic parts of the had, and the functions to rotate them
    one time in the class.  Then you declare 3 different hands:
    an hour hand, a second hand, and a minute hand.  You just
    have to pass to the class parameter values that distiniquish
    them, like different speeds.

    The class itself is not a hand.  It does not do anything until
    you use it to create an "instance" of a hand, like a second hand.

2)  Secondly, it creates a structure.

    Even if you were to just want one copy of something, it can
    be a lot of help to have a structure that keeps all your
    related data values and your procedures together.

    For one thing, it helps you keep your code organized.

    For another, it lets you use one value to pass as a parameter
    to a procedure all your functions and data about something.

    Some languages that don't have classes have structures just
    because they are useful on their own.
    
       

Here is an example.  Point is a class defined by the
graphics package we us.  Be below is a simplified
version I call class Pt

class Pt():
    def __init__(self, x, y):                                         # ---- __init__ is a special procedure that is called whenever
        self.x = x                                                    #      Declare an instantiation of the class.  It is what builds
        self.y = y                                                    #      the new instance.  Its first parameter is always "self".
                                                                      #      It indicates that it call be called from outside the class.
                                                                      #      __init__ and __repr__ are both special, and can only by called
                                                                      #      in special cases.  __init__ is called when you declare an instance
                                                                      #      and __repr__ is called when you print an object of the class.
    
    def __repr__(self):                                               #---- this tells the print command what it should print if you print a Point.
        return "Point({}, {})".format(self.x, self.y)
        
    def draw(self, window):                                           #---- I cheated here by just calling the real Point class drtaw routine                           
        Point(x,y).draw(window)
        return 
    def undraw(self):                                                              
        Point(x,y).undraw()
        return 
        
    def move(self, dx, dy):
        self.undraw()
        self.x = self.x + dx
        self.y = self.y + dy
        self.draw(window)       
                
    def getX(self):
        return self.x
    def getY(self):
        return self.y

    
    
        
pt1 = Pt(10,10)
pt2 = Pt(120,17)

pt1.draw(win)
pt1.move(100,200)


 """      
    

    








"""
# We want access to libraries of pre-written utilities to help us.
#     time gives us access to the system clock
"""
import time

"""
# graphics.py is the graphics interface we use 
"""
from graphics import *

"""
# I have two utility pacakges I wrote.  Whenever I write a procedure
# that seems general enough that I think I might need it another time,
# I stick it here.
#
# Some are to do math calculations for you.
"""
sys.path.append('C:/Users/Joseph H. Hendrickso/Documents/python')
from joe_utilities import *
from joe_graphics_utilities import *

"""
# Give access to randint
# We don't need that in this program.
# It is just part of the standard list I
# have been using.
"""
from random import randint

"""
# GraphWin makes a graphics window for us to use.
# We tell it that we want one that is 600x600 pixels
# We set the coordinates to go from -300 to 300 left to right
# and 300 to -300 top to bottom
"""
win_size = 300
win = GraphWin('clock',2*win_size,2*win_size)
win.setCoords(-win_size,-win_size,win_size,win_size)

"""
# Constants
#
# I don't know that python has real constants that cannot be changed.
# But these are variables that we don't intend to change.
# Making them all capitals is a convention to remind you.
# Putting them at the very top makes it easy to find.
# If yu put them at the top and never change them, python gives you
# access to them from anywhere in the file. If you change them anywhere,
# then you only have access in the procedure where you changed it.
#
"""
DIGITAL_CLOCK_POSITION = Point(-300,300)  # top left point of digital display
DIGITAL_BOX_HEIGHT     = 25 # We need three bozes to Hours, Minutes, and Seconds.
DIGITAL_BOX_WIDTH      = 30
DIGITAl_BOX_COLOR      = 'yellow'


"""
# Our digital clock needs to display three numbers: hours, minutes, seconds.
# So our display will be made up of three sections.  I call each section a box.
# Since we will need three of them, and will need code to access each one,
# it is easiest to define a template for a 'box'.  This template is called
# a class.  It contains all the data and procedures that we need to create and
# use a 'box'.
# 
# This has two advantages.  First, we only have to write the code one time.
# For each box, we just use the class to create a new box for us.
#
# Secondly, it keeps all the data and procedures for a given box organized in
# one place.  Some languages have a seperate concept just to do this, called a
# structure.  I don't see that python has this, but you can use a class for that
# even if you only need one copy of something.
#
"""
class Box:
    """
    Every class has a special function that is run when you use the class to
    create an object.  This is the function that actuall makes the object.  

    It's first input is always. "self".  Having the self input value means
    that it can use variables in the __init__ procedure that start with
    "self."  Functions with the self input and variables that start with
    "self." accessed by users of the Box object.

    But you will need other elements passed in besides "self".

    You need to pass information specifying where to put the box
    and how big the box should be.

    There are 3 standard ways to do this:
       1) Pass 4 points that represent the 4 corners of the rectangle.
       2) Pass only the top_left corner and the bottom_right corner.
          If top_left = (a,b) and bottom_right = (x,y), then
          the top_right = (x , b) and bottom_left = (a, y).
       3) Pass the top_left point, the height, and the width.

    I like method 3 the best, but you can decide.  You will end up using all
    the points and the height and width.  The question is which do you
    want to come up with and which do you want the computer to compute.

    If you use either start_point, height, width you can get all the
    points using:
    
        pts = get_rect_points(start_pt, height, width)

    If you use top_left_pt and bottom_right_pt, you can get all the pts with:
        
        pts = get_rect_points([top_left_pt,bottom_right_pt])
        
    and a list [height width] with

         dim = get_rect_height_width(top_left_pt,bottom_right_pt).

    The value pts is a list, an you access the 4 points as pts[0], pts[1],
    pts[2], and pts[3].

    The value dim is also a list where height = dim[0] and width = dim[1].

    is_point_in_rectangle(pt, pts)
    split = split_rectangle_top_bottom(pts)
    pts = get_rect_points(start_pt, height, width)
    pts = get_rect_points([top_left_pt,bottom_right_pt])
    dim = get_rect_height_width(top_left_pt,bottom_right_pt)
    """
    
    """
    Needs a rectangle and text inside the rectangle
    """ 
    def __init__(self,start_pt,height,width,color):
        pass

    """
    move all parts of the box: rectangle and text
    """
    def move(self, dx, dy):
        pass

    """
    move all parts of the box: rectangle and text
    """
    def draw(self):
        pass

    """
    Returns 'top', 'bottom', or 'out'.
    Use is_point_in_rectangle and
        split_rectangle_top_bottom
    
    """
    def is_point_in_box_top_bottom(self,pt):
        pass
                   
            
        
"""
# Here we will make a class for our digital clock.
# Even though we only need one, it helps to organize our data and
# procedures.  Procedures for a class are commonly called methods.
# Having a new name for procedures helps people who like having special
# names for stuff even if they are particularly useful.
#
"""
class Digital_Display:

    """
    You want 3 boxes, hrs, minutes, seconds
    """
    def __init__(self,start_pt,box_height,box_width,color):
        pass


    """
    draws all the boxes 
    """
    def draw(self):
        pass

    """
    moves all the boxes
    """
    def move(self, dx, dy):
        pass

    """
    Return 'out' if point is in no box.
    if in a box, identify box and whether in top or bottm half
    """
    def is_pt_in_display(self,pt):

        pass
        return 
       
        
        



  


"""
# We will need to set the time on our clock.
# We could write code to let the user type in values.
# But I think it is way cooler to let the usere click on the
# boxes. 
#
# For example, if you click on the minutes box, it changes the minute.  
# If you click the top half, it will increase the time by 1 minute.  
# If you click the bottom half, it will decrease the time by 1 minute.
# The hours and seconds boxes would do the same.
# 
"""
"""Check to see if mouse click point is in display.  If not, return 0 sconds of
change.  If click in display, return -/+ 1  or 60 ro 3600 seconds of time
change depending on which box is clicked and top vs bottom.
"""
def check_request_to_set_time(pt,digital):
    pass

            
def main():

    """ Create and draw the display"""

    """ Get first system time number as a reference base
    using time.clock() """            

    """ set update flag tick_time for 1 second"""
    
    while True:
        pass
        """ Assign time since we started.
        Since we may leave this clock running a long time,
        we don't want this to overflow.
        But since our clock starts over every 12 hours,
        we can make this the seconds counter start
        over every 12*3600 seconds."""
        


        """ Use win.checkMouse() to get click point"""


        """  Reset clock if pt != None """
        

            """ Use check_request_to_set_time to get the amount
            to change our time."""


            """ only bother if change is != 0"""

                """ update the base time with the change"""
                
                """Update time_in_secs with new clock_base_time"""
                
                """Set tick time to ensure immediate update"""


        """ Every second, update the time in display"""


            """ set new tick time to be 1 second from last tick time"""

            """Use convert_secs_to_hhmmss to convert time_in_seconds
            to [hours , minutes , seconds]  """

            """ update digital display boxes."""

        
            
     
main()
    
    
                   
            

