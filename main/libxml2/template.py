pkgname = "libxml2"
pkgver = "2.13.5"
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
hostmakedepends = [
    "automake",
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
source = f"$(GNOME_SITE)/libxml2/{pkgver[: pkgver.rfind('.')]}/libxml2-{pkgver}.tar.xz"
sha256 = "74fc163217a3964257d3be39af943e08861263c4231f9ef5b496b6f6d4c7b2b6"


def post_install(self):
    # Delete unwanted python static lib that gets built due to --enable-static
    self.uninstall("usr/lib/python*/site-packages/*.a", glob=True)
    self.install_license("Copyright")


@subpackage("libxml2-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends = ["python"]
    return ["usr/lib/python*"]


@subpackage("libxml2-devel")
def _(self):
    return self.default_devel(
        extra=["usr/share/gtk-doc", "usr/share/doc/libxml2"]
    )


@subpackage("libxml2-progs")
def _(self):
    return self.default_progs()
