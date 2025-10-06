pkgname = "gnome-backgrounds"
pkgver = "49.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
pkgdesc = "Backgrounds for GNOME desktop"
license = "GPL-2.0-or-later AND CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-backgrounds"
source = f"$(GNOME_SITE)/gnome-backgrounds/{pkgver[: pkgver.find('.')]}/gnome-backgrounds-{pkgver}.tar.xz"
sha256 = "01fe260de58ba00e44aba589a998e33e8bc7aecc701df0bee64cf4cfba44f4b5"


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
