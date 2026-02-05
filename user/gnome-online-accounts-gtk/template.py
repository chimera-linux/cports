pkgname = "gnome-online-accounts-gtk"
pkgver = "3.50.10"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gnome-online-accounts-devel",
    "gtk4-devel",
]
pkgdesc = "GTK frontend for GNOME Online Accounts"
license = "GPL-3.0-or-later"
url = "https://github.com/xapp-project/gnome-online-accounts-gtk"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1335240713781c7f88d3d0a179cd275d309fd010cbd9d9048518560a75d774ac"
hardening = ["vis", "cfi"]
