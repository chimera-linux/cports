pkgname = "enchant"
pkgver = "2.8.21"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-relocatable", "--disable-static"]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "vala",
]
makedepends = [
    "aspell-devel",
    "glib-devel",
    "hunspell-devel",
    "icu-devel",
    "libtool-devel",
    "nuspell-devel",
    "unittest-cpp",
]
pkgdesc = "Generic spell checking library"
license = "LGPL-2.1-or-later"
url = "http://rrthomas.github.io/enchant"
source = f"https://github.com/rrthomas/enchant/releases/download/v{pkgver}/enchant-{pkgver}.tar.gz"
sha256 = "dd2a762697c463148a8f59867089a5ebf2dd1449d869f93764b76c12bcf8acc0"


@subpackage("enchant-devel")
def _(self):
    return self.default_devel()


@subpackage("enchant-progs")
def _(self):
    return self.default_progs()
