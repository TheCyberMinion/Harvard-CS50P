import re
import email, email.policy, email.utils
from urllib.parse import urlparse

# return the contnet of .eml file in form of bytes for better parsing
def processContent(content):
    return email.message_from_bytes(content, policy=email.policy.default)

# return dict with values and keys needed for evaluation
def parseEmailHeader(content):
    headerData = {}

    # keys and data
    headerData['From'] = content['From']
    headerData['Subject'] = content['Subject']
    headerData['ReturnPath'] = content['Return-Path']
    headerData['AuthenticationResults'] = content['Authentication-Results']
    headerData['Body'] = getBody(content)

    return headerData

# returns end domain name for a header
def getDomain(header):
    if header is None:
        return None
    else:
        _ , address =  email.utils.parseaddr(header)
        if '@' not in address:
            return None
        else:
            _ , domainName = address.rsplit('@', 1)
            return domainName.lower()

# extracts the value of p= from the dmarc policy of email body
def getDmarcPolicy(authData):
    if authData is None:
        return None
    else:
        if matches := re.search(r'dmarc=[A-Za-z]+ \(p=([A-Za-z]+)', authData):
            return matches.group(1).upper()
        else:
            return None

# return readbale txt of BODY out of bytes for IOCS
def getBody(content):
    cBody = content.get_body(preferencelist=('html', 'plain'))
    if cBody is None:
        return None
    else:
        return cBody.get_content()

# extracts and returns the main domain from a URL
def getUrlDomain(url):
    return urlparse(url).hostname.lower()
