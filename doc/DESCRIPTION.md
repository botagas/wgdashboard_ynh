This package is designed to coexist with other YunoHost WireGuard packages:

- Uses ACL-based permissions to avoid conflicts or permission issues
- Detects existing WireGuard installations
- Shares `/etc/wireguard` directory safely
- Conditional system configuration to ensure coexistence with other WireGuard implementations
- Uses config panels for credential management