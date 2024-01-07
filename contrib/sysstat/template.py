pkgname = "sysstat"
pkgver = "12.7.5"
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
sha256 = "57664040a549d33bb06a1121c7124d4cadd9b8b35f815856c194393047cd4d6b"
hardening = ["vis", "cfi"]
# dunno how to run these
options = ["!check"]
