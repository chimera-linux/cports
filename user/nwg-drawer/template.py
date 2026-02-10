pkgname = "nwg-drawer"
pkgver = "0.7.4"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go", "pkgconf"]
makedepends = ["xdg-utils", "gtk+3-devel", "gtk-layer-shell-devel", "gobject-introspection-devel"]
pkgdesc = "Application drawer for wlroots-based Wayland compositors"
license = "MIT AND MPL-2.0"
url = "https://nwg-piotr.github.io/nwg-shell/nwg-drawer"
source = (
    f"https://github.com/nwg-piotr/nwg-drawer/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "0caa9f3a5efbd7492ce57fc6952e7f78e2d6ee71d4a430aeb0aa7535abecdab5"
env = {"CGO_ENABLED": "1"}


def post_install(self):
    self.install_license("LICENSE")
    self.install_files("desktop-directories", "usr/share/nwg-drawer")
    self.install_files("img", "usr/share/nwg-drawer")
    self.install_files("drawer.css", "usr/share/nwg-drawer")
