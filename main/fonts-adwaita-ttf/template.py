pkgname = "fonts-adwaita-ttf"
pkgver = "50.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Adwaita family of fonts"
license = "OFL-1.1"
url = "https://gitlab.gnome.org/GNOME/adwaita-fonts"
source = (
    f"$(GNOME_SITE)/adwaita-fonts/{pkgver[:-2]}/adwaita-fonts-{pkgver}.tar.xz"
)
sha256 = "4c927fbfeec1c503801ba510c2c94e0054c82c522cf7ba0d3be5d4d41fcf5c86"


def post_install(self):
    self.install_license("LICENSE")
