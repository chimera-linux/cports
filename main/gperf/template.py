pkgname = "gperf"
pkgver = "3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
pkgdesc = "Perfect hash function generator"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gperf"
source = f"$(GNU_SITE)/gperf/gperf-{pkgver}.tar.gz"
sha256 = "588546b945bba4b70b6a3a616e80b4ab466e3f33024a352fc2198112cdbb3ae2"
# FIXME
hardening = ["vis", "!cfi", "!int"]
