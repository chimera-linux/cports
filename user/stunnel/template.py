pkgname = "stunnel"
pkgver = "5.75"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf-archive", "automake", "libtool"]
makedepends = ["openssl3-devel"]
checkdepends = ["python-cryptography"]
pkgdesc = "TLS proxy to add TLS encryption to existing clients and servers"
license = "GPL-2.0-or-later"
url = "https://stunnel.org"
source = f"{url}/downloads/stunnel-{pkgver}.tar.gz"
sha256 = "0c1ef0ed85240974dccb94fe74fb92d6383474c7c0d10e8796d1f781a3ba5683"


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.rename("etc/stunnel", "usr/share/examples/stunnel", relative=False)
