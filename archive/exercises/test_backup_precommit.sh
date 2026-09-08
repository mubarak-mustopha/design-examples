BACKUPS=/tmp/backup
# rm -rf $BACKUPS
python precommit_backup.py sample_dir $BACKUPS
tree --charset ascii  $BACKUPS