pkgname = "libao"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-pulse"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["libpulse-devel"]
pkgdesc = "Cross-platform audio library"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://www.xiph.org/ao"
source = f"https://github.com/xiph/libao/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "df8a6d0e238feeccb26a783e778716fb41a801536fe7b6fce068e313c0e2bf4d"


@subpackage("libao-devel")
def _(self):
    return self.default_devel()
