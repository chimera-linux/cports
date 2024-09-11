pkgname = "gpicview"
pkgver = "0.2.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-gtk3"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = ["gtk+3-devel"]
pkgdesc = "Lightweight image viewer"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/lxde/gpicview"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1b7be0045b82592cf79c7a7761d4f905d36c7c36b480d39219fe0bdb960a4a58"
