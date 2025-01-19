pkgname = "libexif"
pkgver = "0.6.25"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["ac_cv_path_DOXYGEN=false"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gettext-devel"]
pkgdesc = "EXIF metadata library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/libexif/libexif"
source = f"{url}/archive/libexif-{pkgver.replace('.', '_')}-release.tar.gz"
sha256 = "ee0795432c20d2fdb2a8a579dd6fc0e19d402e36f14f42c03ab60d2345950f09"


@subpackage("libexif-devel")
def _(self):
    return self.default_devel()
