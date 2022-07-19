pkgname = "bsdutils-tiny"
_commit="d4182ca7a0afd33a199f433af049800a944c93a6"
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
sha256 = "5a4f7be8fca0139f2b58eb7c2ed8fb15426c60598368af7449c7611502d35e60"

def post_install(self):
    # drop manpages
    self.rm(self.destdir / "usr/share", recursive = True)
