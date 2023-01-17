pkgname = "xz"
pkgver = "5.2.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "XZ compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:xz"
url = "https://tukaani.org/xz"
source = f"https://tukaani.org/xz/xz-{pkgver}.tar.bz2"
sha256 = "1f8a43d9fcf325d049a31fe4514dc8c44a6d00ce8860d48c4212d1e349d2a3ed"
# unmarked api
hardening = ["!vis"]
options = ["bootstrap"]

def post_install(self):
    self.install_license("COPYING")
    self.rm(self.destdir / "usr/share/doc", recursive = True)
    for tool in [
        "xzgrep", "xzfgrep", "xzegrep", "lzgrep", "lzfgrep", "lzegrep",
        "xzdiff", "lzdiff", "xzcmp", "lzcmp", "xzless", "xzmore",
        "lzless", "lzmore"
    ]:
        self.rm(self.destdir / "usr/bin" / tool)
        self.rm(self.destdir / "usr/share/man/man1" / (tool + ".1"))
        for lang in (self.destdir / "usr/share/man").iterdir():
            if lang.name == "man1":
                continue
            self.rm(lang / "man1" / (tool + ".1"), force = True)

@subpackage("liblzma")
def _lib(self):
    self.pkgdesc = "XZ-format compression library"

    return self.default_libs()

@subpackage("liblzma-devel")
def _devel(self):
    self.pkgdesc = "XZ-format compression library (development files)"

    return self.default_devel()
