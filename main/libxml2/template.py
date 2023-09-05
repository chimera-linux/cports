pkgname = "libxml2"
pkgver = "2.9.12"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--with-threads", "--with-icu", "--with-history"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "python-devel"]
makedepends = [
    "python-devel",
    "zlib-devel",
    "ncurses-devel",
    "xz-devel",
    "icu-devel",
    "libedit-readline-devel",
]
pkgdesc = "XML parsing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.xmlsoft.org"
source = f"{url}/sources/{pkgname}-{pkgver}.tar.gz"
sha256 = "c8d6681e38c56f172892c85ddc0852e1fd4b53b4209e7f4ebf17f7e2eae71d92"
# some icu test failures
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    # we don't want this in the build
    for f in (self.destdir / "usr/lib").glob("python*"):
        (f / "site-packages/libxml2mod.a").unlink()


@subpackage("libxml2-devel")
def _devel(self):
    self.depends += ["xz-devel", "zlib-devel", "icu-devel"]
    return self.default_devel(
        extra=["usr/share/gtk-doc", f"usr/share/doc/{pkgname}-{pkgver}"]
    )


@subpackage("libxml2-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends = ["python"]
    return ["usr/lib/python*", "usr/share/doc/libxml2-python*"]


@subpackage("libxml2-progs")
def _progs(self):
    return self.default_progs()


configure_gen = []
