pkgname = "66-init"
pkgver = "0.8.2.1"
pkgrel = 0
build_style = "meson"
configure_args = [
  "-Denable-all-pic=true",
  "-Denable-pie=true",
  "-Dwith-doc=true"
]
makedepends = [
  "skalibs-devel",
  "execline-devel"
  "s6-devel",
  "oblibs-devel",
  "linux-headers",
  "lowdown"
]
depends = [
  "oblibs",
  "execline"
  "s6",
  "s6-ftrig",
  "s6-fdholder",
  "s6-log"
]
options = [
  "!check",
  "!cross"
]
hardening = [
  "cfi",
  "sst"
]
pkgdesc = "66 service manager from obarun"
license = "ISC"
url = "https://web.obarun.org/software/66/{pkgver}/index"
source = f"https://git.obarun.org/Obarun/66/-/archive/{pkgver}/66-{pkgver}.tar.gz"
