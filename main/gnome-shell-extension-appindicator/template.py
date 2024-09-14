pkgname = "gnome-shell-extension-appindicator"
pkgver = "59"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "jq",
    "meson",
]
depends = ["gnome-shell"]
pkgdesc = "AppIndicator/KStatusNotifierItem support for GNOME"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://github.com/ubuntu/gnome-shell-extension-appindicator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "37d8fb1bf800bbcb6b302fcc599758b36c23b8d166922262d004660b1e521b93"
