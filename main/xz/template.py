pkgname = "xz"
pkgver = "5.8.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = []
renames = ["liblzma"]
pkgdesc = "XZ compression utilities"
license = "0BSD"
url = "https://tukaani.org/xz"
source = f"https://github.com/tukaani-project/xz/releases/download/v{pkgver}/xz-{pkgver}.tar.gz"
sha256 = "507825b599356c10dca1cd720c9d0d0c9d5400b9de300af00e4d1ea150795543"
options = ["bootstrap"]


if self.stage > 0:
    makedepends += ["linux-headers"]


def post_install(self):
    self.install_license("COPYING")
    self.uninstall("usr/share/doc")
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
        self.uninstall(f"usr/bin/{tool}")
        self.uninstall(f"usr/share/man/man1/{tool + '.1'}")


@subpackage("xz-devel")
def _(self):
    self.renames = ["liblzma-devel"]

    return self.default_devel()
