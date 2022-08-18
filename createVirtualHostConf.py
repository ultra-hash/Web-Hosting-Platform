import sys

# Takes Second Adhoc values as domain
# command should be python3 or python createVirtualHostConf.py [sub-domain name]

subdomain = sys.argv[1]
base_string = f"""<VirtualHost *:80>
    ServerName {subdomain}.st-site.tk
    ServerAlias {subdomain}.st-site.tk 
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/{subdomain}.st-site.tk
    ErrorLog ${"{APACHE_LOG_DIR}"}/error.log
    CustomLog ${"{APACHE_LOG_DIR}"}/access.log combined
</VirtualHost>"""

print(base_string)
