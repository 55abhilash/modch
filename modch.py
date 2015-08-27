#!/usr/bin/env python
import sys
import os
class ch:
	def chg(self, CURR_IP):
		chara = '\''
		if (len(sys.argv) < 2) :
			file_to_read = open("/var/www/moodle/config2.php", "r") 
			lines_in_file = file_to_read.readlines()
			#del lines_in_file[20]
			lines_in_file[19] = "$CFG->wwwroot   = " + chara + "http://" + CURR_IP + "/moodle" + chara + ";"
			file_to_read.close()
			file_to_read = open("/var/www/moodle/config2.php", "w")	
		elif (len(sys.argv) == 2) :
			file_to_read = open(sys.argv[1], "r") 
			lines_in_file = file_to_read.readlines()
			#del lines_in_file[int(sys.argv[2])]
			lines_in_file[19] = "$CFG->wwwroot   = " + chara + "http://localhost/moodle" + chara + ";"
			file_to_read.close()
			file_to_read = open(sys.argv[1], "w")	
		else :
			return 1
		for item in lines_in_file :
			file_to_read.write(item)
class ip_:
	def get_ip(self) :
		ifconfig_eth0_out = os.popen("ifconfig eth0 | grep inet\ addr").read()
		ifconfig_wlan0_out = os.popen("ifconfig wlan0 | grep inet\ addr").read()
		if(ifconfig_eth0_out != "") :
			eth0_ip = ifconfig_eth0_out.split()[2][6:]
			print "came+here"
			return eth0_ip
		elif(ifconfig_wlan0_out != "") :
			wlan0_ip = ifconfig_wlan0_out.split()[2][6:]
			return wlan0_ip	
		else :
			return "localhost"

ip__ = ip_()
CURR_IP = ip__.get_ip()
ch_ = ch()
ch_.chg(CURR_IP)		
