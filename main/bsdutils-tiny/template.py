pkgname = "bsdutils-tiny"
_commit="309e666117edfbad300181a3c298233420e99ece"
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
sha256 = "49c1e9fe032ea3684b4097a4a501b310f8fe0663f36e6ee56278537636cbcaf4"

def post_install(self):
    # drop manpages
    self.rm(self.destdir / "usr/share", recursive = True)
