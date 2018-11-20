import glob, sys
from easygui import *
n= diropenbox(msg=None, title=None, default=None)
path = glob.glob(n+'/*.png')
print(path)
n = len(path)
M = True
i=0
while M:

	choice = buttonbox(msg='Which Choclate', title=' ', choices=('Exit', 'Previous', 'Next'), image=path[i])
	if choice == 'Exit':
		sys.exit(0)
	if choice == 'Previous':
		if i == 0:
			continue
		else:
			i -= 1
			choice = buttonbox(msg='Which Choclate', title=' ', choices=('Exit', 'Previous', 'Next'), image=path[i])
	if choice == 'Next':
		if i >= n:
			continue
		else:
			i+=1
			choice = buttonbox(msg='Which Choclate', title=' ', choices=('Exit', 'Previous', 'Next'), image=path[i])

		
	

