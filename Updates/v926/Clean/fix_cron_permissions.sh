#!/bin/bash

# This script fixes common issues that prevent cron jobs from running properly

# Ensure scripts have the correct permissions
echo "Setting correct permissions for backup scripts..."
chmod +x /home/admin/Downloads/ISMv900/remote_backup_database.sh
chmod +x /home/admin/Downloads/ISMv900/setup_remote_backup.sh
chmod +x /home/admin/Downloads/ISMv900/setup_backup_task.sh

# Create necessary directories and set permissions
echo "Creating necessary directories and setting permissions..."
mkdir -p /home/admin/Downloads/ISMv900
chmod 755 /home/admin/Downloads/ISMv900

# Create log files with proper permissions
echo "Creating log files with proper permissions..."
touch /home/admin/Downloads/ISMv900/cron_log.txt
touch /home/admin/Downloads/ISMv900/remote_backup_log.txt
chmod 666 /home/admin/Downloads/ISMv900/cron_log.txt
chmod 666 /home/admin/Downloads/ISMv900/remote_backup_log.txt

# Test if scripts are executable from cron environment
echo "Testing script execution with limited environment..."
env -i HOME=$HOME PATH=/usr/bin:/bin /home/admin/Downloads/ISMv900/remote_backup_database.sh > /home/admin/Downloads/ISMv900/cron_test_log.txt 2>&1
if [ $? -eq 0 ]; then
    echo "Script executed successfully with limited environment."
else
    echo "Script failed with limited environment. Check /home/admin/Downloads/ISMv900/cron_test_log.txt for details."
fi

# Reload cron service to ensure it picks up changes
echo "Reloading cron service..."
sudo systemctl restart cron || sudo service cron restart

echo "Fix completed. To test if cron is working properly:"
echo "1. Wait for 5 minutes and check if new backup files appear on remote server"
echo "2. Check log files at /home/admin/Downloads/ISMv900/cron_log.txt"
echo "3. Check if cron is running with: ps -ef | grep cron"
echo "4. Check cron logs with: sudo grep CRON /var/log/syslog"
