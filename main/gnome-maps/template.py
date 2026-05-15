pkgname = "gnome-maps"
pkgver = "50.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
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
    "librest-devel",
    "librsvg-devel",
    "libshumate-devel",
    "libxml2-devel",
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
    "librest",
    "libsecret",
    "libshumate",
    "libsoup",
    "pango",
]
checkdepends = ["libsecret"]
pkgdesc = "GNOME maps"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND CC0-1.0"
url = "https://apps.gnome.org/Maps"
source = f"$(GNOME_SITE)/gnome-maps/{pkgver.split('.')[0]}/gnome-maps-{pkgver}.tar.xz"
sha256 = "42cdf0367f945ce3db1203a6bcfd1d5f5f36d9cac361c81c18567b93130de9eb"
options = ["!cross"]
