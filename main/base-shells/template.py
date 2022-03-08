pkgname = "base-shells"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = ["bsdutils"]
triggers = ["/etc/shells.d"]
pkgdesc = "Trigger to manage /etc/shells"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]
