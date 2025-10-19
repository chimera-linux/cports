pkgname = "gnome-console"
pkgver = "49.0"
pkgrel = 2
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libgtop-devel",
    "pcre2-devel",
    "vte-gtk4-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "GNOME console"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/console"
source = (
    f"$(GNOME_SITE)/gnome-console/{pkgver[:-2]}/gnome-console-{pkgver}.tar.xz"
)
sha256 = "9e8e9646f473d01f4b4a7bce2c47ad226b4ae83fabf24cbbb4ac94f6ac5d5cc2"
# tries to open gpu
options = ["!check"]
