
from ps4 import *

bacteria = [ResistantBacteria(birth_prob=0.5, death_prob=0.2, resistant=True, mut_prob=0.3)] * 10 + [ResistantBacteria(birth_prob=0.5, death_prob=0.2, resistant=False, mut_prob=0.3)] * 3
patient = TreatedPatient(bacteria, 50)

print(patient.get_resist_pop())