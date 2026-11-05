pkgname = "cifs-utils"
pkgver = "7.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--sbindir=/usr/bin",
    "--enable-systemd=no",
    "--disable-dependency-tracking",  # speed up build
    "--with-libcap=no",  # have libcap-ng so not needed
]
configure_gen = []
make_dir = "."
make_install_args = ["ROOTSBINDIR=/usr/bin"]
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "heimdal-devel",
    "keyutils-devel",
    "libcap-ng-devel",
    "linux-pam-devel",
    "python-docutils",
    "samba-winbind-devel",
    "talloc-devel",
]
depends = ["cmd:python!python"]  # for python scripts
pkgdesc = "CIFS filesystem user-space tools"
license = "GPL-3.0-or-later"
url = "https://wiki.samba.org/index.php/LinuxCIFS_utils"
source = [
    f"https://download.samba.org/pub/linux-cifs/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
]
sha256 = "9f3750f402520b15c2c8eb52fd485df6ea77e5e66fe5e39ce8ac4386c32c0296"
hardening = ["vis", "cfi"]
