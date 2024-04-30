pkgname = "tio"
pkgver = "3.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "bash-completion",
    "glib-devel",
    "inih-devel",
    "linux-headers",
    "lua5.4-devel",
]
pkgdesc = "Terminal Serial I/O tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/tio/tio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "82a0948bbbd9eff87e86e795c60994cdb1263a1334f1db68f061a0704e600b6d"
