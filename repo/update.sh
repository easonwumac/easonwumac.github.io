rm Packages
dpkg-scanpackages -m deb / > Packages
bzip2 -fks Packages
gzip -f -k Packages