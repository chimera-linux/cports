pkgname = "evtest"
pkgver = "1.36"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["asciidoc", "automake", "xmlto"]
makedepends = ["linux-headers"]
pkgdesc = "Command line tool to display device input information"
license = "GPL-2.0-or-later"
url = "https://gitlab.freedesktop.org/libevdev/evtest"
source = f"{url}/-/archive/evtest-{pkgver}/evtest-evtest-{pkgver}.tar.gz"
sha256 = "3b9a66c92e48b0cd13b689530b5729c031bc1bcbfe9d19c258f9245e2f8d2a0f"
# silence 10k lines of spam
tool_flags = {"CFLAGS": ["-Wno-initializer-overrides"]}
hardening = ["vis", "cfi"]
