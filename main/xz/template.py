pkgname = "xz"
pkgver = "5.6.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = []
provides = [self.with_pkgver("liblzma")]
pkgdesc = "XZ compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://tukaani.org/xz"
source = f"https://github.com/tukaani-project/xz/releases/download/v{pkgver}/xz-{pkgver}.tar.gz"
sha256 = "269e3f2e512cbd3314849982014dc199a7b2148cf5c91cedc6db629acdf5e09b"
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
    self.provides = [self.with_pkgver("liblzma-devel")]

    return self.default_devel()
