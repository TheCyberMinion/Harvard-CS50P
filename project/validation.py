import re
from contentProcess import getUrlDomain

# check from and return domain against each other
def checkDomainMismatch(fromDomain, returnDomain):
    if fromDomain is None or returnDomain is None:
        return False
    elif (fromDomain != returnDomain):
        return True
    else:
        return False

# extract IOCS values(only urls and IP'S for now)
def extractIOCS(text):
    if text is None:
        return {'urls' : [] , 'ips' : []}
    else:

        # make list of urls
        urls = re.findall(r'https?://[^\s<>"\']+', text)
        urls = list(dict.fromkeys(urls))

        # make list of ip's
        ips = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', text)
        ips = list(dict.fromkeys(ips))

        return {'urls' : urls , 'ips' : ips}

# get and returns values for totalurls and passing urls
def checkURL(urlList, domain):
    if domain is None:
        return 0, 0
    else:
        totalDomains = len(urlList)
        validDomains = 0
        for rawURL in urlList:
            url = getUrlDomain(rawURL)
            if url == domain or url.endswith('.' + domain):
                validDomains += 1
        return totalDomains, validDomains
