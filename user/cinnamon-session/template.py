pkgname = "cinnamon-session"
pkgver = "6.4.0"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = ["--libexecdir=/usr/lib"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "cinnamon-desktop-devel",
    "elogind-devel",
    "glib-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libice-devel",
    "libsm-devel",
    "libx11-devel",
    "libxau-devel",
    "libxcomposite-devel",
    "libxext-devel",
    "libxrender-devel",
    "libxtst-devel",
    "mesa-devel",
    "pango-devel",
    "xapp-devel",
    "xtrans",
]
depends = ["gtk+3", "python-gobject", "python-setproctitle", "xapp"]
pkgdesc = "Cinnamon session manager"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cinnamon-session/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "464075d920df360b5ad94f72395a09b5fbf8b14f0190406ec76055a17659e243"
hardening = ["vis"]
