pkgname = "flatpak-builder"
pkgver = "1.4.7"
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
sha256 = "fd5bc36fe3b974395f782e6c920d8955cee168f513370c32cc800b69acd980d0"
# CFI: fails on builder_(context|cache)_finalize during "flatpak-builder build ..."
hardening = ["vis", "!cfi"]
