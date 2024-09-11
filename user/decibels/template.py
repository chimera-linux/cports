pkgname = "decibels"
pkgver = "46.0"
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
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/Incubator/decibels"
source = [
    f"{url}/-/archive/{pkgver}/decibels-{pkgver}.tar.gz",
    "https://gitlab.gnome.org/BrainBlasted/gi-typescript-definitions/-/archive/dbbaa0527556cd3ce5434c4a5072cd99348eff7a.tar.gz",
]
source_paths = [".", "gi-types"]
sha256 = [
    "ab43bc4f6a9fe697e3a78700d525c03b3fca124a9fb6fc5591239af00f07d31f",
    "6c625c8a01bd15e9f35fd6ea6823b5afb2288e6a40e34d852d37b6fa0fa51e57",
]
