pkgname = "oblibs"
pkgver = "0.3.4.0"
pkgrel = 0
build_style = "meson"
configure_args = [
  "-Denable-all-pic=true",
  "-Denable-pie=true",
]
makedepends = [
  "skalibs-devel",
  "execline-devel"
  "linux-headers",
]
depends = ["skalibs"]
options = [
  "!check",
  "!cross"
]
hardening = [
  "cfi",
  "sst"
]
pkgdesc = "small general-purpose library used by 66"
license = "ISC"
source = f"https://git.obarun.org/Obarun/oblibs/-/archive/{pkgver}/oblibs-{pkgver}.tar.gz"
