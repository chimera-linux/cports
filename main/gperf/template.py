pkgname = "gperf"
pkgver = "3.2.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
pkgdesc = "Perfect hash function generator"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gperf"
source = f"$(GNU_SITE)/gperf/gperf-{pkgver}.tar.gz"
sha256 = "ed5ad317858e0a9badbbada70df40194002e16e8834ac24491307c88f96f9702"
# FIXME
hardening = ["vis", "!cfi", "!int"]
