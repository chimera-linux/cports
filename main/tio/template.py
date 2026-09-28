pkgname = "tio"
pkgver = "3.9"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "bash-completion",
    "glib-devel",
    "linux-headers",
    "lua5.4-devel",
]
pkgdesc = "Terminal Serial I/O tool"
license = "GPL-2.0-or-later"
url = "https://github.com/tio/tio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "88e6fc49f458526a265357601e4fb3e7400685e9720a9150227cbd288432e6f1"
