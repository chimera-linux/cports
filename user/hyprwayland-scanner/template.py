pkgname = "hyprwayland-scanner"
pkgver = "0.4.6"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "pugixml-devel",
]
pkgdesc = "Hyprland implementation of wayland-scanner for C++"
license = "BSD-3-Clause"
url = "https://github.com/hyprwm/hyprwayland-scanner"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "05f55fd1a20d8ca81b5030980fdb7c87147749230145bdb3745af2741d617f5c"

options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
