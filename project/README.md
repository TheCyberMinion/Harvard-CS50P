# PHISH-TRIAGE

### Video Demo:

### Description

phish-triage is a tool I plan to built as my first cyber project and its version1 is gonna be cs50p final project. This tool simply takes a email file idealy a'.eml' which contains all the info not visible to a common user as this info is usually hidden in places where normally peopple dont look. This info is the truth behind the convinsing front that pople see in body and shows the truth rather than a glorfified GUI. My tool's puspose is to use the file and find the stuff that matters and rate it from 0-100, the higher the score the more the chances the email is not a scam.

Good thing about this is as for now it entierly runs offline. It runs based on already predetemined set of rules what to check what to comapare all decided based on real world standards. It simply reads file from the disk and does eveything itself from taking the file to reading the contnet to talking out needed stuff to printing the report everything from start to end happens locally. It does not use any other 3rd party libraries that needs install and only works on python built-in stuff. The 'pytest' listes in reqirements only exist to test the code itself.

Talking about my file structer,

First I have "project.py" that is my main file with main function and three other functions,

getFilePath -> this functions returns the filePath
getContentFromFile -> this functions gets contnet for the email file
scoreEmail -> this is the functions that generates trust score out of 100, the higher the better

Then i have a seperate file "contentProcess.py" that contains all my functions related to processing the content of the file itself, it contains 6 functions being,

processContent -> it takes the content in byte form and returns parsed email object
parseEmailHeader -> it takes the message object as value and return dict with needed keys and values for risk evaluation
getDomain -> strips just the domain from a header line
getDmarcPolicy -> from the email file extract the value of 'P=' from dmarc policy
getBody -> it takes the message object and returns readable body out of it
getUrlDomain -> takes a ulr and returns the extracted main domain from it

Another file i have is "validation.py", this file contains all the functions related to validating the content to get to scoring stage of the program. It only contains three functions,

checkDomainMismatch -> this returns the value of from and return domain match either True Or False
extractIOCS -> this takes the plain string we got form "getBody()" and extracts list of all URL's and IP's from the file and returns them as a list in a dict
checkURL -> this helps get values for passURLS to decide the score assigned based on URL factor

Then I have the test file "test_project.py" which test the three functions getFilePath, getContentFromFile, scoreEmail for mutiple cases including edge cases.

## Design Decisions Points Where I Had To Think & Figure Out

In this program the open() uses an arguemnt 'rb' which open the file in byte form instead of normla strings to make it easer to function later

The Body preference in "getBody()" is HTML to get URL's which is not possible in plain

The Link Matching heps in edge cases for ex. if i dont have the '.' then 'notgoogle.com' will get accepeted since there is a 'google.com' at end but this is a not a legit domain.

ScoreFactor -> The domain part awards 20 points if domains from and return match but in case they don't we check the DMARC policy and if their dmarc policy is strong they are excused for having seprate domains and still awarded the 20 points.

## Limitations

This is just a base version or maybe just a foundation or as i call It version1.

It has many flaws it only uses 3 factors to detemine the score, it never checks the URL themselves, the URL padding can become an issue and there is a scoring flaw as well.

I plan to work on it after cs50 as well and extend it to a real phish-triage with way more check factors and batch processing and maybe GUI as well.

## What Happens & Why

Assuming user wants to run anaysis of a file located at,

samples/exampleLegit.eml

First user uses command line to start the programm while provding the FilePath to the email file and then the whole system argument in stored in a list variable called 'argList'

The command would look like this

python project.py samples/exampleLegit.eml

and would be stored in argList as [project.py, samples/exampleLegit.eml]

Since we have the argument stored now i take it and run it through "getFilePath" function which make sure user has not given any less or extra args then needed and if the checks pass then it return the final filePath after removing any extra sidespaces or any ', " if any entered by user to prevent any problems in functioning.

Now that we have file path we take it get content from that file if it exist and for that we use "processContnet" function, its parameter is another another function "getCotentFromFile" which is called by main to get the raw content out of the file if it exist on the path given and if there is no file or path is invalid it exits the programm. Once we have the contnet the function "processContnet" fire with the raw content from email file this time and returns email object to use later which is easier to get values out of and we store it in variable 'msg'.

Then we get the data out of the contnet we just got which can help us in validation of the email, we run function "parseEmailHeader" with content as parameter to get a dict of needed keys and words consisiting of [From, Subject, ReturnPath, AuthenticationResults, Body] and store it in a varaible 'headerData'. For the value of Body we call another function getBody which helps to get the body in more readble format.

Next step is to get from and return domains and store then in their resepctive varibales by running their headerValue we got in the dict headerData with function "getDomain" that takes just the domain out of the header for example given 'example1@gmail.com' it will return 'gmail.com'

We also need to consider another factor while calculating the score which is the URL's and for that we have fuction extractIOCS whihc takes the 'Body' from headerData and uses re.findall alonng wiht some regex to get list of all URL's and IP's present in the Body. The return value which is a dict containt list of URLS and Ip's is stored in a varibale names iocs.

Next part is running some checks to calcualte score, we run three checks here to get back 4 values,

Check1 -> we use "checkDomainMismatch" by passing from and return domain values to get a True and False back telling us if they match or not

Check2 -> we use "getDmarcPolicy" to get value of 'P=' which can help us evaluate the security of the Domain itself.

Check3 -> we use "checkURL" by passing the list of URLS's we created before and stores in 'iocs' along with the the value of from domain to get two values back in return, 'totalURLS' which is total number of URl's that exist in the email and the second 'passURLS' which in numner of URL's that match the from domain this is import bcz the more they pass the better the score. The "checkURL" function uses "getUrlDomain" function to get URL out of the raw url using built-in url parsing feautres.

This part of the programm since we are reaching the end we use some print statements to print a report of why what score will be given and how many points will be awarded for what until we reach the final score print statment where we finally calculate the score.

To get the score we call the fuction "scoreEmail" and pass in the result of out domain check, the result of dmarc check along wiht URL variables.

It start with the variable totalScore and assigns it score based factors given,

1st -> The URL part awards upto 50 points, if the number of URL present in file is 20 and 10 pass then the file gets 25 points its always a liner calcuations to keep it simple

2nd -> This part awards 20 points if domains from and return match but in case they don't we check the DMARC policy and if their dmarc policy is strong they are excused for having seprate domains and still awarded the 20 points.

3rd -> If dmarc policy is strong you get awarded 30 points otherwise nothing

All these factor make score out 100 points and returns the score after rounding it to nearest INT before printing it for the user along wiht the detailed report.
