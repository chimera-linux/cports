pkgname = "libcaca"
pkgver = "0.99_beta20"
pkgrel = 3
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake", "pkgconf", "python", "slibtool"]
makedepends = ["ncurses-devel", "imlib2-devel", "libx11-devel"]
pkgdesc = "Graphics library that outputs text instead of pixels"
license = "WTFPL"
url = "http://caca.zoy.org/wiki/libcaca"
source = f"https://github.com/cacalabs/libcaca/releases/download/v{pkgver.replace('_', '.')}/libcaca-{pkgver.replace('_', '.')}.tar.gz"
sha256 = "8ad74babc63bf665b0b2378d95b4da65b7493c11bd9f3ac600517085b0c4acf2"


def post_install(self):
    from cbuild.util import python

    self.install_license("COPYING")

    d = self.destdir / "usr/lib"
    # remove broken autotools-compiled junk
    for f in d.rglob("*.pyo"):
        f.unlink()
    for f in d.rglob("*.pyc"):
        f.unlink()
    # actually compile properly
    python.precompile(self, "usr/lib")


@subpackage("libcaca-devel")
def _(self):
    return self.default_devel()


@subpackage("libcaca-progs")
def _(self):
    return self.default_progs()
