pkgname = "mate-polkit"
pkgver = "1.28.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "polkit-devel",
]
pkgdesc = "Polkit integration for the MATE desktop"
maintainer = "natthias <natthias@proton.me>"
license = "LGPL-2.0-or-later"
url = "https://mate-desktop.org"
source = f"https://github.com/mate-desktop/mate-polkit/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b7dd0999f1570e41939997f075ddbf459650c6572dd89a63b3a1963d60427001"
