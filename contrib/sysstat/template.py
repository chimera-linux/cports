pkgname = "sysstat"
pkgver = "12.7.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-compress-manpg"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
]
makedepends = ["linux-headers"]
pkgdesc = "Linux performance monitoring tools"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://sysstat.github.io"
source = f"https://sysstat.github.io/sysstat-packages/sysstat-{pkgver}.tar.xz"
sha256 = "474b2bbc89e47b22dc8e4832cc2c555e7fb52f1271b7913434290986a62b71f7"
hardening = ["vis", "cfi"]
# dunno how to run these
options = ["!check"]
