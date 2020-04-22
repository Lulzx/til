# Freeing disk space on your Linux server


To find out where disk space is being used:

1. Get to the root of your machine by running `cd /
`2. Run `sudo du -h –max-depth=1
`3. Note which directories are using a lot of disk space.
4. `cd` into one of the big directories.
5. Run `ls -l` to see which files are using a lot of space. Delete any you don’t need.
6. Repeat steps 2 to 5.
