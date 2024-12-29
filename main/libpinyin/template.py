pkgname = "libpinyin"
pkgver = "2.8.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--with-dbm=KyotoCabinet", "--enable-libzhuyin"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext"]
makedepends = ["kyotocabinet-devel", "glib-devel"]
pkgdesc = "Algorithms core for intelligent sentence-based Chinese pinyin IMEs"
maintainer = "metalparade <comer@live.cn>"
license = "GPL-3.0-or-later"
url = "https://github.com/libpinyin/libpinyin"
source = f"{url}/releases/download/{pkgver}/libpinyin-{pkgver}.tar.gz"
sha256 = "353154f06d71dd0737b77ddcb27cb0dcaddb00f7ccd695bc0314bb42050e9050"


@subpackage("libpinyin-devel")
def _(self):
    return self.default_devel()
