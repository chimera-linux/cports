pkgname = "chafa"
pkgver = "1.14.5"
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
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://hpjansson.org/chafa"
source = f"https://github.com/hpjansson/chafa/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "788cb29e6d9cd29578c2040b3a11f69f4c9408e04f6c93c994c071e2a85d5ba4"


@subpackage("chafa-devel")
def _(self):
    return self.default_devel()
