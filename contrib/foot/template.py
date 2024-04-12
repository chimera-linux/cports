pkgname = "foot"
pkgver = "1.17.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dterminfo-base-name=foot-extra"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "fcft-devel",
    "fontconfig-devel",
    "freetype-devel",
    "libinput-devel",
    "libxkbcommon-devel",
    "ncurses-devel",
    "pixman-devel",
    "tllist",
    "utf8proc-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Fast, lightweight and minimalistic Wayland terminal emulator"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://codeberg.org/dnkl/foot"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "da49d302fb98d61e674dace27d44ab6e6e6446a1ee156a09a430efb738d74b39"
hardening = ["vis", "cfi"]


def post_install(self):
    ded = self.destdir
    self.install_dir(f"usr/share/licenses/{pkgname}")
    self.mv(
        ded / "usr/share/doc/foot/LICENSE",
        ded / f"usr/share/licenses/{pkgname}/LICENSE",
    )


@subpackage("foot-terminfo")
def _tinfo(self):
    self.pkgdesc = f"{pkgdesc} (extra terminfo data)"

    return ["usr/share/terminfo"]


@subpackage("foot-themes")
def _themes(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.pkgdesc = f"{pkgdesc} (colour themes)"

    return ["usr/share/foot/themes"]
