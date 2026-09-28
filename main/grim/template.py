pkgname = "grim"
pkgver = "1.5.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dfish-completions=true",
    "-Dbash-completions=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
    "wayland-progs",
]
makedepends = [
    "bash-completion",
    "cairo-devel",
    "libjpeg-turbo-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Grab images from a wayland compositor"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/grim"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "17771517611c5ce1c56e6c0ce4e860ec27052273ca51f010672dbfac7d540f1f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.rename("usr/share/bash-completion/completions/grim.bash", "grim")
