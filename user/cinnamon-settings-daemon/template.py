pkgname = "cinnamon-settings-daemon"
pkgver = "6.4.0"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = ["--libexecdir=/usr/lib", "-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "cinnamon-desktop-devel",
    "colord-devel",
    "cups-devel",
    "elogind-devel",
    "fontconfig-devel",
    "glib-devel",
    "gtk+3-devel",
    "lcms2-devel",
    "libcanberra-devel",
    "libgnomekbd-devel",
    "libgudev-devel",
    "libnotify-devel",
    "libpulse-devel",
    "librsvg-devel",
    "libwacom-devel",
    "libx11-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxi-devel",
    "libxklavier-devel",
    "nss-devel",
    "pango-devel",
    "polkit-devel",
    "upower-devel",
    "xorgproto",
]
pkgdesc = "Settings daemon for the Cinnamon desktop"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-settings-daemon/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cb4311632849cfceca1ea9b6fbb19478559137cb544d866184f4316dfae86a57"


@subpackage("cinnamon-settings-daemon-devel")
def _(self):
    return self.default_devel()
