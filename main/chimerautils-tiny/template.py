pkgname = "chimerautils-tiny"
_commit="f5e7bc7ba541b46ff6ff8fe73b3b27a599e898b1"
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
sha256 = "956250245473544f06b247fffa9a01060957ab858e6b9551ecc1ef25f76bd136"

def post_install(self):
    # drop manpages
    self.rm(self.destdir / "usr/share", recursive = True)
