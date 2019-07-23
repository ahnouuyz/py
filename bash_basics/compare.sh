#!/usr/bin/env bash

file1="set1"
file2="set2"

sorted_file1="${file1}.sorted"
sorted_file2="${file2}.sorted"
unique1="${file1}_unique.txt"
unique2="${file2}_unique.txt"
commons="commmons.txt"

if [ ! -f $sorted_file1 ]; then
	sort $file1 > $sorted_file1
	echo "New file: $sorted_file1 created."
fi
if [ ! -f $sorted_file2 ]; then
	sort $file2 > $sorted_file2
	echo "New file: $sorted_file2 created."
fi

echo -e "\nThis takes about 43 seconds to compare 2 sets of about 4,000,000 entries each (includes sorting the files)."
echo -e "This takes about 17 seconds if the files have been sorted.\n"
echo "Entries unique to either file will (try to) be shown on the screen:"
comm -3 --total $sorted_file1 $sorted_file2

diff --speed-large-files $file1 $file2 | tee >(grep "< " | tr -d "< " | sort > $unique1) >(grep "> " | tr -d "> " | sort > $unique2) > /dev/null
echo "Values unique to $file1 written to $unique1"
echo "Values unique to $file2 written to $unique2"

comm -12 $sorted_file1 $sorted_file2 > $commons
echo "Values common to both $file1 and $file2 written to $commons"
