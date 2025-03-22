pkgname = "gnome-backgrounds"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
pkgdesc = "Backgrounds for GNOME desktop"
license = "GPL-2.0-or-later AND CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-backgrounds"
source = f"$(GNOME_SITE)/gnome-backgrounds/{pkgver[:-2]}/gnome-backgrounds-{pkgver}.tar.xz"
sha256 = "2d6baa011ee97804c7561f7e1cbd8d4763e30b55b8818dda78f9f75afb8d8d05"


@subpackage("gnome-backgrounds-gnome")
def _(self):
    self.subdesc = "GNOME integration"
    self.depends += [
        self.parent,
        "gdk-pixbuf",
        "libjxl",
        "librsvg",
    ]
    self.options = ["empty"]

    return []
