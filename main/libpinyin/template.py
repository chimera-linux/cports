pkgname = "libpinyin"
pkgver = "2.10.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-dbm=KyotoCabinet", "--enable-libzhuyin"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext"]
makedepends = ["kyotocabinet-devel", "glib-devel"]
pkgdesc = "Algorithms core for intelligent sentence-based Chinese pinyin IMEs"
license = "GPL-3.0-or-later"
url = "https://github.com/libpinyin/libpinyin"
source = f"{url}/releases/download/{pkgver}/libpinyin-{pkgver}.tar.gz"
sha256 = "2c29d9dfd1e0dc521fa654b300cc5560bad82d6bed42e4b3ec9d71098fb26d80"


@subpackage("libpinyin-devel")
def _(self):
    return self.default_devel()
