# Opdracht 3 tekstfuncties
# Naam student:
# Groep:

# Hier komt je code...
# Definitie van de losse regels van één kerstboom
boom = [
    "    *    ",
    "   ***   ",
    "  *****  ",
    " ******* ",
    "*********",
    "   ***   ",
    "   ***   ",
    "   ***   "
]

# Teken vijf bomen naast elkaar
for regel in boom:
    print((regel + '  ') * 5)
