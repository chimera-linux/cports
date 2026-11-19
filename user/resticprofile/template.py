pkgname = "resticprofile"
pkgver = "0.34.0"
pkgrel = 1
build_style = "go"
make_build_args = [
    "-tags",
    "no_self_update",
    f"-ldflags=-X main.version=v{pkgver}",
]
# make_build_args = [f"-ldflags=-X main.version=v{pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Configuration profiles manager for restic"
license = "GPL-3.0-only"
url = "https://creativeprojects.github.io/resticprofile"
source = f"https://github.com/creativeprojects/resticprofile/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "343b956215e3a9124d0ac3d94740668a905eb4b9210e9f50f91baec67144f693"
# fails due to lack of systemd
options = ["!check"]


def install(self):
    self.install_bin("build/resticprofile")


def post_install(self):
    self.install_license("LICENSE")
