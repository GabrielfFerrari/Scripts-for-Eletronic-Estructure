#!/bin/bash
# make fdf file
ARQUIVO_FDF=*.fdf				
ARQUIVO_FDF_FINAL=$1			
POSITIONS=media.txt			
ARQUIVO_TXT=position.txt		
MAKERC() {
	BLOCK1=$(grep -n '%block AtomicCoordinatesAndAtomicSpecies' $ARQUIVO_FDF | cut -d: -f1)
	BLOCK2=$(grep -n '%endblock AtomicCoordinatesAndAtomicSpecies' $ARQUIVO_FDF | cut -d: -f1)
	BLOCK3=$(wc -l *.fdf |cut -d' ' -f1)
	sed -n '1,'$BLOCK1'p' $ARQUIVO_FDF >> $ARQUIVO_FDF_FINAL
	}

TRATAMENT_ANI() {
	LINHA_INICIO=$( grep -n ' 100' *.ANI | sed -n '$ p' | cut -d: -f1) # TROCAR O 100 PELA QUANTIDADE DE ATOMOS
	LINHA_TOTAL=$(wc -l *.ANI | cut -d' ' -f1)
	sed -n ''$LINHA_INICIO','$LINHA_TOTAL'p' *.ANI >> $ARQUIVO_TXT
	sed -i 's/file.xyz/'$ARQUIVO_TXT'/'
	sed -i 's/file.fdf/'$1'/'
	cat $POSITIONS >> $ARQUIVO_FDF_FINAL
	sed -n ''$BLOCK2','$BLOCK3'p' $ARQUIVO_FDF >> $ARQUIVO_FDF_FINAL
	}
