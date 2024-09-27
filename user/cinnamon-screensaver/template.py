pkgname = "cinnamon-screensaver"
pkgver = "6.4.0"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = ["--libexecdir=/usr/lib", "-Dpam-prefix=/usr/lib"]
hostmakedepends = ["gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "dbus-devel",
    "glib-devel",
    "gtk+3-devel",
    "libx11-devel",
    "libxext-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "linux-pam-devel",
    "xdotool-devel",
]
depends = [
    "cinnamon-desktop",
    "cinnamon-schemas",
    "gtk+3",
    "python-cairo",
    "python-gobject",
    "python-setproctitle",
    "python-xapp",
    "xapp",
]
pkgdesc = "Cinnamon screen locker and screensaver program"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-screensaver/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e985b68981482b7ead6aef55988937958539221d752f9a4feb7ced9ac32fe422"
options = ["!cross"]


@subpackage("cinnamon-screensaver-devel")
def _(self):
    return self.default_devel()


@subpackage("cinnamon-screensaver-static")
def _(self):
    return ["usr/lib/cinnamon-screensaver/*.a"]
