pkgname = "lxterminal"
pkgver = "0.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-gtk3"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "pkgconf",
]
makedepends = [
    "vte-gtk3-devel",
    "glib-devel",
    "libx11-devel",
    "pango-devel",
]
pkgdesc = "Lightweight vte-based tabbed terminal emulator for LXDE"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/lxterminal"
source = f"https://downloads.sourceforge.net/lxde/lxterminal-{pkgver}.tar.xz"
sha256 = "9db8748923b3fa09a82ae2210ed1fa4cdb4c45312009da9caed103d48f8e9be7"
