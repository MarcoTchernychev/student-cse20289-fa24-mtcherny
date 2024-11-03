#Marco Tchernychev
#mtcherny@nd.edu
#!/usr/bin/bash
datetime=$(date +%Y-%m-%d_%H-%M)
#set -x
#echo "$date"
log=$datetime-UnitTest.log
#echo "$log"
python3 -m unittest tests.test_3a >> "$log" 2>&1
python3 -m unittest tests.test_3b >> "$log" 2>&1
python3 -m unittest tests.test_3c3d >> "$log" 2>&1
python3 -m unittest tests.test_4 >> "$log" 2>&1

count=$(grep -o "OK" "$log" | wc -l)

#echo "$count"

if [ -z "$count" ]; then
        cat "$log"
else
    #Check if the count is equal to 4
    if [ "$count" -eq 4 ]; then
        echo "log $log is going to hw06 directory"
    fi
    #Check if the count is not equal to 4
    if [ "$count" -ne 4 ]; then
        cat "$log"
    fi
fi