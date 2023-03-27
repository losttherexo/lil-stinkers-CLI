# need to import models.py - unsure on how to do so
from db.models import *
import ipdb

a1 = Artist("Mac Miller", "Rap")
a2 = Artist("Ludwig van Beethoven", "Classical")

l1 = Listener("Jesse")
l2 = Listener("Andre")
l3 = Listener("Tom")
l4 = Listener("Collin")

l1 = Song("Ladders", a1, l4)
l2 = Song("Für Elise", a2, l1)

ipdb.set_trace()