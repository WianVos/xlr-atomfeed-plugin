import xmltodict
import requests
import os


nugetURL= feedUrl
packageType = "RC"
if preRelease:
    packageType = "PR" #PR= PreRelease and RC = ReleaseCandidate







print "trying to get a response from nuget"
if proxy_string != "":
    print "using proxy %s" % proxy_string
    response = requests.get(nugetURL, auth=requests.auth.HTTPBasicAuth(user, password),verify=False, timeout=100, proxies={proxy_string})
else:
    response = requests.get(nugetURL, auth=requests.auth.HTTPBasicAuth(user, password),verify=False, timeout=100)
print response.status_code
response.raise_for_status()



# try to open from URL
print response.text
doc = xmltodict.parse(response.text)
print "-----------------------------------"
print doc
# only check if feed has been updated

oEntries = doc['feed']['entry']

for i in range(0, len(oEntries)):
    if oEntries[i]['title']['#text'] == packageName:
        if packageType == "PR" and oEntries[i]['m:properties']['d:IsPrerelease']['#text'] == "true":
                if oEntries[i]['m:properties']['d:IsLatestVersion']['#text'] == "true" or oEntries[i]['m:properties']['d:IsAbsoluteLatestVersion']['#text'] == "true":
                    nugetVersionForUse = oEntries[i]['m:properties']['d:Version']
        if packageType == "RC" and oEntries[i]['m:properties']['d:IsPrerelease']['#text'] == "false":
                if oEntries[i]['m:properties']['d:IsLatestVersion']['#text'] == "true":
                    nugetVersionForUse = oEntries[i]['m:properties']['d:Version']

triggerState = nugetVersionForUse
# 'nuget-rabobank',
# '#oJgul!|`i/rl:FT/?@='),verify=False)
