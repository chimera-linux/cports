pkgname = "catatonit"
pkgver = "0.2.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
]
pkgdesc = "Init for containers"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/openSUSE/catatonit"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d0cf1feffdc89c9fb52af20fc10127887a408bbd99e0424558d182b310a3dc92"
hardening = ["vis", "cfi"]
