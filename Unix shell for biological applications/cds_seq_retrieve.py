from Bio import Entrez

# Let Entrez know who you are
Entrez.email = "arrerex580@gmail.com"

# Ask for the accession number and which database to query
accession = input("Enter Accession number: ")
database = input("Enter database to search: ").lower()

# Get the fasta file for the accession number from the database provided
handle = Entrez.efetch(db=database,id=accession,rettype="fasta",retmode='text')

# write the fasta file into cds_seq.fasta
with open('cds_seq.fasta','w') as file:
	file.write(handle.read())

