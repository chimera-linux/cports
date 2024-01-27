pkgname = "bemenu"
pkgver = "0.6.20"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "scdoc"
]
makedepends = [
    "cairo-devel",
    "libxkbcommon-devel",
    "libxinerama-devel",
    "linux-headers",
    "ncurses-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols"
]
pkgdesc = "Dynamic menu library and client program inspired by dmenu"
maintainer = "Rupus Reinefjord <rupus@reinefjord.net>"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://github.com/Cloudef/bemenu"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "abd8ec1f496d2ca7df1f1afe13cb44143279ba761e130bc4324d6fdb23753bba"
hardening = ["vis", "cfi-genptr"]
# no tests
options = ["!check"]
