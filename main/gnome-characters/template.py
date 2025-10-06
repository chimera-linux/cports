pkgname = "gnome-characters"
pkgver = "49.0"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "gjs-devel",
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libunistring-devel",
]
checkdepends = ["fonts-dejavu", "xwayland-run"]
depends = ["gjs", "gnome-desktop", "libadwaita"]
pkgdesc = "GNOME character map utility"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Design/Apps/CharacterMap"
source = f"$(GNOME_SITE)/gnome-characters/{pkgver[:-2]}/gnome-characters-{pkgver}.tar.xz"
sha256 = "1b6e548a82e26aa4ec9afe409d69a25709362c037fa5c533186d6a1db29af6e3"
# tries to access gpu
options = ["!check"]
