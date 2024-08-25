pkgname = "wdisplays"
pkgver = "1.1.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "glib-devel",
    "meson",
    "pkgconf",
    "python-scour",
    "wayland-progs",
]
makedepends = [
    "gtk+3-devel",
    "libepoxy-devel",
    "wayland-protocols",
]
# dependency of wcm=0.8.0-r1, provides same file as 0.8.0-r0
replaces = ["wcm<0.8.0-r1"]
pkgdesc = "GUI display configuration tool for wlroots compositors"
maintainer = "dhruv22592 <dhruv22592@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/artizirk/wdisplays"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "2df2c56db494c8450b1c7746b0ed2af11bf637fe2838f7412146fcc5cc1a2605"
