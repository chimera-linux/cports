pkgname = "gweather-locations"
pkgver = "2026.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
    "python-gobject",
]
pkgdesc = "GNOME Weather locations database"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gweather-locations"
source = f"$(GNOME_SITE)/gweather-locations/{pkgver[:-2]}/gweather-locations-{pkgver}.tar.xz"
sha256 = "e7570a3661e0a752a06387b2032585cf588fc56770b1f9f39f1a55d17b2835fe"


@subpackage("gweather-locations-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
