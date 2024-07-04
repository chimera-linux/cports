pkgname = "exo"
pkgver = "4.18.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gmake",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "python",
    "xfce4-dev-tools",
]
makedepends = ["glib-devel", "gtk+3-devel", "libxfce4ui-devel"]
pkgdesc = "Xfce extensions library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://docs.xfce.org/xfce/exo/start"
source = f"$(XFCE_SITE)/xfce/exo/{pkgver[:-2]}/exo-{pkgver}.tar.bz2"
sha256 = "4f2c61d045a888cdb64297fd0ae20cc23da9b97ffb82562ed12806ed21da7d55"


@subpackage("exo-devel")
def _devel(self):
    return self.default_devel()
