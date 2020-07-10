import sys
import os
from rdkit import Chem

def comparemolfiles(inputdirectory, referencedirectory):
	'''This function checks if the molecules in a set of mol-files are identical to the molecules in a second set of mol-files using Standard InChI.
	(assuming the files have the same names)'''

	dirlist = os.listdir(inputdirectory)										# returns a list of filenames for the given directory
	rightmoleculeinbothmolfiles = 0
	check = False
	with open(str(inputdirectory+'/'+'RDKit_inchi_Report.txt'), 'w+') as output:		# create empty output.txt
		for file in dirlist:													# Loop over inputdirectory
			if file.lower()[-4:] == ".mol" or ".sdf":
				check = True
				input = Chem.SDMolSupplier(str(inputdirectory + '/' + file))		# read mol-file with molecule to be checked (mol)

				input2 = Chem.SDMolSupplier(str(referencedirectory + '/' + file[:-4] + ".sdf"))	# read reference mol-file / ADAPT ENDING ACCORDING TO FILES
				for compound in input:
					if not compound:
						inchi1 = ""
						continue
						output.write('Not able to read molfile: ' + inputdirectory+'/'+file)
					inchi1 = Chem.inchi.MolToInchi(compound)						# generate standard Inchi
				for compound in input2:
					if not compound:
						inchi2 = ""											
						continue
						output.write('Not able to read molfile: ' + referencedirectory+'/' + file)
					inchi2 = Chem.inchi.MolToInchi(compound)						# generate (canonical) SMILES
				if inchi1 == inchi2:
					print(inputdirectory + '/' + file + ' contains the right structure: \n' + str(inchi1) + ' vs. \n' + str(inchi2) + '(Reference)\n')
					output.write(inputdirectory + '/' + file + ' contains the right structure: \n' + str(inchi1) + ' vs. \n' + str(inchi2) + '(Reference)\n')
					rightmoleculeinbothmolfiles += 1
				else: 
					print(inputdirectory + '/' + file + ' does not contain the right structure: \n' + str(inchi1) + ' vs. \n' + str(inchi2) + '(Reference)\n')
					output.write(inputdirectory + '/' + file + ' does not contain the right structure: \n' + str(inchi1) + ' vs. \n' + str(inchi2) + '(Reference)\n')
		output.write(str(rightmoleculeinbothmolfiles) + ' mol-files contain the right structure.')
		if check == False:
			print('No mol-files found.')
			os.remove(str(inputdirectory+'/'+'RDKit_inchi_Report.txt'))						# If no sdf-files were found, print message and delete output.
		else:
			print('List of standard InChI sucessfully created and saved in ' + str(inputdirectory+'/'+'RDKit_inchiReport.txt'))
		return

def main():
	if len(sys.argv) != 3:
		print("\"Usage of this function: comparemolfileswithstandardinchi.py directory-with-mol-files directory-with-reference-molfiles ")
	if len(sys.argv) == 3:
		comparemolfiles(sys.argv[1], sys.argv[2])
	sys.exit(1)

if __name__ == '__main__':
	main()
