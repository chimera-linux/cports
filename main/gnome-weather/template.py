pkgname = "gnome-weather"
pkgver = "47_alpha"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
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
source = f"$(GNOME_SITE)/gnome-weather/{pkgver[:2]}/gnome-weather-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "f829c8e098fba799da0fa09a49e1f0bff8dfc2b63f9d4ecb8657f4e5632db5da"
