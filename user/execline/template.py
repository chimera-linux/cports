pkgname = "execline"
pkgver = "2.9.8.1"
pkgrel = 0
build_style = "makefile"
makedepends = ["skalibs-devel"]
depends = ["skalibs"]
options = [
  "!check",
  "!cross"
]
hardening = [
  "cfi",
  "sst"
]
pkgdesc = "Non-interactive scripting language"
license = "ISC"
url = "https://skarnet.org/software/execline"
source = f"https://skarnet.org/software/execline/execline-{pkgver}.tar.gz"
sha256 = "23350d10797909636060522607591cb4a2118328cb58c5e65fb19a2c0d47264e"
