import sys
######################################
import Exercises.exercise01 as EX01
import Exercises.exercise02 as EX02
######################################



###################################################
# Main

if (len(sys.argv)==1):
    print("Usage: setup <Exercise Number>")
else:
    if (sys.argv[1]=="1"):
        EX01.RunExercise()
    if (sys.argv[1]=="2"):
        EX02.RunExercise()

