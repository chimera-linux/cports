pkgname = "sysstat"
pkgver = "12.7.4"
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
sha256 = "71b38ee41e661775ed220d32153723e44d992e0091029d645dab8f7b7a127287"
hardening = ["vis", "cfi"]
# dunno how to run these
options = ["!check"]
