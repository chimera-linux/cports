pkgname = "foot"
pkgver = "1.21.0"
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
provides = [self.with_pkgver("foot-themes")]
pkgdesc = "Wayland terminal emulator"
license = "MIT"
url = "https://codeberg.org/dnkl/foot"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "b93b196a3fbab86678c54be627557bdc7b1fc8042d99b14c4a74b149f60bcd52"
hardening = ["vis", "cfi"]


def post_install(self):
    self.rename(
        "usr/share/doc/foot/LICENSE",
        f"usr/share/licenses/{pkgname}/LICENSE",
        relative=False,
    )
    self.install_service(self.files_path / "foot.user")


@subpackage("foot-terminfo")
def _(self):
    self.subdesc = "extra terminfo data"

    return ["usr/share/terminfo"]
