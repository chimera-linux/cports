pkgname = "usbmuxd"
pkgver = "1.1.1"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--without-systemd"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = [
    "libimobiledevice-devel",
    "libusb-devel",
]
pkgdesc = "USB multiplex daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/usbmuxd/archive/{pkgver}.tar.gz"
sha256 = "e7ce30143e69d77fc5aa6fb0cb5f0cfcdbeff47eb1ac7fd90ac259a90de9fadd"


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "usbmuxd")
