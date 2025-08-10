#!/bin/bash

# Set up environment variables for cron
CRON_SCRIPT="
# Set environment variables for remote backup script
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOME=/home/admin
LANG=en_US.UTF-8
SHELL=/bin/bash

# Remote backup every 5 minutes
*/5 * * * * /home/admin/Downloads/ISMv900/remote_backup_database.sh >> /home/admin/Downloads/ISMv900/cron_log.txt 2>&1
"

# Add proper cron job with full environment
echo "$CRON_SCRIPT" | crontab -

# Make sure scripts are executable
chmod +x /home/admin/Downloads/ISMv900/remote_backup_database.sh
chmod +x /home/admin/Downloads/ISMv900/setup_remote_backup.sh

# Create cron log file
touch /home/admin/Downloads/ISMv900/cron_log.txt
chmod 666 /home/admin/Downloads/ISMv900/cron_log.txt

echo "Remote backup task has been scheduled to run every 5 minutes"
echo "To check if it's installed, run: crontab -l"
echo "To monitor cron execution, check: /home/admin/Downloads/ISMv900/cron_log.txt"
echo "To monitor backup logs, check: /home/admin/Downloads/ISMv900/remote_backup_log.txt"
