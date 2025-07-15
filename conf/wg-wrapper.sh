#!/bin/bash
# WireGuard wrapper script for YunoHost WGDashboard
# Automatically adds sudo to WireGuard commands

# Pass all arguments to sudo wg
exec sudo /usr/bin/wg "$@"
