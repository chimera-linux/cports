pkgname = "openrsync"
pkgver = "0.5.0_git20250127"
pkgrel = 0
_commit = "a257c0f495af2b5ee6b41efc6724850a445f87ed"
build_style = "configure"
configure_args = ["PREFIX=/usr", "MANDIR=/usr/share/man"]
pkgdesc = "OpenBSD rsync"
license = "ISC"
url = "https://github.com/kristapsdz/openrsync"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "e2def3d03bcb61a584c1f878dd66da4dc7ca889652689096dc0cd0f5bd7371fa"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
