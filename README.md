# missed-call-notify
Sending an email notification about a missed call from the Asterisk server by SMTP

HOW TO INSTALL

1. Put missed-call-notify.py in /home directory (for example). 
2. Make it executable:

$ chmod +x /home/missed-call-notify.py

3. Add dialplan to the extensions.conf file:

exten => h,1,NoOp(Dialstatus is ${DIALSTATUS})
exten => h,2,ExecIf($["${DIALSTATUS}"!="ANSWER"]?system(/home/missed-call-notify.py ${CALLERID(name)} ${CALLERID(num)} ${EXTEN})

4. Reload dialplan:

$ asterisk -rx 'dialplan reload'
