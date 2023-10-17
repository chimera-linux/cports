pkgname = "foot"
pkgver = "1.16.2"
pkgrel = 0
build_style = "meson"
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
depends = [f"foot-terminfo={pkgver}-r{pkgrel}"]
pkgdesc = "Fast, lightweight and minimalistic Wayland terminal emulator"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://codeberg.org/dnkl/foot"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "0e02af376e5f4a96eeb90470b7ad2e79a1d660db2a7d1aa772be43c7db00e475"
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
    self.pkgdesc = f"{pkgdesc} (terminfo data)"

    return ["usr/share/terminfo"]


@subpackage("foot-themes")
def _themes(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.pkgdesc = f"{pkgdesc} (colour themes)"

    return ["usr/share/foot/themes"]
