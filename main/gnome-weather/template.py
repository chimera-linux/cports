pkgname = "gnome-weather"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
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
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "153826705ccf672e14f2fe4dfc782f8e89b7c4cbe4aafe95a5532fbde7a3d49d"
options = ["!cross"]
