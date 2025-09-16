pkgname = "openrc-settingsd"
pkgver = "1.5.0"
pkgrel = 5
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dopenrc=disabled",
    "-Denv-update=",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "glib-devel",
    "linux-headers",
    "polkit-devel",
]
depends = ["dinit-dbus", "polkit"]
pkgdesc = "Implementation of hostnamed, localed, and timedated"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/postmarketOS/openrc-settingsd"
source = f"{url}/-/archive/v{pkgver}/openrc-settingsd-v{pkgver}.tar.gz"
sha256 = "f4a74262e0012783047ec1d12dfdf4ef3a983e9abaeb436e17703d6881f72292"


def post_install(self):
    self.install_service(self.files_path / "openrc-settingsd")
    self.install_tmpfiles(self.files_path / "openrc-settingsd.conf")
