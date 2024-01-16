pkgname = "flatpak-builder"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "docbook-xsl",
    "gettext-devel",
    "gmake",
    "libtool",
    "libxml2-progs",
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
    "musl-bsd-headers",
]
checkdepends = ["bash"]
depends = [
    "elfutils",
    "flatpak",
    "git",
    "llvm-binutils",
    "virtual:cmd:patch!chimerautils-extra",
]
pkgdesc = "Tool to build flatpaks from source"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://docs.flatpak.org"
source = f"https://github.com/flatpak/flatpak-builder/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e257825a47f7a3e71e30fb0f80f2d9ac6e4801f746f552dfaf0e564e3ee351c8"
# FIXME: CFI fails on builder_(context|cache)_finalize during "flatpak-builder build ..."
hardening = ["vis", "!cfi"]
