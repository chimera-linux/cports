pkgname = "gnome-shell-extension-appindicator"
pkgver = "57"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "glib",
    "jq",
    "meson",
]
pkgdesc = "AppIndicator/KStatusNotifierItem support for GNOME"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://github.com/ubuntu/gnome-shell-extension-appindicator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "788fa3ff2f8525efbd794bffd0fcec3d77c9c1cbfcff0fadeb93b4925751ca41"
