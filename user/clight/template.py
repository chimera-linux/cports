pkgname = "clight"
pkgver = "4.11"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "dbus-devel",
    "elogind-devel",
    "gsl-devel",
    "libconfig-devel",
    "libmodule-devel",
    "linux-headers",
    "ninja",
    "pkgconf",
    "popt-devel",
]
makedepends = [
    "bash-completion",
    "fish-shell",
]
depends = [
    "clightd",
]
install_if = [
    "clightd>=5",
]
pkgdesc = "User daemon to adjust screen backlight based on ambient brightness"
maintainer = "Anthony <w732qq@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/FedeDP/Clight"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9a7ec2070b0e1d074477cd219d6894dde9eb85cbe83daebc22054fab29dade34"


def post_install(self):
    self.install_service(self.files_path / "clight.user")
