#!/bin/bash
git init
git add .
git commit -m "$1"
git remote add origin https://github.com/androide72/Shell_script.git
git push origin master
