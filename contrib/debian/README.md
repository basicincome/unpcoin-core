
Debian
====================
This directory contains files used to package unpayd/unpay-qt
for Debian-based Linux systems. If you compile unpayd/unpay-qt yourself, there are some useful files here.

## unpay: URI support ##


unpay-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install unpay-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your unpay-qt binary to `/usr/bin`
and the `../../share/pixmaps/unpay128.png` to `/usr/share/pixmaps`

unpay-qt.protocol (KDE)

