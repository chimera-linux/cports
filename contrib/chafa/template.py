pkgname = "chafa"
pkgver = "1.14.4"
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
    "xsltproc",
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
sha256 = "65b084173eb904c3e0b4eafd561cf0f676a17fe19b0d47b98118808f0646c92e"


@subpackage("chafa-devel")
def _(self):
    return self.default_devel()
