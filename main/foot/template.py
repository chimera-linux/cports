pkgname = "foot"
pkgver = "1.27.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dterminfo-base-name=foot-extra"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "dinit-chimera",
    "fcft-devel",
    "fontconfig-devel",
    "freetype-devel",
    "libinput-devel",
    "libxkbcommon-devel",
    "ncurses-devel",
    "pixman-devel",
    "tllist",
    "turnstile",
    "utf8proc-devel",
    "wayland-devel",
    "wayland-protocols",
]
provides = [self.with_pkgver("foot-themes")]
pkgdesc = "Wayland terminal emulator"
license = "MIT"
url = "https://codeberg.org/dnkl/foot"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "4e6131cc859ec6a36569f1978cf3617cc3836a681d13d228ded1b4885dab7770"
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
