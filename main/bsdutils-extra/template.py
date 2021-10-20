pkgname = "bsdutils-extra"
_commit="66541d372e13de2e236d5d3a385e4ea6359bf421"
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
sha256 = "9025cf42e5a9a4e6f4c1b0f2444ab7a9e60c683c28577df88f521af6476dceb6"
# no test suite
options = ["bootstrap", "!check"]
