pkgname = "megatools"
pkgver = "1.11.5.20250706"
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
sha256 = "51f78a03748a64b1066ce28a2ca75d98dbef5f00fe9789dc894827f9a913b362"
hardening = ["vis", "cfi"]
