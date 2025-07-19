pkgname = "foot"
pkgver = "1.23.0"
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
sha256 = "74c874feb5ae0277a9f19fbd6418a40524cd71d629784276d109ebfe4e786421"
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
