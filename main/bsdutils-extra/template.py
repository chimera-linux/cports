pkgname = "bsdutils-extra"
_commit="abc84ae47425bcebfbbd4430cbf53ed480bfedb0"
pkgver = "0.0.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["openssl-devel"]
depends = ["bsdutils"]
pkgdesc = "Extra tools to complement bsdutils"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdutils-extra"
source = f"https://github.com/chimera-linux/bsdutils-extra/archive/{_commit}.tar.gz"
sha256 = "9d7a9b35e138fbe0cba83dea68da9936c0a8ab304514148dd618ed8b4ebfc637"
# no test suite
options = ["bootstrap", "!check", "lto"]
