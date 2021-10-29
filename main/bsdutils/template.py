pkgname = "bsdutils"
_commit="476c0114038edd084c5868dbbefed61ac35928a1"
pkgver = "0.0.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
makedepends = [
    "acl-devel", "ncurses-devel", "libedit-devel", "openssl-devel",
    "musl-fts-devel", "musl-rpmatch-devel", "libxo-devel"
]
pkgdesc = "FreeBSD userland utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdutils"
source = f"https://github.com/chimera-linux/bsdutils/archive/{_commit}.tar.gz"
sha256 = "f17ba35406cc01e635783afe51e10151ca862cfc9ec92c335438bd96f7d7ed8c"
# no test suite
options = ["bootstrap", "!check"]

if current.stage > 0:
    makedepends += ["linux-headers"]
