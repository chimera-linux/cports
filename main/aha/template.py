pkgname = "aha"
pkgver = "0.5.1"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Ansi HTML Adapter"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later OR MPL-1.1"
url = "https://github.com/theZiz/aha"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "6aea13487f6b5c3e453a447a67345f8095282f5acd97344466816b05ebd0b3b1"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]
