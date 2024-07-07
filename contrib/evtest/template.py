pkgname = "evtest"
pkgver = "1.35"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["asciidoc", "automake", "xmlto"]
makedepends = ["linux-headers"]
pkgdesc = "Command line tool to display device input information"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://gitlab.freedesktop.org/libevdev/evtest"
source = f"{url}/-/archive/evtest-{pkgver}/evtest-evtest-{pkgver}.tar.gz"
sha256 = "06dfe6b9760b78f3f73aca2120cbcb79339b33e59d5c79a49b4bd5d34844b054"
# silence 10k lines of spam
tool_flags = {"CFLAGS": ["-Wno-initializer-overrides"]}
hardening = ["vis", "cfi"]
