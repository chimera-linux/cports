pkgname = "bsdutils-extra"
_commit="9a51731999c36e7a59f5dccf152032cf62fdb225"
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
sha256 = "45d4a7711d2af55c9542886c6077fbe1989705f3997accb14a56b794318870e4"
# no test suite
options = ["bootstrap", "!check"]
