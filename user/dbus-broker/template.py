pkgname = "dbus-broker"
pkgver = "33"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlauncher=false",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Linux D-Bus message broker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/bus1/dbus-broker/wiki"
source = f"https://github.com/bus1/dbus-broker/releases/download/v{pkgver}/dbus-broker-{pkgver}.tar.xz"
sha256 = "23713f25624749fdb274907e429080fa2d8f4dbe76acd87bb6d21a3c818c7841"
hardening = ["vis", "cfi"]
restricted = "no dinit controller"
