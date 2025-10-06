pkgname = "gnome-shell-extension-appindicator"
pkgver = "61"
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
sha256 = "48555dd9c9437f835c9b01238f69a8643d2b17dffd7dbb8e23ccf2e97bb4d8de"
