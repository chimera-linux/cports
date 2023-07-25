pkgname = "xfce4-terminal"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "intltool"]
makedepends = ["exo-devel", "libxfce4ui-devel", "vte-gtk3-devel"]
depends = [
    "desktop-file-utils",
    "gsettings-desktop-schemas",
]
pkgdesc = "Xfce terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://xfce.org"
source = f"https://archive.xfce.org/src/apps/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "78e55957af7c6fc1f283e90be33988661593a4da98383da1b0b54fdf6554baf4"

configure_gen = []
