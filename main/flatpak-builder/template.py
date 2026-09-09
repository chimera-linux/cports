pkgname = "flatpak-builder"
pkgver = "1.4.11"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "appstream",
    "debugedit",
    "docbook-xsl",
    "meson",
    "pkgconf",
    "xmlto",
]
makedepends = [
    "curl-devel",
    "elfutils-devel",
    "flatpak-devel",
    "json-glib-devel",
    "libxml2-devel",
    "libyaml-devel",
    "linux-headers",
]
checkdepends = ["bash"]
depends = [
    "cmd:patch!chimerautils-extra",
    "debugedit",
    "elfutils",
    "flatpak",
    "git",
    "llvm-binutils",
]
pkgdesc = "Tool to build flatpaks from source"
license = "LGPL-2.1-or-later"
url = "https://docs.flatpak.org"
source = f"https://github.com/flatpak/flatpak-builder/releases/download/{pkgver}/flatpak-builder-{pkgver}.tar.xz"
sha256 = "2a5ef4f3eaea86f808aa477e57e65b6f68978eb1c034fafe05bffdebbf1dcd03"
# CFI: fails on builder_(context|cache)_finalize during "flatpak-builder build ..."
hardening = ["vis", "!cfi"]
