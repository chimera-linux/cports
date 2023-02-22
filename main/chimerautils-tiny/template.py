pkgname = "chimerautils-tiny"
pkgver = "13.1.1"
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
source = f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "29302568bb615d33d5e65ea0de9b9abe31b7ff7aeea870923bc85de53e164fa4"
hardening = ["vis", "cfi"]

def post_install(self):
    # drop manpages
    self.rm(self.destdir / "usr/share", recursive = True)
    # drop sysconfdir
    self.rm(self.destdir / "etc", recursive = True)
