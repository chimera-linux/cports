pkgname = "megatools"
pkgver = "1.11.4.20250411"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "asciidoc",
    "meson",
    "pkgconf",
    # TODO package docbook2x to allow man page compliation
    # "docbook2x",
]
makedepends = [
    "curl-devel",
    "fuse-devel",
    "glib-devel",
    "glib-networking",
    "gobject-introspection",
    "libsodium-devel",
    "openssl3-devel",
]
pkgdesc = "Command line client for mega.nz"
license = "GPL-2.0-or-later"
url = "https://megatools.megous.com"
source = f"{url}/builds/megatools-{pkgver}.tar.gz"
sha256 = "f404ea598c9c5a67a966a007421945dc212460d673fa66bea44544fd82f8e7c9"
hardening = ["vis", "cfi"]
