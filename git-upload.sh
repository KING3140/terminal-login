#!/bin/bash
clear
read -p "Enter path of file u wanna upload:~# " path
cd $path
git init
git add .
git status
git commit -m "main"
read -p 'Enter gitHub username:~# ' user
read -p 'Enter repo name:~#  ' repo
git remote add origin https://github.com/$user/$repo.git
git push -u origin master
