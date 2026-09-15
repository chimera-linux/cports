pkgname = "libxml2"
pkgver = "2.14.6"
pkgrel = 3
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--enable-static",
    "--with-history",
    "--with-icu",
    "--with-legacy",
    "--with-threads",
    "--without-python",
]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "icu-devel",
    "libedit-readline-devel",
    "ncurses-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "XML parsing library"
license = "MIT"
url = "http://www.xmlsoft.org"
source = f"$(GNOME_SITE)/libxml2/{pkgver[: pkgver.rfind('.')]}/libxml2-{pkgver}.tar.xz"
sha256 = "7ce458a0affeb83f0b55f1f4f9e0e55735dbfc1a9de124ee86fb4a66b597203a"


def post_install(self):
    self.install_license("Copyright")


@subpackage("libxml2-devel")
def _(self):
    return self.default_devel(
        extra=["usr/share/gtk-doc", "usr/share/doc/libxml2"]
    )


@subpackage("libxml2-progs")
def _(self):
    return self.default_progs()
