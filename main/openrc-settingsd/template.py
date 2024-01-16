pkgname = "openrc-settingsd"
pkgver = "1.4.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dopenrc=disabled", "-Denv-update="]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "dbus-devel",
    "glib-devel",
    "linux-headers",
    "polkit-devel",
]
depends = ["dbus", "polkit"]
pkgdesc = "Implementation of hostnamed, localed, and timedated"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/postmarketOS/openrc-settingsd"
source = f"{url}/-/archive/v{pkgver}/openrc-settingsd-v{pkgver}.tar.gz"
sha256 = "9d09e02de0faf15ee9a6a742586cf9b1a314591ec50f84e2513636ecfe4f2ff3"


def post_install(self):
    self.install_service(self.files_path / "openrc-settingsd")
    self.install_file(
        self.files_path / "openrc-settingsd.conf", "usr/lib/tmpfiles.d"
    )
