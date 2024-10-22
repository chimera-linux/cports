pkgname = "klibc-kinit-standalone"
_commit = "f2f5cb9f87598b27ee0a68bc3e5bbe470e6b8827"
pkgver = "0.0.1"
pkgrel = 2
build_style = "meson"
configure_args = ["--libexecdir=/usr/lib"]  # XXX drop libexec
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["zlib-ng-compat-devel", "libcap-devel", "linux-headers"]
pkgdesc = "Standalone kinit tools from klibc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/chimera-linux/klibc-kinit-standalone"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "b15bb14e33b222299685eb0818274268ea32b4133db834fb038cd0ede08bd926"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING.md")
