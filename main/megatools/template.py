pkgname = "megatools"
pkgver = "1.11.1.20241028"
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
    "fuse-devel",
    "glib-devel",
    "glib-networking",
    "gobject-introspection",
    "curl-devel",
    "libsodium-devel",
    "openssl3-devel",
]
pkgdesc = "Command line client for mega.nz"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "GPL-2.0-or-later"
url = "https://megatools.megous.com"
source = f"{url}/builds/megatools-{pkgver}.tar.gz"
sha256 = "3632135a23aa737950e74183199eb23d4e44461ca4221842717225fb31527a4d"
hardening = ["vis", "cfi"]
