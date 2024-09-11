pkgname = "lxlauncher"
pkgver = "0.2.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-gtk3"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "pkgconf",
]
makedepends = ["gtk+3-devel", "startup-notification-devel", "menu-cache"]
pkgdesc = "Open source clone of the Asus launcher for EeePC"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/lxlauncher"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "06568a4f262cd974554c373a538091b55759df3e911b134c9ed012ff75c29fd9"
# no tests
options = ["!check"]
