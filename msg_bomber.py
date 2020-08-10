""" 
open google
go to amazon website
click sign in button
take phno as input
enter phno
click continue
click get OTP ONCE
Click resend OTP again n again
close browser"""

#oopen google
from selenium import webdriver
browser=webdriver.Chrome('C:\\Users\Pavana Prabhu\chromedriver_win32 (1)\chromedriver.exe')
browser.get('https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1')

#take phno as input

phno=input("Enter yr phno:")
times=int(input("Enter no of times:"))
#finding the input num
phone=browser.find_element_by_id('ap_email')
#to send val of phno
phone.send_keys(phno)

#click continue button
cnt=browser.find_element_by_id('continue')
cnt.click()

#click sendotp button
sendotp=browser.find_element_by_id('continue')
sendotp.click()


n=times-1
for i in range(n):
 
	#resend otp is a  link text
    r=browser.find_element_by_link_text("Resend OTP")
    r.click()

browser.quit()