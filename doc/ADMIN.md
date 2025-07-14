# WGDashboard Administration

## Configured information

- The app install dir is `__INSTALL_DIR__`
- The default username is `__WG_USER__`
- If you don't set a password, it will be randomly generated and available during post-install. You can retrieve it using `yunohost app setting __APP__ wg_password`, it is also shown in the post install window.

## WireGuard Integration

This package is designed to coexist with other YunoHost WireGuard packages:

- Uses ACL-based permissions instead of conflicting ownership
- Detects existing WireGuard installations
- Shares `/etc/wireguard` directory safely
- Conditional system configuration to avoid conflicts
