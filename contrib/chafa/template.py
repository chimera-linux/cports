pkgname = "chafa"
pkgver = "1.14.2"
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
sha256 = "c54ca17da967f317791922d5632bd39aa0a1a140eeeb53d087099f1108b8749d"


@subpackage("chafa-devel")
def _(self):
    return self.default_devel()
