pkgname = "libxml2"
pkgver = "2.14.2"
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
license = "MIT"
url = "http://www.xmlsoft.org"
source = f"$(GNOME_SITE)/libxml2/{pkgver[: pkgver.rfind('.')]}/libxml2-{pkgver}.tar.xz"
sha256 = "353f3c83535d4224a4e5f1e88c90b5d4563ea8fec11f6407df640fd28fc8b8c6"


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
