pkgname = "sysstat"
pkgver = "12.7.9"
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
sha256 = "9896143f0dba8d130eabae276d0362c6d4303295612ab9bf060eae225eb766fd"
hardening = ["vis", "cfi"]
# dunno how to run these
options = ["!check"]
