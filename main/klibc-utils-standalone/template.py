pkgname = "klibc-utils-standalone"
_commit = "ed98c6b24cbe5989d22fda762ad58e29dd5d6592"
pkgver = "0.0.1"
pkgrel = 2
build_style = "meson"
configure_args = ["--libexecdir=/usr/lib"]  # XXX drop libexec
hostmakedepends = ["meson"]
makedepends = ["linux-headers"]
pkgdesc = "Standalone utilities from klibc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/chimera-linux/klibc-utils-standalone"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "f4ab09ff29cfb360fe004d1235ed248c033888cc5e3a389121568a4c2005f938"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING.md")
