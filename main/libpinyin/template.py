pkgname = "libpinyin"
pkgver = "2.10.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-dbm=KyotoCabinet", "--enable-libzhuyin"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext"]
makedepends = ["kyotocabinet-devel", "glib-devel"]
pkgdesc = "Algorithms core for intelligent sentence-based Chinese pinyin IMEs"
license = "GPL-3.0-or-later"
url = "https://github.com/libpinyin/libpinyin"
source = f"{url}/releases/download/{pkgver}/libpinyin-{pkgver}.tar.gz"
sha256 = "3fe786ff2c2059bdbdf9d8d752db691a516a941a977521955fe0af3f0b4db299"


@subpackage("libpinyin-devel")
def _(self):
    return self.default_devel()
