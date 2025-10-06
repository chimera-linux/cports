pkgname = "fonts-adwaita-ttf"
pkgver = "49.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Adwaita family of fonts"
license = "OFL-1.1"
url = "https://gitlab.gnome.org/GNOME/adwaita-fonts"
source = (
    f"$(GNOME_SITE)/adwaita-fonts/{pkgver[:-2]}/adwaita-fonts-{pkgver}.tar.xz"
)
sha256 = "3157c620eb5b72b25ab156d194aa4eb223f9870d547fe83fdbdf06d3e7becb37"


def post_install(self):
    self.install_license("LICENSE")
