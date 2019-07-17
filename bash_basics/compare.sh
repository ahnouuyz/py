#!/usr/bin/env bash

f1="set1"
f2="set2"

echo "Comparing 2 sets of about 1,000,000 entries each took about 35 sec on a 10-year-old computer."
echo "Entries unique to either file will (try to) be shown on the screen:"
comm -3 --total <(tr '[:upper:]' '[:lower:]' <$f1 | sort) <(tr '[:upper:]' '[:lower:]' <$f2 | sort)

echo "Now, unique and common values will be saved into separate files..."
comm -23 <(tr '[:upper:]' '[:lower:]' <$f1 | sort) <(tr '[:upper:]' '[:lower:]' <$f2 | sort) > ${f1}_only
comm -13 <(tr '[:upper:]' '[:lower:]' <$f1 | sort) <(tr '[:upper:]' '[:lower:]' <$f2 | sort) > ${f2}_only
comm -12 <(tr '[:upper:]' '[:lower:]' <$f1 | sort) <(tr '[:upper:]' '[:lower:]' <$f2 | sort) > both
echo "Done! 3 separate files saved!"

# for x in $(cat $f1)
# do
# 	if [ $(grep -i $x $f2) ]
# 	then
# 		found="$x found in both"
# 		printf "$found\r\n" >> both1.txt
# 		echo $found
# 	else
# 		notfound="$x not found in $f2"
# 		printf "$notfound\r\n" >> ${f2}_missing.txt
# 	fi
# done
