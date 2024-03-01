pkgname = "chafa"
pkgver = "1.14.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-man"]
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "docbook-xsl-nons",
    "gm4",
    "gmake",
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
sha256 = "faefc09807c955c882fa044947fc939952862f6e8d2e242262dbcc9f97e108ef"


@subpackage("chafa-devel")
def _devel(self):
    return self.default_devel()
