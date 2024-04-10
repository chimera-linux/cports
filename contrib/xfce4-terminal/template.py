pkgname = "xfce4-terminal"
pkgver = "1.1.3"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "intltool"]
makedepends = ["exo-devel", "libxfce4ui-devel", "vte-gtk3-devel"]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "Xfce terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://xfce.org"
source = f"https://archive.xfce.org/src/apps/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "214dd588d441b69f816009682a3bb4652cc19bed7ea64b612a12f097417b3d45"

configure_gen = []
