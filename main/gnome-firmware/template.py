pkgname = "gnome-firmware"
pkgver = "49.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Delogind=true", "-Dconsolekit=false", "-Dsystemd=false"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "help2man",
    "meson",
    "pkgconf",
]
makedepends = [
    "elogind-devel",
    "fwupd-devel",
    "libadwaita-devel",
    "libxmlb-devel",
]
pkgdesc = "GNOME firmware updater"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/World/gnome-firmware"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "19d443e1639245bcfa7fe0fb9dd86ceb32d8d354c4e1b4c8ffebbaa9b7133c85"
options = ["!cross"]
