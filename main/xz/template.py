pkgname = "xz"
pkgver = "5.2.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "XZ compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:xz"
url = "https://tukaani.org/xz"
source = f"https://tukaani.org/xz/xz-{pkgver}.tar.bz2"
sha256 = "5117f930900b341493827d63aa910ff5e011e0b994197c3b71c08a20228a42df"
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
        self.rm(self.destdir / "usr/share/man/de/man1" / (tool + ".1"))

@subpackage("liblzma")
def _lib(self):
    self.pkgdesc = "XZ-format compression library"

    return self.default_libs()

@subpackage("liblzma-devel")
def _devel(self):
    self.pkgdesc = "XZ-format compression library (development files)"

    return self.default_devel()
