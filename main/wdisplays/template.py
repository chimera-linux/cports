pkgname = "wdisplays"
pkgver = "1.1.3"
pkgrel = 0
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
license = "GPL-3.0-or-later"
url = "https://github.com/artizirk/wdisplays"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "6b8674598d50cb56a3acb79bd563c1d7a7d7781a8ce8dcc83a240916024b7070"
