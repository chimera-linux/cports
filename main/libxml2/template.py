pkgname = "libxml2"
pkgver = "2.12.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-threads",
    "--with-icu",
    "--with-history",
    "--enable-shared",
    "--enable-static",
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
    "zlib-devel",
]
pkgdesc = "XML parsing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.xmlsoft.org"
source = f"$(GNOME_SITE)/libxml2/{pkgver[:pkgver.rfind('.')]}/libxml2-{pkgver}.tar.xz"
sha256 = "a972796696afd38073e0f59c283c3a2f5a560b5268b4babc391b286166526b21"


def post_extract(self):
    # FIXME: even though we build with icu, this fails to parse for some reason
    self.rm("test/icu_parse_test.xml")


def post_install(self):
    # Delete unwanted python static lib that gets built due to --enable-static
    self.rm(self.destdir / "usr/lib/python*/site-packages/*.a", glob=True)
    self.install_license("Copyright")


@subpackage("libxml2-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends = ["python"]
    return ["usr/lib/python*", "usr/share/doc/libxml2/python"]


@subpackage("libxml2-devel")
def _devel(self):
    self.depends += ["xz-devel", "zlib-devel", "icu-devel"]
    return self.default_devel(
        extra=["usr/share/gtk-doc", "usr/share/doc/libxml2"]
    )


@subpackage("libxml2-progs")
def _progs(self):
    return self.default_progs()
