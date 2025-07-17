# WGDashboard Administration

This is NOT MEANT to be public facing or exposed in any shape or form to the internet. WGDashboard requires sudo privileges to an extent, and as such, it is highly discouraged to allow the service to be accessible outside the network.

## System Requirements

- Python 3.9 or higher (automatic compatibility fixes applied during installation if needed)

## Configured information

- The app install dir is `__INSTALL_DIR__`
- The default username is `__WG_USER__`
- If you don't set a password, it will be randomly generated and available during post-install. You can retrieve it using `yunohost app setting __APP__ wg_password`, it is also shown in the post install window.

## WireGuard Integration

This package is designed to coexist with other YunoHost WireGuard packages:

- Uses ACL-based permissions to avoid conflicts or permission issues
- Detects existing WireGuard installations
- Shares `/etc/wireguard` directory safely
- Conditional system configuration to ensure coexistence with other WireGuard implementations
