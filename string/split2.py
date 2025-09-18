# url = "http://www.google.com"
#protocol = http
# subdomain = www
# domain = google
# top level domain = com


url = "http://www.google.com"

protocol, url_wwithout_protocol= url.split(":")

subdomain,domain,top_level_domain  = url_wwithout_protocol.split(".")

subdomain = subdomain.replace("//","")

print(f"protocol : {protocol} sub domain : {subdomain}, domain : {domain}, top level domain :  {top_level_domain}")

