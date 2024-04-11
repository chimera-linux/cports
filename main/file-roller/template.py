pkgname = "file-roller"
pkgver = "44.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext",
    "glib-devel",
    "desktop-file-utils",
    "itstool",
    "gtk-update-icon-cache",
]
makedepends = [
    "gtk4-devel",
    "glib-devel",
    "libarchive-devel",
    "libnotify-devel",
    "nautilus-devel",
    "libadwaita-devel",
    "libportal-devel",
    "json-glib-devel",
]
pkgdesc = "GNOME archiver frontend"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/FileRoller"
source = f"https://gitlab.gnome.org/GNOME/file-roller/-/archive/{pkgver}/file-roller-{pkgver}.tar.gz"
sha256 = "70f53c6994d961b981f077377a2076461c0973eaee1c51d194d937f1ded85443"
