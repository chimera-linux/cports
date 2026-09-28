pkgname = "stunnel"
pkgver = "5.76"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf-archive", "automake", "libtool"]
makedepends = ["openssl3-devel"]
checkdepends = ["python-cryptography"]
pkgdesc = "TLS proxy to add TLS encryption to existing clients and servers"
license = "GPL-2.0-or-later"
url = "https://stunnel.org"
source = f"{url}/downloads/stunnel-{pkgver}.tar.gz"
sha256 = "cda37eb4d0fb1e129718ed27ad77b5735e899394ce040bb2be28bbb937fd79e1"


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.rename("etc/stunnel", "usr/share/examples/stunnel", relative=False)
