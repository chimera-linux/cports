pkgname = "libxml2"
pkgver = "2.13.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--enable-static",
    "--with-history",
    "--with-icu",
    "--with-legacy",
    "--with-threads",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
    "python-devel",
]
makedepends = [
    "icu-devel",
    "libedit-readline-devel",
    "ncurses-devel",
    "python-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "XML parsing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.xmlsoft.org"
source = f"$(GNOME_SITE)/libxml2/{pkgver[:pkgver.rfind('.')]}/libxml2-{pkgver}.tar.xz"
sha256 = "e7c8f5e0b5542159e0ddc409c22c9164304b581eaa9930653a76fb845b169263"


def post_install(self):
    # Delete unwanted python static lib that gets built due to --enable-static
    self.uninstall("usr/lib/python*/site-packages/*.a", glob=True)
    self.install_license("Copyright")


@subpackage("libxml2-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends = ["python"]
    return ["usr/lib/python*"]


@subpackage("libxml2-devel")
def _devel(self):
    return self.default_devel(
        extra=["usr/share/gtk-doc", "usr/share/doc/libxml2"]
    )


@subpackage("libxml2-progs")
def _progs(self):
    return self.default_progs()
