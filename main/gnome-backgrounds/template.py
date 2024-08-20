pkgname = "gnome-backgrounds"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
pkgdesc = "Backgrounds for GNOME desktop"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-backgrounds"
source = f"$(GNOME_SITE)/gnome-backgrounds/{pkgver[:-2]}/gnome-backgrounds-{pkgver}.tar.xz"
sha256 = "4ddd3ac439a4a067876805921bb75f4d3c8b85a218d47c276dddde8928443c2e"


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
