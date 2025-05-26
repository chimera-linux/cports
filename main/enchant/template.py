pkgname = "enchant"
pkgver = "2.8.5"
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
sha256 = "27bf35078dddb9746ef040a9fc5bd07fc3f6be6e1ee082d4d7e00d09c524d89a"


@subpackage("enchant-devel")
def _(self):
    return self.default_devel()


@subpackage("enchant-progs")
def _(self):
    return self.default_progs()
