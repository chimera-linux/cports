pkgname = "chimerautils-tiny"
_commit="670908b6c79f60c7e48d682b3e03996994513cbb"
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
sha256 = "dbdfd753b22bd19fc3f214f9aead12c603b114636466b3c3aff09b93c485bc18"

def post_install(self):
    # drop manpages
    self.rm(self.destdir / "usr/share", recursive = True)
