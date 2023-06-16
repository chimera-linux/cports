pkgname = "gperf"
pkgver = "3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "Perfect hash function generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gperf"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "588546b945bba4b70b6a3a616e80b4ab466e3f33024a352fc2198112cdbb3ae2"
# FIXME cfi int
hardening = ["vis", "!cfi", "!int"]
