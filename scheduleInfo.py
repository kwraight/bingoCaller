#basic schedule job to use summaryInfo to summarise data, delete data and tweet summary plot
import schedule
import subprocess
import time
import datetime

def job(slot):
    print subprocess.check_output(['python', 'bingoInfo.py','--slot',slot])
    print "done job:\n",datetime.datetime.now()

#schedule.every().day.at("11:00").do(job("morning"))
#schedule.every().day.at("14:30").do(job("afternoon"))
#schedule.every().day.at("19:30").do(job("evening"))

schedule.every().day.at("23:17").do(job,"go")

while True:
    schedule.run_pending()
    time.sleep(1)
