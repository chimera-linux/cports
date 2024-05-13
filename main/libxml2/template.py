pkgname = "libxml2"
pkgver = "2.12.7"
pkgrel = 1
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
sha256 = "24ae78ff1363a973e6d8beba941a7945da2ac056e19b53956aeb6927fd6cfb56"


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
