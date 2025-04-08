pkgname = "gperf"
pkgver = "3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
pkgdesc = "Perfect hash function generator"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gperf"
source = f"$(GNU_SITE)/gperf/gperf-{pkgver}.tar.gz"
sha256 = "e0ddadebb396906a3e3e4cac2f697c8d6ab92dffa5d365a5bc23c7d41d30ef62"
# FIXME
hardening = ["vis", "!cfi", "!int"]
