pkgname = "xfce4-terminal"
pkgver = "1.1.3"
pkgrel = 1
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "intltool",
    "libtool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = ["exo-devel", "libxfce4ui-devel", "vte-gtk3-devel"]
pkgdesc = "Xfce terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-terminal/start"
source = f"$(XFCE_SITE)/apps/xfce4-terminal/{pkgver[:-2]}/xfce4-terminal-{pkgver}.tar.bz2"
sha256 = "214dd588d441b69f816009682a3bb4652cc19bed7ea64b612a12f097417b3d45"
