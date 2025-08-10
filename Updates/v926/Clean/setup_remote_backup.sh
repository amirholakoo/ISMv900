#!/bin/bash

# Setup passwordless SSH for database backups to remote Raspberry Pi
REMOTE_IP="192.168.1.184"
REMOTE_USER="admin"
REMOTE_DIR="/home/admin/Downloads/ISMv900"

echo "Setting up passwordless SSH to $REMOTE_USER@$REMOTE_IP"

# Check if SSH key exists, if not create one
if [ ! -f ~/.ssh/id_rsa ]; then
    echo "Generating SSH key pair..."
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""
else
    echo "SSH key already exists."
fi

# Create .ssh directory on remote host if it doesn't exist
ssh -o "StrictHostKeyChecking=no" $REMOTE_USER@$REMOTE_IP "mkdir -p ~/.ssh"

# Copy the public key to the remote host
echo "Copying SSH public key to remote host..."
cat ~/.ssh/id_rsa.pub | ssh $REMOTE_USER@$REMOTE_IP "cat >> ~/.ssh/authorized_keys"

# Set proper permissions for SSH files on remote host
ssh $REMOTE_USER@$REMOTE_IP "chmod 700 ~/.ssh; chmod 600 ~/.ssh/authorized_keys"

# Create backup directory on remote host
ssh $REMOTE_USER@$REMOTE_IP "mkdir -p $REMOTE_DIR/database_backups"

echo "Passwordless SSH setup complete. Testing connection..."

# Test SSH connection
if ssh -o "BatchMode=yes" $REMOTE_USER@$REMOTE_IP "echo 'SSH connection successful'"; then
    echo "Setup completed successfully! You can now use the remote_backup_database.sh script."
else
    echo "Setup failed. Please check your SSH connection and try again."
fi
