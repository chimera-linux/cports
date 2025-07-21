pkgname = "gnome-firmware"
pkgver = "47.0"
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
sha256 = "b39534a0aab3c0d8b8c27152af7a02b7f7c8082d87b9d5cf8ebdd9b520f03bb3"
options = ["!cross"]
