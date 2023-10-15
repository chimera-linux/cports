pkgname = "brightnessctl"
pkgver = "0.5.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["UDEVDIR=/usr/lib/udev/rules.d"]
make_use_env = True
hostmakedepends = ["gmake"]
pkgdesc = "Program to read and control device brightness"
maintainer = "Froggo <froggo8311@proton.me>"
license = "X11"
url = "https://github.com/Hummer12007/brightnessctl"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a68869e23f56ac4f2e28f1783002810ddbf10f95e1af9b48b2912fb169f46994"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
