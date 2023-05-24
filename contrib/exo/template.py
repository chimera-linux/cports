pkgname = "exo"
pkgver = "4.18.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
hostmakedepends = [
    "pkgconf",
    "gmake",
    "intltool",
    "gettext-tiny",
    "glib-devel",
    "python",
]
makedepends = ["glib-devel", "libxfce4ui-devel", "gtk+3-devel"]
depends = ["hicolor-icon-theme", "desktop-file-utils"]
pkgdesc = "Xfce extensions library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://xfce.org"
source = f"https://archive.xfce.org/src/xfce/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "4f2c61d045a888cdb64297fd0ae20cc23da9b97ffb82562ed12806ed21da7d55"


@subpackage("exo-devel")
def _dev(self):
    return self.default_devel()


configure_gen = []
