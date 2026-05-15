pkgname = "gnome-backgrounds"
pkgver = "50.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
pkgdesc = "Backgrounds for GNOME desktop"
license = "GPL-2.0-or-later AND CC-BY-2.0 AND CC-BY-SA-2.0 AND CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-backgrounds"
source = f"$(GNOME_SITE)/gnome-backgrounds/{pkgver[: pkgver.find('.')]}/gnome-backgrounds-{pkgver}.tar.xz"
sha256 = "1acdba7acb4f34c7321febc6273444344fd55fd593611d446de70860183b52b8"


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
