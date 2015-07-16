from django.db import models

# Create your models here.
class Document(models.Model):
    #title = models.CharField(max_length=128, unique=True)                               #Stores Title of Document
    image = models.FileField(upload_to='documents/%Y/%m/%d')                              #Stores Image
    #current_transcription = models.CharField(max_length=128, unique=True)               #Stores transcription submitted by curator
    #old_transcription = models.CharField(max_length=128, unique=True)                   #Stores the transcription made by the census ( The compilation of all transcriptions through generic user inputs )
   # current_markers = models.OneToManyField(Markers, blank="true")     #Stores the current location of markers submitted by curator
   # old_markers = models.OneToManyField(Markers, blank="true")           #Stores the location of markers made by the census ( The compilation of all recieved marker locations)
    time_stamp = models.DateTimeField(auto_now_add=True)                                #Stores Time at submission


    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.title

class Markers(models.Model):
    x_coordinate = models.IntegerField(default=0)           #Stores X coord as integer
    y_coordinate = models.IntegerField(default=0)           #Stores Y coord as integer
    letter = models.CharField(max_length=128, unique=True)  #Stores Greek symbol
    time_stamp = models.DateTimeField(auto_now_add=True)    #Stores Time at submission
    user_id = models.IntegerField(default=0)                #Stores the id of the user submitting document



    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.x_coordinate+','+self.y_coordinate+','+self.letter  #Type cast return to integers