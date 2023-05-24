pkgname = "libexif"
pkgver = "0.6.24"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["ac_cv_path_DOXYGEN=false"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext-tiny-devel"]
pkgdesc = "EXIF metadata library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/libexif/libexif"
source = f"{url}/archive/{pkgname}-{pkgver.replace('.', '_')}-release.tar.gz"
sha256 = "d3fb7c47829ec4d2def39aa38f4c35a0891763448a05dbf216a329a12bf198f9"


@subpackage("libexif-devel")
def _devel(self):
    return self.default_devel()
