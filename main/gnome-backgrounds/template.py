pkgname = "gnome-backgrounds"
pkgver = "51.0.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
pkgdesc = "Backgrounds for GNOME desktop"
license = "GPL-2.0-or-later AND CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-backgrounds"
source = f"$(GNOME_SITE)/gnome-backgrounds/{pkgver[: pkgver.find('.')]}/gnome-backgrounds-{pkgver}.tar.xz"
sha256 = "ec50534d7749be0e1503c5504f826c61d1460d2b41cb84518fa6b2f5547d1e1e"


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
