pkgname = "stunnel"
pkgver = "5.74"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf-archive", "automake", "libtool"]
makedepends = ["openssl3-devel"]
checkdepends = ["python-cryptography"]
pkgdesc = "TLS proxy to add TLS encryption to existing clients and servers"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "GPL-2.0-or-later"
url = "https://stunnel.org"
source = f"{url}/downloads/stunnel-{pkgver}.tar.gz"
sha256 = "9bef235ab5d24a2a8dff6485dfd782ed235f4407e9bc8716deb383fc80cd6230"


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.rename("etc/stunnel", "usr/share/examples/stunnel", relative=False)
