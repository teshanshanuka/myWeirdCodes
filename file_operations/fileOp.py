import os, shutil

CURDIR = os.getcwd()

def writeFile(filename, text):
	"""writeFile(filename, text)::Write a file in current directory or in a subdirectory in current directory"""
	if '\\' in filename:
		filedir = os.path.dirname(filename)
		if not os.path.exists(filedir):
			os.makedirs(filedir)
	file = open(filename, 'w')
	file.write(text)
	file.close()
	print('Created', os.path.join(CURDIR,filename))

def copyFiles(**kwargs):
	"""
	copyFiles(**kwargs)::
	copyFiles(files = [file name or list of file names to copy], todir = {directory to copy})
	copyFiles(files, todir,fromdir = {directory to copy files from})
	"""
	if 'files' in kwargs:
		if 'todir' in kwargs:
			# if directory given not exists, create it
			if not os.path.exists(kwargs['todir']):
				os.makedirs(kwargs['todir'])
			if 'fromdir' in kwargs:
				# if only one filename is passed
				if isinstance(kwargs['files'], str):
					if not os.path.isfile(os.path.join(kwargs['fromdir'],kwargs['files'])):
						print(os.path.join(kwargs['fromdir'],kwargs['files']), 'not Found!')
						return
					shutil.copy(os.path.join(kwargs['fromdir'],kwargs['files']), kwargs['todir'])
				# if a list of file names is passed
				elif isinstance(kwargs['files'], list):
					for file in kwargs['files']:
						# if file given not exists, prompt and quit function
						if not os.path.isfile(os.path.join(kwargs['fromdir'],file)):
							print(os.path.join(kwargs['fromdir'],file), 'not Found!')
						continue
						shutil.copy(os.path.join(kwargs['fromdir'],file), kwargs['todir'])
			else:
				# if only one filename is passed
				if isinstance(kwargs['files'], str):
					if not os.path.isfile(kwargs['files']):
						print(kwargs['files'], 'not Found!')
						return
					shutil.copy(kwargs['files'], kwargs['todir'])
				# if a list of file names is passed
				elif isinstance(kwargs['files'], list):	
					for file in kwargs['files']:
						if not os.path.isfile(file):
							print(file, 'not Found!')
						continue
						shutil.copy(file, kwargs['todir'])

# copyFiles(files= 'none.txt')
# copyFiles(files= 'sample.txt', todir= 'zb')
# copyFiles(files= 'sample.txt', todir= 'zb1')
# copyFiles(files= 'test.txt', todir= 'zb', fromdir = 'testFolder')
# copyFiles(files= ['test.txt', 'test2.txt'], todir= 'zb\\sa', fromdir = 'testFolder')
