pkgname = "cinnamon-settings-daemon"
pkgver = "6.2.0"
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
sha256 = "ecb360017284cdf8a5776a64175ac69f730790d3031f1f4cabc5f8c52660a498"


@subpackage("cinnamon-settings-daemon-devel")
def _(self):
    return self.default_devel()
