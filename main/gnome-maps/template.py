pkgname = "gnome-maps"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "gettext",
    "desktop-file-utils",
]
makedepends = [
    "glib-devel",
    "gjs-devel",
    "gtk4-devel",
    "geoclue-devel",
    "libadwaita-devel",
    "libgweather-devel",
    "geocode-glib-devel",
    "libportal-devel",
    "libshumate-devel",
    "libxml2-devel",
    "rest-devel",
    "librsvg-devel",
    "json-glib-devel",
]
checkdepends = ["libsecret"]
pkgdesc = "GNOME maps"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/Maps"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e70979b56075b9a3051f375ea7080ea481e7bd5229e6d8228f8de961cae2a9ae"
