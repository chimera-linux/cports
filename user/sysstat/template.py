pkgname = "sysstat"
pkgver = "12.7.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-compress-manpg"]
make_dir = "."
hostmakedepends = [
    "automake",
]
makedepends = ["linux-headers"]
pkgdesc = "Linux performance monitoring tools"
license = "GPL-2.0-or-later"
url = "https://sysstat.github.io"
source = f"https://sysstat.github.io/sysstat-packages/sysstat-{pkgver}.tar.xz"
sha256 = "fce51c768a9babfc871e1896409a17be7017460730a796b36b502dbaac0ed2b9"
hardening = ["vis", "cfi"]
# dunno how to run these
options = ["!check"]
