import os,sys

def DoStuff( X,Y ):
  result=X+Y
  if(result>10):print("big result");a=1
  else:
   print( "small result" )
  for  i in range(0,5):print(i)
  veryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryLongVariableName=result
  return  veryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryVeryLongVariableName

class  myclass:
 def __init__( self ,Name ):
  self.Name=Name
 def PrintName(self):print("Name is:",self.Name)
