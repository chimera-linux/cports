pkgname = "gnome-maps"
pkgver = "47.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "geoclue-devel",
    "geocode-glib-devel",
    "gjs-devel",
    "glib-devel",
    "gtk4-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libgweather-devel",
    "libportal-devel",
    "librsvg-devel",
    "libshumate-devel",
    "libxml2-devel",
    "rest-devel",
]
depends = [
    "gdk-pixbuf",
    "geoclue",
    "geocode-glib",
    "gjs",
    "graphene",
    "libadwaita",
    "libgweather",
    "libportal",
    "libsecret",
    "libshumate",
    "libsoup",
    "pango",
    "rest",
]
checkdepends = ["libsecret"]
pkgdesc = "GNOME maps"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND CC0-1.0"
url = "https://apps.gnome.org/Maps"
source = f"$(GNOME_SITE)/gnome-maps/{pkgver.split('.')[0]}/gnome-maps-{pkgver}.tar.xz"
sha256 = "5851e786daec658f21e457a206ff0a9ad1659f3741aad9490b1bf3192154fe9b"
options = ["!cross"]
