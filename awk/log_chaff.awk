#!/usr/bin/awk -f 
#A program I used in conjunction with parse_json_logs.py. Allowed me to filter out specific bots I didn't care about or have already seen.

#TODO: Add more functionality to filter out more junk
# For a match, add that sesid here so I can check against it later.
/mdrfckr/ { FS="|"; sessid[$2] = $2; next }

#For every line, add into here to loop back over later
{
    a[i++]=$0
}

#After everything loop back over and print non-matches.
END {
    indx=0
    while (indx <= i) {
        split(a[indx], line)
        if (!(line[2] in sessid)) { print a[indx] }
        indx++
    }
    print indx, "lines trimmed"
}

