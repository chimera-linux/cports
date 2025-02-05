pkgname = "gnome-weather"
pkgver = "47.0"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Weather"
source = (
    f"$(GNOME_SITE)/gnome-weather/{pkgver[:-2]}/gnome-weather-{pkgver}.tar.xz"
)
sha256 = "515f5862374dd346cbc85a9ddf0306b2d327657850bb60b6c9c9860fce9620e6"
