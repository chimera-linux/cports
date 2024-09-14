pkgname = "megatools"
pkgver = "1.11.1.20230212"
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
    "libcurl-devel",
    "libsodium-devel",
    "openssl-devel",
]
pkgdesc = "Command line client for mega.nz"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "GPL-2.0-or-later"
url = "https://megatools.megous.com"
source = f"{url}/builds/megatools-{pkgver}.tar.gz"
sha256 = "ecfa2ee4b277c601ebae648287311030aa4ca73ea61ee730bc66bef24ef19a34"
hardening = ["vis", "cfi"]
