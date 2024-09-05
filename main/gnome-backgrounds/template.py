pkgname = "gnome-backgrounds"
pkgver = "47_beta"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
pkgdesc = "Backgrounds for GNOME desktop"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-backgrounds"
source = f"$(GNOME_SITE)/gnome-backgrounds/{pkgver[:2]}/gnome-backgrounds-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "ac1421d30ee51b70d37f23590753ca9534c13c6dbdedbfe3dc9db870227a9736"


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
