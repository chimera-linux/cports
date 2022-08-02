pkgname = "chimerautils-tiny"
_commit="a1310e9f9c0345875ef7c8bccafe278e16becefc"
pkgver = "0.0.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--bindir=libexec/chimerautils-tiny",
    "--sbindir=libexec/chimerautils-tiny",
    "--libexecdir=libexec/chimerautils-tiny/libexec",
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
url = "https://github.com/chimera-linux/chimerautils"
source = f"https://github.com/chimera-linux/chimerautils/archive/{_commit}.tar.gz"
sha256 = "1b13f1f8f02983b5c58739228cf4c1c8e04cfd12ed0fdceb281aaa81a1d25bb8"

def post_install(self):
    # drop manpages
    self.rm(self.destdir / "usr/share", recursive = True)
