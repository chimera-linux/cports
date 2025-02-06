pkgname = "libdinitctl"
pkgver = "0_git20250206"
pkgrel = 0
_gitrev = "a3111b9b7fa4174518f2b696e67e1ef664e16589"
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Library to interact with dinit's client protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/libdinitctl"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "9b9b50404a8835dc6c8000c41a093cdcd83c784690275f5b3872ec991faeeacc"


def post_install(self):
    self.install_license("COPYING.md")


@subpackage("libdinitctl-devel")
def _(self):
    return self.default_devel()
