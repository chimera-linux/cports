pkgname = "gnome-shell-extension-appindicator"
pkgver = "58"
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
sha256 = "7a6fda28ddd214fbb832486b85c73447ff0c5fc7a36c6d1510c4ff6801cff9d8"
