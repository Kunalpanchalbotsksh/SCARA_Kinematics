import math
#import string #related to arduino serial data type conversion (might save your time and mine too)
print("Take Clockwise = Negative (-ve), Anticlockwise = Positive (+ve)")
z=0
alpha1=0
alpha2=180
ARM_1=float(150)
ARM_2=float(100)
pi=3.141592653589793
print("\nArm 1 at Angle w.r.t x-asis:",alpha1,'       (Range 0° to 180°)')
print("Arm 2 at Angle w.r.t x-asis:",alpha2,'    (Range 0° to 360°)')
print("\nInputs Method to control SCARA:-\nBy Forward Kinematics = F/f\nBy Inverse Kinematics = I/i\nBy Gcode file = G/g")
while True:
      while True:
         Initial_input= input("\nMethod to control SCARA:")
         if Initial_input in ("F","f","I","i","G","g","QUIT","quit","end"):
            break
         print("invalid input")
      if Initial_input in ("quit","QUIT","end"):
         print("Ended")
         break
      elif Initial_input in ("F","f"):
         while True:
            while True:
               ARM1_max=180
               ARM1_min=0
               Theta=input("Enter θ (Arm 1 Rotation):") #Get θ
               try:
                  Theta=int(Theta)#to verify integer
               except ValueError as k:
                  print("Arm 1 have Range 0° to 180°")#invalid argument
                  continue
               q=alpha1+Theta
               if ARM1_max<q:
                  print("Arm 1 have Range 0° to 180°")#invalid argument
                  continue
               elif ARM1_min>q:
                  print("Arm 1 have Range 0° to 180°")#invalid argument
                  continue
               else:
                  break
            θ=Theta/1.8 # ********Required Output**************
            while True:
                  ARM2_max=360
                  ARM2_min=0
                  Beta=input("Enter β (Arm 2 Rotation):") #Get β
                  try:
                     Beta=int(Beta)#to verify integer
                  except ValueError as k:
                     print("Arm 2 have Range 0° to 360°")#invalid argument
                     continue
                  p=alpha2+Beta
                  if ARM2_max<p:
                     print("Arm 2 have Range 0° to 360°")#invalid argument
                     continue
                  elif ARM2_min>p:
                     print("Arm 2 have Range 0° to 360°")#invalid argument
                     continue
                  else:
                     break
            β=Beta/1.8 # ********Required Output**************
            a=math.cos(math.radians(alpha1+Theta))
            b=math.cos(math.radians(alpha2+Beta))
            c=math.sin(math.radians(alpha1+Theta))
            if q in (180,0):
               c=0
            elif p in (180,0):
               c=0
            d=math.sin(math.radians(alpha2+Beta))
            if q in (180,0):
               d=0
            elif p in (180,0):
               d=0
            Forward_Kinematics_Matrix=[a,b,c,d]
            print("END_EFFECTOR_COORDINATE(x,y)=(",ARM_1 * Forward_Kinematics_Matrix[0] + ARM_2 * Forward_Kinematics_Matrix[1],",",ARM_1 * Forward_Kinematics_Matrix[2] + ARM_2 * Forward_Kinematics_Matrix[3],")")
            alpha1=alpha1+Theta
            alpha2=alpha2+Beta
            print("Arm 1 at Angle w.r.t x-asis:",alpha1)
            print("Arm 2 at Angle w.r.t x-asis:",alpha2)   
            while True:
               r=input("Check for Next Rotation:")
               if r in ("y","n","yes","Y","N","no"):
                  break
                  print("invalid input")
            if r in ("y","yes","Y"):
                  continue
            elif r in ("n","no","N"):
                  print("Ended")
                  break    
      elif Initial_input in ("I","i"):
         while True:
            while True:
               x=float(input("Enter X co-ordinate:"))
               y=float(input("Enter Y co-ordinate:"))
               c = math.sqrt(x**2+y**2)
               Phi = math.atan2(y,x)    # φ
               h=-1
               try:
                  new_alpha1 = Phi + h * math.acos((c**2 + ARM_1**2 - ARM_2** 2)/(2*c*ARM_1))
                  new_alpha2 = Phi - h * math.acos((c**2 + ARM_2**2 - ARM_1**2)/(2*c*ARM_2))
                  print("α1=",round(math.degrees(new_alpha1),4),"α2=",round(math.degrees(new_alpha2),4))
               except:
                  print("Given Co-ordinate is out of workspace area")
                  continue
               else:
                  print("\nArm 1 at Angle w.r.t x-asis:",math.degrees(new_alpha1),'       (Range 0° to 180°)')
                  print("Arm 2 at Angle w.r.t x-asis:",math.degrees(new_alpha2),'    (Range 0° to 360°)')
                  break
            Theta=math.degrees(new_alpha1)-alpha2
            Beta=math.degrees(new_alpha2)-alpha2
            θ=Theta/1.8 # ********Required Output**************
            β=Beta/1.8 # ********Required Output**************
            alpha1=math.degrees(new_alpha1)
            alpha2=math.degrees(new_alpha2)
            print
            while True:
                  r=input("Check for Next Rotation:")
                  if r in ("y","Y","n","N","yes","no"):
                     break
                  print("invalid input")
            if r in ("y","yes","Y"):
                  continue
            elif r in ("n","no","N"):
                  print("Ended")
                  break
      elif Initial_input in ("G","g"):
         gcode = open("C:\\Users\Shrikant\Downloads\Kinematics\gcode.txt", "r")  # Yes change according to your gcode location (prefered location of your slicer)
         for x in gcode:
               coordinate_arr = x.split()
               print("x,y",coordinate_arr[1].replace("X",""),coordinate_arr[2].replace("Y",""))
               x=float(coordinate_arr[1].replace("X",""))
               y=float(coordinate_arr[2].replace("Y",""))
               #z=float(coordinate_arr[3].replace("Z","")) #UNCOMMENT for z inputs from gcode
               c = math.sqrt(x**2+y**2)
               Phi = math.atan2(y,x)#φ
               h=-1
               try:
                  new_alpha1 = Phi + h * math.acos((c**2 + ARM_1**2 - ARM_2**2)/(2*c*ARM_1))
                  new_alpha2 = Phi - h * math.acos((c**2 + ARM_2**2 - ARM_1**2)/(2*c*ARM_2))
                  print("α1=",round(math.degrees(new_alpha1),4),"old α1",alpha1,"α2=",round(math.degrees(new_alpha2),4),"old α2",alpha2)
                  Theta=math.degrees(new_alpha1)-alpha1
                  Beta=math.degrees(new_alpha2)-alpha2
                  θ=Theta/1.8 # ********Required Output**************
                  β=Beta/1.8 # ********Required Output**************
                  print("θ=",Theta,"and β=",Beta)
                  alpha1=math.degrees(new_alpha1)
                  alpha2=math.degrees(new_alpha2)
               except:
                  print("Given Co-ordinate is out of workspace area")
                  continue
               
      while True:
         r=input("Switch Method to control SCARA:")
         if r in ("y","n","yes","no","Y","N","QUIT","quit"):
            break
            print("invalid input")
      if r in ("y","yes","Y"):
          continue
      elif r in ("n","no","N","QUIT","quit"):
         print("Ended")
         break
