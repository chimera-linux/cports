pkgname = "xz"
pkgver = "5.6.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = []
provides = [f"liblzma={pkgver}-r{pkgrel}"]
pkgdesc = "XZ compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://tukaani.org/xz"
source = f"https://github.com/tukaani-project/xz/releases/download/v{pkgver}/xz-{pkgver}.tar.bz2"
sha256 = "d300422649a0124b1121630be559c890ceedf32667d7064b8128933166c217c8"
options = ["bootstrap"]


if self.stage > 0:
    makedepends += ["linux-headers"]


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
