#!/bin/bash
n=N # Number of species chemical for PDOS Calculate
FORTRAN_PROGRAMS=( "gnubands" "eigdos" "fmpdos.f" "eletronic.py")
ELETRONIC_DATA(){ #get informations about total energy and magnetic moment
  pwd >> ../Data-pristine.txt
  tail -n 32 *.out | grep Total >> ../Data-pristine.txt
}
DATA_BUILD(){
  code=$(ls *.out | cut -d'.' -f1) ; ./${FORTRAN_PROGRAMS[0]} <*.bands> $code.bands.dat # build a band.dat file
  FERMI=$(cat *.EIG | head -n 1 | tr -d [:blank:]) ; echo "FERMI: $FERMI" >> ../Data-pristine.txt
  sed -i 's/'$FERMI'/'$FERMI' 0.05 1000 -10 10/' *.EIG
  ./${FORTRAN_PROGRAMS[1]} <*.EIG> $code.dos.dat
  PDOS=$(ls *.PDOS | cut -d'/' -f2)
  for i in $(seq $n); do
    cat ${FORTRAN_PROGRAMS[2]} | sed 's/inputdata/'$PDOS'/' | sed 's/output.dat/'$i'.dat/' | sed 's/chemical/'$i'/' >> fmpdoss.f
    gfortran fmpdoss.f -o fmpdos.x ; ./fmpdos.x ; rm -r fmpdos.x ; rm -r fmpdoss.f
  done
}
PYTHON_MANAGER(){
  sed -i 's/name/'$code'/' eletronic.py ; sed -i 's/PF/'$FERMI'/' eletronic.py ; sed -i 's/EF/'$FERMI'/' eletronic.py
  grep constrained *.out >> const.dat ; sed -i 's/'$code'/name.input' eletronic.py
  PLOTS=("DOS_PLOTY()" "PDOS_PLOTY()" "BANDS_PLOTY()" "GAP_CALCULATE()")
  for ((k=0; k <${#PLOTS[@]}; k++)); do
    if [ $k -eq 3 ]; then
      cp eletronic.py run.py ; echo "${PLOTS[k]}" >> run.py ; echo "GAP: $(python3 run.py)" >> ../Data-pristine.txt ; rm -r run.py
    fi
    cp eletronic.py run.py ; echo "${PLOTS[k]}" >> run.py ; python3 run.py ; rm -r run.py
done
}
DIRETORY_MANAGER(){
	DIR=("")
for (( a=0; a<${#DIR[@]}; a++ )); do
	echo "Inicio do primeiro loop"
  for ((b=0; b<${#FORTRAN_PROGRAMS[@]}; b++)); do
    cp ${FORTRAN_PROGRAMS[b]} ${DIR[a]}
  done
  cd ${DIR[a]} ; ELETRONIC_DATA ; DATA_BUILD ; PYTHON_MANAGER ; cd ..
done
}
DIRETORY_MANAGER
