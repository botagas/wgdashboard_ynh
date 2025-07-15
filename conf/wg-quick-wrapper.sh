#!/bin/bash
# WireGuard Quick wrapper script for YunoHost WGDashboard
# Automatically adds sudo to wg-quick commands

# Pass all arguments to sudo wg-quick
exec sudo /usr/bin/wg-quick "$@"
