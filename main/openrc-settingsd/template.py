pkgname = "openrc-settingsd"
pkgver = "1.5.0"
pkgrel = 4
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
sha256 = "f4a74262e0012783047ec1d12dfdf4ef3a983e9abaeb436e17703d6881f72292"


def post_install(self):
    self.install_service(self.files_path / "openrc-settingsd")
    self.install_tmpfiles(self.files_path / "openrc-settingsd.conf")
