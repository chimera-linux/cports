pkgname = "libpinyin"
pkgver = "2.10.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-dbm=KyotoCabinet", "--enable-libzhuyin"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext"]
makedepends = ["kyotocabinet-devel", "glib-devel"]
pkgdesc = "Algorithms core for intelligent sentence-based Chinese pinyin IMEs"
license = "GPL-3.0-or-later"
url = "https://github.com/libpinyin/libpinyin"
source = f"{url}/releases/download/{pkgver}/libpinyin-{pkgver}.tar.gz"
sha256 = "bc5fd25724f9863bc329d2aa3d400dce28130efdb819bb96d42db52b0845d37f"


@subpackage("libpinyin-devel")
def _(self):
    return self.default_devel()
