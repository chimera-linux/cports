pkgname = "fonts-adwaita-ttf"
pkgver = "48.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Adwaita family of fonts"
license = "OFL-1.1"
url = "https://gitlab.gnome.org/GNOME/adwaita-fonts"
source = (
    f"$(GNOME_SITE)/adwaita-fonts/{pkgver[:-2]}/adwaita-fonts-{pkgver}.tar.xz"
)
sha256 = "156f7e92f2f82e527fc73c309dbb237c0a4a5c3a95bc5ee94a5efb6947c553e0"


def post_install(self):
    self.install_license("LICENSE")
