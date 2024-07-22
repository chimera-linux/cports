pkgname = "rtkit"
pkgver = "0.13"
pkgrel = 4
build_style = "meson"
configure_args = [
    "-Dlibsystemd=disabled",
    "-Dinstalled_tests=false",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "dbus-devel",
    "libcap-devel",
    "polkit-devel",
    "zlib-ng-compat-devel",
]
depends = ["polkit"]
pkgdesc = "Realtime policy and watchdog daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND GPL-3.0-or-later"
url = "https://github.com/heftig/rtkit"
source = f"{url}/releases/download/v{pkgver}/rtkit-{pkgver}.tar.xz"
sha256 = "a157144cd95cf6d25200e74b74a8f01e4fe51fd421bb63c1f00d471394b640ab"
hardening = ["vis", "cfi"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_license("LICENSE")
    self.install_service(self.files_path / "rtkit")
    self.install_sysusers(self.files_path / "sysusers.conf")
    # optional
    self.install_file(
        self.files_path / "50-rtkit.rules", "usr/share/polkit-1/rules.d"
    )
