#! /usr/bin/python3.8

##########################################################
## Search for homologous structures (Protein Data Bank) ##
## from peptide sequences.                              ##
## by Lucas Sousa Palmeira.                             ##
##########################################################

import sqlite3

class DataBase:
    def __init__(self, arq):
        self.arq = arq

    def data(self):

        sequences = []

        with open(f'{self.arq}', 'r') as file:
            seq = file.readlines()
            for x in seq:
                for y in ['\n']:
                    element = x.replace(y, "")
                    sequences.append(element)

        self.data = []

        for i, seq in enumerate(sequences):
            with open(f'pep{i}.log', 'r') as file:
                lines = file.readlines()[34]
                self.data.append((f'pep{i}', seq, lines[0:4], lines[5:6], lines[82:86]))

    def add(self):

        connection = sqlite3.connect('blastp_data.db')
        cursor = connection.cursor()
        cursor.executemany('''
                            insert into peptides_amps_blast (id, sequence, homologous_pdb, chain, identity)
                            values(?, ?, ?, ?, ?)
                            ''', self.data)

        connection.commit()
        cursor.close()
        connection.close()