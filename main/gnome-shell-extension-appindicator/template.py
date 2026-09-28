pkgname = "gnome-shell-extension-appindicator"
pkgver = "66"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "jq",
    "meson",
]
depends = ["gnome-shell"]
pkgdesc = "AppIndicator/KStatusNotifierItem support for GNOME"
license = "GPL-2.0-or-later"
url = "https://github.com/ubuntu/gnome-shell-extension-appindicator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3f692824e54c2192d984a24e1685722d1c88787e24dba662aecabe0b7f9e2bbc"
