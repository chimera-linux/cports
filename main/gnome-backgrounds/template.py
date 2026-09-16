pkgname = "gnome-backgrounds"
pkgver = "51.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
pkgdesc = "Backgrounds for GNOME desktop"
license = "GPL-2.0-or-later AND CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-backgrounds"
source = f"$(GNOME_SITE)/gnome-backgrounds/{pkgver[: pkgver.find('.')]}/gnome-backgrounds-{pkgver}.tar.xz"
sha256 = "5811d24118d78f41b66c616efb1094c20507cb546e484dca4963fe738a4ba7db"


@subpackage("gnome-backgrounds-gnome")
def _(self):
    self.subdesc = "GNOME integration"
    self.depends += [
        self.parent,
        "gdk-pixbuf",
        "glycin-loaders",
    ]
    self.options = ["empty"]

    return []
