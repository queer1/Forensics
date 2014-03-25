#!/usr/bin/python
import commands
# This is the beta version. This script can be used for Forensics 
# Imaging of suspect disc.It includes two methods of Imaging 
# -Imaging using attached evidence disc to suspect system &
# -Imaging using Forensics workstation over network using Netcat.
# Author : SaMaN
# Repo : c0d3r4ck
print '''      _____     _  _____        ___      _    
     |  _  |   | ||____ |      /   |    | |   
  ___| |/' | __| |    / /_ __ / /| | ___| | __
 / __|  /| |/ _` |    \ \ '__/ /_| |/ __| |/ /
| (__\ |_/ / (_| |.___/ / |  \___  | (__|   < 
 \___|\___/ \__,_|\____/|_|      |_/\___|_|\_\
                                              
                                                '''
print "-----------------------------------"
print "Welcome to the disk imaging script"
print "-----------------------------------"
print "                                       "
flag=True
while flag==True:
	print "Choose your method of Disc Imaging:"
	print "1. Disc Imaging by live boot on suspect system."
	print "2. Disc imaging using Netcat"
	print "3. Exit"
	ch=input()
	def choice(ch):
		if ch==1 or 2:
			print " Please enter following information"
			dsk=commands.getoutput("fdisk -l|grep sd")
			print "Available Disks:"+"\n"+dsk
			susp=raw_input("A. Enter the path for suspect disk:")
			evid=raw_input("B. Enter the path for Evidence Disk(leave blank for Netcat Disc imaging)")
			hash=raw_input("C. Do you want to calculate hashes for both?(yes/no)")
			if hash=="y" or "yes":
				hpath=raw_input("Enter the path for hash log file:")
				if ch==1:
					print " Disk imaging started... This may take few minutes"
					cmd=commands.getoutput("dcfldd if=%s of=%s/image.dd hash=md5,sha1 hashlog=%s/hashlog.txt"%(susp,evid,hpath))
					print cmd
				elif ch==2:
					print '''Enter the following commands on Forensics Workstation ::
								"nc -l -p <port number> |gunzip|pipebench>/<path for evidence disc>/image.dd" ''' 
					ip=raw_input("Enter the I.P of Forensics Workstation:")
					prt=input("Enter port number of Forensics Workstation:")
					print " Disk imaging started... This may take few minutes"
					cmdnc=commands.getoutput("dcfldd if=%s| gzip --fast|nc %s %s"%(susp,ip,prt))
					print cmdnc
				else:
					print "Wrong Input"
			elif hash=="n" or hash=="no":
				if ch==1:
					print " Disk imaging started... This may take few minutes"
					cmd=commands.getoutput("dcfldd if=%s of=%s/image.dd"%(susp,evid))
					print cmd
				elif ch==2:
					print '''Enter the following commands on Forensics Workstation ::
								"nc -l -p <port number> |gunzip|pipebench>/<path for evidence disc>/image.dd" ''' 
					ip=raw_input("Enter the I.P of Forensics Workstation:")
					prt=input("Enter port number of Forensics Workstation:")
					print " Disk imaging started... This may take few minutes"
					cmdnc=commands.getoutput("dcfldd if=%s| gzip --fast|nc %s %s"%(susp,ip,prt))
					print cmdnc
				else:
					print "Wrong Input"
			else :
				print "Wrong Input"
		elif ch==3:
			print "Bye Bye"
			
		else:
			print "Wrong input"
		return
choice(ch) 

