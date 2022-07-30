pkgname = "bsdutils-tiny"
_commit="7ad373fe2b60f33cd2a49f23746bb0ac53cbe743"
pkgver = "0.0.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--bindir=libexec/bsdutils-tiny",
    "--sbindir=libexec/bsdutils-tiny",
    "--libexecdir=libexec/bsdutils-tiny/libexec",
    "-Dstatic_fts=true",
    "-Dstatic_rpmatch=true",
    "-Dcolor_ls=false",
    "-Dlibcrypto=disabled",
    "-Dlibedit=disabled",
    "-Dzlib=disabled",
    "-Dlzma=disabled",
    "-Dbzip2=disabled",
]
hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
makedepends = [
    "musl-fts-devel", "musl-rpmatch-devel", "libxo-tiny-devel",
    "linux-headers", "musl-bsd-headers",
]
pkgdesc = "FreeBSD userland utilities (tiny version)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdutils"
source = f"https://github.com/chimera-linux/bsdutils/archive/{_commit}.tar.gz"
sha256 = "689045a08ac0bb141a23bd42e23464d6e480772da1c76597aed0b5853365a197"

def post_install(self):
    # drop manpages
    self.rm(self.destdir / "usr/share", recursive = True)
