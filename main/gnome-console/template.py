pkgname = "gnome-console"
pkgver = "49.1"
pkgrel = 0
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
sha256 = "fca39fd041e05ee7ca6d2a5c82001937d02ae1513f3f3651bd37ae0e2ef66e3e"
# tries to open gpu
options = ["!check"]
