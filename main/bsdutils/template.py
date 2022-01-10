pkgname = "bsdutils"
_commit="d7050267fbc655a8b1a01bae58f23b304e0daf32"
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
sha256 = "30e947783d0a3155231d6fd3f5a3fe5d1576622734c518075e27052c6cfd970c"
# no test suite
options = ["bootstrap", "!check"]

if self.stage > 0:
    makedepends += ["linux-headers"]
