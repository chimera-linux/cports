pkgname = "bsdutils"
_commit="fcd11975c10fd553b14ba9098dc3c26568f56f2d"
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
sha256 = "55096a3a3f766b6fee21adf5c9981afe180d70aa43962eed3a6b9aa2a0af354d"
# no test suite
options = ["bootstrap", "!check"]

if not current.bootstrapping:
    makedepends += ["kernel-libc-headers"]
