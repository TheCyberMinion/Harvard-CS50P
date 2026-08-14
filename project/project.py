import sys
from contentProcess import parseEmailHeader, getDmarcPolicy, processContent, getDomain
from validation import checkDomainMismatch, extractIOCS, checkURL

def main():

    # list of systme arguments provided by user
    argList = sys.argv

    # assign filepath based on system args
    filePath = getFilePath(argList)

    # assign the content of .eml file
    msg = processContent(getContentFromFile(filePath))

    # get dict of keys and data
    headerData = parseEmailHeader(msg)

    # get from and retrun domains
    fromDomain = getDomain(headerData['From'])
    returnDomain = getDomain(headerData['ReturnPath'])

    # get dict containing list of url and a list Ip's
    iocs = extractIOCS(headerData['Body'])

    # running checks 1,2,3
    # check1 -> from and return domain against each other
    domainCheck = checkDomainMismatch(fromDomain, returnDomain)
    # check2 -> get dmarcPolicy value of 'P'
    dmarcPolicy = getDmarcPolicy(headerData['AuthenticationResults'])
    # check3 -> url located inside the email pass/fail values
    totalURLS, passURLS  = checkURL(iocs['urls'], fromDomain)

    #score report
    if domainCheck is False or dmarcPolicy == 'REJECT':
        print('Domain Check Passed +20 points')
    else:
        print('Domain Check Failed +0 points')

    if dmarcPolicy == 'REJECT':
        print('DMARC Policy Passed +30 points')
    else:
        print('DMARC Policy Failed +0 points')

    print(f"Total URL's In Email: {totalURLS}")
    print(f"URL's In Email With Sender Domain: {passURLS}")
    if totalURLS == 0:
        print(f'Points Assigned: +0 points')
    else:
        print(f'Points Assigned: +{round((passURLS/totalURLS) * 50)} points')

    # gets and prints final score at end of the report
    print(f'Final Score: {scoreEmail(domainCheck, dmarcPolicy, totalURLS, passURLS)}')

# testFunction1
# return final score emails based on factor identified in file
def scoreEmail(domainCheck, dmarcPolicy, totalURLS, passURLS):
    # domainCheck has 20 points if domain match but if they are not
    # then dmarc policy is used to evaluate
    # dmarc Polcy Pas 30 points if is REJECT
    # url has 50 points total
    if totalURLS == 0:
        totalScore = 0
    else:
        totalScore = (passURLS/totalURLS) * 50
    if domainCheck is False or dmarcPolicy == 'REJECT':
        totalScore += 20
    if dmarcPolicy == 'REJECT':
        totalScore += 30
    return round(totalScore)

# testFunction2
# gets the file path and sends it out
def getFilePath(argList):
    if len(argList) < 2:
        sys.exit('File Path Not Provided')
    elif len(argList) == 2:
        #strips sidespaces and optional ' or " if they exist and returns the value
        return (argList[1]).strip().strip("'\"")
    else:
        sys.exit('Too Many Arguments Provided')

# testFunction3
# this gets the content of the .eml file as bytes if it exist
# otherwise exits with a message if the file does not exist
# or if the file path is invalid
def getContentFromFile(filePath):
    try:
        with open(filePath, 'rb') as file:
            return file.read()
    except OSError as error:
        sys.exit(f'Could Not Read The File: {error}')

if __name__ == '__main__':
    main()
