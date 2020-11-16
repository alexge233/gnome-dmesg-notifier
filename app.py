import os
import tailhead
import time
import re
from subprocess import run

keywords = ["emerg", "alert", "crit", "err", "info"]
regexes = []

#
# assert logfile or even use argparse to get it in
#

for key in keywords:
    expr = '\]\s{1,}' + key +'\:(.*)$'
    regexes.append(re.compile(expr))

for line in tailhead.follow_path('/var/log/syslog'):
    if line is not None:
        for expr in regexes:
            exists = re.match(expr, line)
            if exists is not None:
                print(exists)
                #run(['notify-send', text]
    else:
        time.sleep(1)
