#!/bin/bash


extensions=(.py .pl .bash .csh .c .h .html .htm .css .php)

backup_dir=( web alarm )

backup_dest=/home/pi/code_backup

for d in ${backup_dir[*]}; do
  if [ ! -e $backup_dest/$d ]; then
    mkdir $backup_dest/$d
#  else
#    echo "$d exists"
  fi

  for e in ${extensions[*]}; do
    cd /home/pi/$d
  
    filelist=(`find -name "*$e"`)
    numfiles=${#filelist[*]}
  
   if [ $numfiles -gt 0 ]; then
     cp --parents ${filelist[*]} $backup_dest/$d
     echo $e, $numfiles
   fi
  done

done

# back up these individual files too

filelist=(/home/pi/.bashrc /home/pi/backup.bash)

for f in ${filelist[*]}; do
  cp $f $backup_dest
done
