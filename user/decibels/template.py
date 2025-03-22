pkgname = "decibels"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "desktop-file-utils",
    "gettext",
    "libxml2-progs",
    "meson",
    "pkgconf",
    "typescript",
]
makedepends = ["gjs-devel"]
depends = ["gjs", "libadwaita", "gst-plugins-base"]
pkgdesc = "GNOME audio player"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/Incubator/decibels"
source = [
    f"{url}/-/archive/{pkgver}/decibels-{pkgver}.tar.gz",
    "https://gitlab.gnome.org/BrainBlasted/gi-typescript-definitions/-/archive/dbbaa0527556cd3ce5434c4a5072cd99348eff7a.tar.gz",
]
source_paths = [".", "gi-types"]
sha256 = [
    "1ffe2c4ab2502314c74f017f2b58b9d110548a9cbc237096e6712e67c03b2e10",
    "6c625c8a01bd15e9f35fd6ea6823b5afb2288e6a40e34d852d37b6fa0fa51e57",
]
