This is NOT MEANT to be public facing or exposed in any shape or form to the internet. WGDashboard requires sudo privileges to an extent, and as such, it is highly discouraged to allow the service to be accessible outside the network.

This installation script will set the admin user (which will be selected by you) and password, which will be randomly generated (unless specified otherwise).

#### Warning
- This does not support SSO or LDAP and is intended for local use only. External exposure is not advised.


#### Recommendations
- Make sure to do proper backups of the whole instance as well as the apps and data within Yunohost. Installs can always break something, so be prepared.
- Even though it does not support SSO/LDAP, you are still able to set the same admin user and password during install, if you wish. It is best practice to use different credentials whenever possible, however.
