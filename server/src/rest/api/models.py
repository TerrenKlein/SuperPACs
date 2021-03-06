from django.db import models

# Create your models here.

class Representative(models.Model):
    '''
    Representative class which represents Representatives.
    '''


    first_name = models.CharField(max_length = 140)
    middle_name = models.CharField(max_length = 140,default="")
    last_name = models.CharField(max_length = 140)

    district = models.CharField(max_length = 140,default="")
    state = models.CharField(max_length = 140)
    sitelink = models.CharField(max_length = 500,default="")


    PARTIES =   (("D","Democrat"),
                ("R","Republican"),
                )
    party = models.CharField(max_length=1, choices=PARTIES)

    CHAMBERS =   (("H","House"),
                ("S","Senate"),
                )
    chamber = models.CharField(max_length=1, choices=CHAMBERS)

    ##PROPUBLICA api id.
    propublicaid = models.CharField(max_length = 9,unique=True)

    ##FEC api id
    fecid = models.CharField(max_length = 9,default = "")


    def __str__(self):
        return self.name+" ("+party+")"


    ##getters
    def __json__(self):
        return {"id":self.id,"name":str(self.first_name+" "+self.last_name),"party":self.party}



class SuperPAC(models.Model):
    '''
    SuperPAC class which represents SuperPACs.
    '''
    name = models.CharField(max_length = 140)
    sitelink = models.CharField(max_length = 500,default="")

    ##PROPUBLICA api id reference.
    propublicaid = models.CharField(max_length = 9,default="")

    ##FEC api id
    fecid = models.CharField(max_length = 9,unique = True)


    def __str__(self):
        return self.name

    def __json__(self):
        return {"id":self.id,"name":self.name}

class Donation(models.Model):
    '''
    Donation class that acts as a donation edge from SuperPACs to Representatives.
    '''
    superpac = models.ForeignKey(SuperPAC, on_delete=models.CASCADE)##figure out what is best here.
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)
    amount = models.IntegerField()
    support_options =   (("S","Support"),
                        ("O","Oppose"),
                        )
    support = models.CharField(max_length=1, choices=support_options)
    uid = models.CharField(max_length = 40,default=None)

    def __str__(self):
        return self.superpac.__str__()+","+self.representative.__str__()+","+self.amount

    def __json__(self):
        return {"from":self.superpac.id,"to":self.representative.id,"amount":self.amount,"support":self.support}
