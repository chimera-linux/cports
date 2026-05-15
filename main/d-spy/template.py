pkgname = "d-spy"
pkgver = "50.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext-devel",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "libdex-devel",
]
pkgdesc = "D-Bus inspector and debugger"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/d-spy"
source = f"{url}/-/archive/{pkgver}/d-spy-{pkgver}.tar.gz"
sha256 = "0407ecd00b123a16ed6ffc26635a8b3362846ab9b756ed56d16cffc11787867a"
hardening = ["vis", "!cfi"]
