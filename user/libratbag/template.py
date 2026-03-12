pkgname = "libratbag"
pkgver = "0.18"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd=false",
    "-Dlogind-provider=elogind",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "swig",
]
makedepends = [
    "check-devel",
    "dinit-chimera",
    "dinit-dbus",
    "elogind-devel",
    "glib-devel",
    "json-glib-devel",
    "libevdev-devel",
    "libunistring-devel",
    "python-devel",
    "tangle-devel",
    "udev-devel",
]
depends = [
    "python-evdev",
    "python-gobject",
]
checkdepends = [*depends]
pkgdesc = "Configuration daemon for input devices"
license = "MIT"
url = "https://github.com/libratbag/libratbag"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8a7f8bf00c21ef5ad534e2804ed537f2fc6521a3932dd822c438e561a85a1bcd"


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "ratbagd")


@subpackage("libratbag-devel")
def _(self):
    return self.default_devel()
