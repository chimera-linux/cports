pkgname = "xz"
pkgver = "5.4.5"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
provides = [f"liblzma={pkgver}-r{pkgrel}"]
pkgdesc = "XZ compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:xz"
url = "https://tukaani.org/xz"
source = f"https://tukaani.org/xz/xz-{pkgver}.tar.bz2"
sha256 = "8ccf5fff868c006f29522e386fb4c6a1b66463fbca65a4cfc3c4bd596e895e79"
options = ["bootstrap"]


def post_install(self):
    self.install_license("COPYING")
    self.rm(self.destdir / "usr/share/doc", recursive=True)
    for tool in [
        "xzgrep",
        "xzfgrep",
        "xzegrep",
        "lzgrep",
        "lzfgrep",
        "lzegrep",
        "xzdiff",
        "lzdiff",
        "xzcmp",
        "lzcmp",
        "xzless",
        "xzmore",
        "lzless",
        "lzmore",
    ]:
        self.rm(self.destdir / "usr/bin" / tool)
        self.rm(self.destdir / "usr/share/man/man1" / (tool + ".1"))
        for lang in (self.destdir / "usr/share/man").iterdir():
            if lang.name == "man1":
                continue
            self.rm(lang / "man1" / (tool + ".1"), force=True)


@subpackage("xz-devel")
def _devel(self):
    self.provides = [f"liblzma-devel={pkgver}-r{pkgrel}"]

    return self.default_devel()
