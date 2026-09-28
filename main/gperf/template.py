pkgname = "gperf"
pkgver = "3.3"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
pkgdesc = "Perfect hash function generator"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gperf"
source = f"$(GNU_SITE)/gperf/gperf-{pkgver}.tar.gz"
sha256 = "fd87e0aba7e43ae054837afd6cd4db03a3f2693deb3619085e6ed9d8d9604ad8"
# FIXME
hardening = ["vis", "!cfi", "!int"]
