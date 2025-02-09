pkgname = "megatools"
pkgver = "1.11.3.20250203"
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
sha256 = "37a426ecd360220c9d6c1389c19a9e8f3e07077a9d996e3fd9f756657c1df0a9"
hardening = ["vis", "cfi"]
