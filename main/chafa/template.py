pkgname = "chafa"
pkgver = "1.16.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-man"]
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "docbook-xsl-nons",
    "gm4",
    "libtool",
    "libxml2-progs",
    "pkgconf",
    "libxslt-progs",
]
makedepends = [
    "freetype-devel",
    "glib-devel",
    "libavif-devel",
    "libjpeg-turbo-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libwebp-devel",
]
pkgdesc = "Character art facsimile generator"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://hpjansson.org/chafa"
source = f"https://github.com/hpjansson/chafa/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5b92d2e44647b0a4cd7e34ffa040bd2ae533240382c9610751c7fb36a5595fe4"


@subpackage("chafa-devel")
def _(self):
    return self.default_devel()
