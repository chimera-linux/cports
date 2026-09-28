pkgname = "libxml2"
pkgver = "2.15.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--enable-static",
    "--with-history",
    "--with-icu",
    "--with-legacy",
    "--with-threads",
    "--without-docs",
]
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
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
sha256 = "98087fd181d9070724f3fbc65c7377db03038eb92bd882374daff44940138821"


def post_install(self):
    self.install_license("Copyright")


@subpackage("libxml2-devel")
def _(self):
    return self.default_devel()


@subpackage("libxml2-progs")
def _(self):
    return self.default_progs()
