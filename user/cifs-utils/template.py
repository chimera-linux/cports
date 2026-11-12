pkgname = "cifs-utils"
pkgver = "7.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-systemd",
]
make_dir = "."
make_install_args = ["ROOTSBINDIR=/usr/bin"]
hostmakedepends = [
    "automake",
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
depends = ["python"]
pkgdesc = "CIFS userspace tools"
license = "GPL-3.0-or-later"
url = "https://wiki.samba.org/index.php/LinuxCIFS_utils"
source = f"https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-{pkgver}.tar.bz2"
sha256 = "9f3750f402520b15c2c8eb52fd485df6ea77e5e66fe5e39ce8ac4386c32c0296"


def post_install(self):
    self.uninstall("usr/include")
