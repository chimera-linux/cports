pkgname = "irssi"
pkgver = "1.4.5"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "openssl3-devel",
    "perl",
    "ncurses-devel",
    "glib-devel",
]

pkgdesc = "Modular TUI IRC client with IPv6 support"
license = "GPL-2.0-or-later"
url = "https://irssi.org"
source = f"https://github.com/irssi/irssi/releases/download/{pkgver}/irssi-{pkgver}.tar.gz"
sha256 = "31653e8e0c5b1ef9b89905c330a0d77fe3f0592f88d163e504c1923dcd28ac47"
