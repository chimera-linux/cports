pkgname = "gnome-weather"
pkgver = "49.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
    "typescript",
]
makedepends = [
    "geoclue-devel",
    "gjs-devel",
    "gobject-introspection-devel",
    "libadwaita-devel",
    "libgweather-devel",
]
depends = ["geoclue", "gjs", "libadwaita", "libgweather"]
pkgdesc = "GNOME weather application"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Weather"
source = (
    f"$(GNOME_SITE)/gnome-weather/{pkgver[:-2]}/gnome-weather-{pkgver}.tar.xz"
)
sha256 = "ee1f76b85eba9db0c8d5c02041a9d85ecdd22abb5ec6bb3ff32225929c0fce5f"
