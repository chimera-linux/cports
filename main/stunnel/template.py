pkgname = "stunnel"
pkgver = "5.73"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf-archive", "automake", "libtool"]
makedepends = ["openssl-devel"]
checkdepends = ["python-cryptography"]
pkgdesc = "TLS proxy to add TLS encryption to existing clients and servers"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "GPL-2.0-or-later"
url = "https://stunnel.org"
source = f"{url}/downloads/stunnel-{pkgver}.tar.gz"
sha256 = "bc917c3bcd943a4d632360c067977a31e85e385f5f4845f69749bce88183cb38"


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
