pkgname = "bsdutils-tiny"
_commit="c2f7b6eba186633b357176e1ba7881c01a2aab17"
pkgver = "0.0.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--bindir=libexec/bsdutils-tiny",
    "--sbindir=libexec/bsdutils-tiny",
    "-Dstatic_fts=true",
    "-Dstatic_rpmatch=true",
    "-Dcolor_ls=false",
    "-Dlibcrypto=disabled",
    "-Dlibedit=disabled",
]
hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
makedepends = [
    "musl-fts-devel", "musl-rpmatch-devel", "libxo-tiny-devel",
    "linux-headers",
]
pkgdesc = "FreeBSD userland utilities (tiny version)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdutils"
source = f"https://github.com/chimera-linux/bsdutils/archive/{_commit}.tar.gz"
sha256 = "dea57d715d98e7206a113dc1039542b3c330d3ead6dc8e49d2ece50e604a3c86"

def post_install(self):
    # drop manpages
    self.rm(self.destdir / "usr/share", recursive = True)
