#***(1)Returns all Trainees from Trainee table
Trainee = Trainee.objects.all()

#(2)Returns first Trainee in table
firstTrainee = Trainee.objects.first()

#(3)Returns last Trainee in table
lastTrainee = Trainee.objects.last()

#(4)Returns single Trainee by name
TraineeByName = Trainee.objects.get(name='Monica')

#***(5)Returns single Trainee by name
TraineeByEmail = Trainee.objects.get(email=ross@gmail.com)
# print(TraineeByEmail)

#***(6)Returns all Progresses related to Trainees (firstTrainees variable set above)
firstTrainee.progress_set.all()

#(7)***Returns progresses Trainees name: (Query parent model values)
Progress = Progress.objects.first() 
parentName = Progress.Trainee.name

#(8)***Returns Packages from Packages table with value of "Pranayama" in type attribute
Package = Package.objects.filter(type="Pranayama")