#! /usr/bin/python3.8

##########################################################
## Search for homologous structures (Protein Data Bank) ##
## from peptide sequences.                              ##
## by Lucas Sousa Palmeira.                             ##
##########################################################

import sqlite3
from biopep import Peptide
from extract import DataBase

peptides = []

with open('peptides.txt', 'r') as file:
    seq = file.readlines()
    for x in seq:
        for y in ['\n']:
            element = x.replace(y, "")
            peptides.append(element)

for i, seq in enumerate(peptides):
    pep = Peptide(i, seq)
    pep.createfasta()
    pep.createali()
    pep.runblast()
    pep.identity(25)
    pep.pdb()

connection = sqlite3.connect('blastp_data.db')
cursor = connection.cursor()
cursor.execute('''
                create table peptides_amps_blast(id text, sequence text, homologous_pdb text, \
                chain text, identity text)
                ''')
connection.commit()
cursor.close()
connection.close()

itens = DataBase('peptides.txt')
itens.data()
itens.add()