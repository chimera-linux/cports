pkgname = "hikari"
pkgver = "2.3.3"
pkgrel = 0
build_style = "makefile"
make_build_args = ["WITH_ALL=1", f"VERSION={pkgver}"]
make_install_args = ["ETC_PREFIX=/"]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = [
    "cairo-devel",
    "libinput-devel",
    "libucl-devel",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "pango-devel",
    "pixman-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.15-devel",
    "xwayland-devel",
]
pkgdesc = "Stacking wayland compositor"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://hikari.acmelabs.space"
source = f"https://hikari.acmelabs.space/releases/hikari-{pkgver}.tar.gz"
sha256 = "40736ff326e11a51128c1739051a692ad2c79173fc4b695c8be5ec7a614b4de2"
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    # remove suid
    (self.destdir / "usr/bin/hikari-unlocker").chmod(0o755)
