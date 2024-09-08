pkgname = "telepathy-idle"
pkgver = "0.2.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf", "xsltproc"]
makedepends = [
    "dbus-glib-devel",
    "telepathy-glib-devel",
]
checkdepends = ["dbus", "python-dbus"]
pkgdesc = "IRC connection manager for the Telepathy framework"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "LGPL-2.1-or-later"
url = "https://telepathy.freedesktop.org"
source = f"{url}/releases/telepathy-idle/telepathy-idle-{pkgver}.tar.gz"
sha256 = "8387e25e5fb0b4cbe701e5dc092d666d6510b833fd3e7e462e9170d36ec3c15f"
