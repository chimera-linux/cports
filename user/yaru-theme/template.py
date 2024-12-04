pkgname = "yaru-theme"
pkgver = "24.10.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "bash",
    "sassc",
]
makedepends = ["gtk+3-devel"]
pkgdesc = "Default theme for Ubuntu"
maintainer = "metalparade <comer@live.cn>"
license = "GPL-3.0-or-later OR CC-BY-SA-4.0"
url = "https://github.com/ubuntu/yaru"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "80eed1a9832cf81976bf12b4cc85565b7d035176d1c3d73ccca7cacf1e4094a5"


@subpackage("yaru-theme-gnome-shell")
def _(self):
    self.subdesc = "GNOME Shell"
    return [
        "usr/share/gnome-shell",
        "usr/share/themes/*/index.theme",
        "usr/share/themes/*/gnome-shell",
    ]


@subpackage("yaru-theme-gtk")
def _(self):
    self.subdesc = "GTK"
    return [
        "usr/share/themes/*/gtk-2.0",
        "usr/share/themes/*/gtk-3.0",
        "usr/share/themes/*/gtk-4.0",
    ]


@subpackage("yaru-theme-gtksourceview")
def _(self):
    self.subdesc = "GTK sourceview files"
    return [
        "usr/share/gtksourceview-2.0",
        "usr/share/gtksourceview-3.0",
        "usr/share/gtksourceview-4",
        "usr/share/gtksourceview-5",
        "usr/share/libgedit-gtksourceview-300",
    ]


@subpackage("yaru-theme-icon")
def _(self):
    self.subdesc = "Icon theme"
    return ["usr/share/icons"]


@subpackage("yaru-theme-sound")
def _(self):
    self.subdesc = "Sound theme"
    return ["usr/share/sounds/Yaru"]
