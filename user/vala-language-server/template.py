pkgname = "vala-language-server"
pkgver = "0.48.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
    "vala",
]
makedepends = [
    "jsonrpc-glib-devel",
    "libgee-devel",
    "vala-devel",
]
pkgdesc = "Language server for vala"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/vala-lang/vala-language-server"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6e848334accd27566843d56db15bedcf7529dc68e416d23d3b4e9fc522019c68"
