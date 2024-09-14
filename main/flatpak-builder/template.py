pkgname = "flatpak-builder"
pkgver = "1.4.4"
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
    "elfutils-devel",
    "flatpak-devel",
    "json-glib-devel",
    "libcurl-devel",
    "libxml2-devel",
    "libyaml-devel",
    "linux-headers",
]
checkdepends = ["bash"]
depends = [
    "debugedit",
    "elfutils",
    "flatpak",
    "git",
    "llvm-binutils",
    "cmd:patch!chimerautils-extra",
]
pkgdesc = "Tool to build flatpaks from source"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://docs.flatpak.org"
source = f"https://github.com/flatpak/flatpak-builder/releases/download/{pkgver}/flatpak-builder-{pkgver}.tar.xz"
sha256 = "dc27159394baaa2cb523f52f874472ff50d161983233264ca2a22e850741ec7a"
# CFI: fails on builder_(context|cache)_finalize during "flatpak-builder build ..."
hardening = ["vis", "!cfi"]
