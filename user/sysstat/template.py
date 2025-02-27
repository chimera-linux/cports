pkgname = "sysstat"
pkgver = "12.7.7"
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
sha256 = "79bddfca14130797c02aa4d819528aaa243c879e5bbd1c404cd43c9953a8cdf9"
hardening = ["vis", "cfi"]
# dunno how to run these
options = ["!check"]
