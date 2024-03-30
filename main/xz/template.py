pkgname = "xz"
pkgver = "5.6.1"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = []
provides = [f"liblzma={pkgver}-r{pkgrel}"]
pkgdesc = "XZ compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://tukaani.org/xz"
# official release tarballs are backdoored and github repo was taken down
# use our own mirror of commit fd1b975b7851e081ed6e5cf63df946cd5cbdbb94
# grabbed straight from git (without the trigger)
source = f"https://repo.chimera-linux.org/distfiles/xz-{pkgver}.tar.gz"
sha256 = "237284fae40e5f8e9908f0a977e7d0b9a5c7c1c10a41b8e6ed0fb40e930467c8"
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
