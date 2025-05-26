pkgname = "gnome-backgrounds"
pkgver = "48.2.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
pkgdesc = "Backgrounds for GNOME desktop"
license = "GPL-2.0-or-later AND CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-backgrounds"
source = f"$(GNOME_SITE)/gnome-backgrounds/{pkgver[: pkgver.find('.')]}/gnome-backgrounds-{pkgver}.tar.xz"
sha256 = "6a1c5b7b2e0d8f5ce977926d55f9c2d65dd180822cdea5e59150dcfb5abd1ed9"


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
