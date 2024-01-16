pkgname = "file-roller"
pkgver = "44_alpha"
pkgrel = 0
build_style = "meson"
_commit = "49405db32edd55606d7f19056e425b7c9293119a"
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
source = (
    f"https://gitlab.gnome.org/GNOME/file-roller/-/archive/{_commit}.tar.gz"
)
sha256 = "4a71ea19c268f95ec561c100945d7ac4ccc92bdae097fd4c6defcb4088f54d3f"
