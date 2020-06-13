#!/bin/bash
git init
git add .
git commit -m "$1"
git remote add origin https://github.com/androide72/data-study.git
git push origin master
