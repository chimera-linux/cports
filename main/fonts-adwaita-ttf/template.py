pkgname = "fonts-adwaita-ttf"
pkgver = "51.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Adwaita family of fonts"
license = "OFL-1.1"
url = "https://gitlab.gnome.org/GNOME/adwaita-fonts"
source = (
    f"$(GNOME_SITE)/adwaita-fonts/{pkgver[:-2]}/adwaita-fonts-{pkgver}.tar.xz"
)
sha256 = "fa104ae2c1b96580d322f563ffe8b2dfca5296b0eca4971efd2d8011405123d2"


def post_install(self):
    self.install_license("LICENSE")
