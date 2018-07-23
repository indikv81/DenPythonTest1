import pycurl
import certifi


def info(self):
    "Return a dictionary with all info on the last response."
    m = {}
    m['effective-url'] = self.getinfo(self.EFFECTIVE_URL)
    m['http-code'] = self.getinfo(self.HTTP_CODE)
    m['total-time'] = self.getinfo(self.TOTAL_TIME)
    m['namelookup-time'] = self.getinfo(self.NAMELOOKUP_TIME)
    m['connect-time'] = self.getinfo(self.CONNECT_TIME)
    m['pretransfer-time'] = self.getinfo(self.PRETRANSFER_TIME)
    m['redirect-time'] = self.getinfo(self.REDIRECT_TIME)
    m['redirect-count'] = self.getinfo(self.REDIRECT_COUNT)
    m['size-upload'] = self.getinfo(self.SIZE_UPLOAD)
    m['size-download'] = self.getinfo(self.SIZE_DOWNLOAD)
    m['speed-upload'] = self.getinfo(self.SPEED_UPLOAD)
    m['header-size'] = self.getinfo(self.HEADER_SIZE)
    m['request-size'] = self.getinfo(self.REQUEST_SIZE)
    m['content-length-download'] = self.getinfo(self.CONTENT_LENGTH_DOWNLOAD)
    m['content-length-upload'] = self.getinfo(self.CONTENT_LENGTH_UPLOAD)
    m['content-type'] = self.getinfo(self.CONTENT_TYPE)
    m['response-code'] = self.getinfo(self.RESPONSE_CODE)
    m['speed-download'] = self.getinfo(self.SPEED_DOWNLOAD)
    m['ssl-verifyresult'] = self.getinfo(self.SSL_VERIFYRESULT)
    m['filetime'] = self.getinfo(self.INFO_FILETIME)
    m['starttransfer-time'] = self.getinfo(self.STARTTRANSFER_TIME)
    m['redirect-time'] = self.getinfo(self.REDIRECT_TIME)
    m['redirect-count'] = self.getinfo(self.REDIRECT_COUNT)
    m['http-connectcode'] = self.getinfo(self.HTTP_CONNECTCODE)
    m['httpauth-avail'] = self.getinfo(self.HTTPAUTH_AVAIL)
    m['proxyauth-avail'] = self.getinfo(self.PROXYAUTH_AVAIL)
    m['os-errno'] = self.getinfo(self.OS_ERRNO)
    m['num-connects'] = self.getinfo(self.NUM_CONNECTS)
    m['ssl-engines'] = self.getinfo(self.SSL_ENGINES)
    m['cookielist'] = self.getinfo(self.INFO_COOKIELIST)
    m['lastsocket'] = self.getinfo(self.LASTSOCKET)
    #m['ftp-entry-path'] = self.getinfo(self.FTP_ENTRY_PATH)
    return m

curl = pycurl.Curl()
curl.setopt(pycurl.CAINFO, certifi.where())
print(certifi.where())
print('------------------------------------------------------------------------------------------------------')
curl.setopt(pycurl.URL, 'https://ya.ru')
curl.perform()
print('------------------------------------------------------------------------------------------------------')
print(curl.getinfo(curl.HTTP_CODE))
print('------------------------------------------------------------------------------------------------------')
#print(curl.getinfo(curl.FTP_ENTRY_PATH))

print(info(curl))

