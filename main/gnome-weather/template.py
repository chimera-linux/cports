pkgname = "gnome-weather"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "geoclue-devel",
    "gjs-devel",
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
sha256 = "4c0569b3d815ae2f9416d47134cbd3056340640ff186d31a94c865813b4bdbb5"
