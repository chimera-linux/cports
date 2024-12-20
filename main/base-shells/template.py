pkgname = "base-shells"
pkgver = "0.2"
pkgrel = 0
build_style = "meta"
depends = ["chimerautils"]
triggers = ["/etc/shells.d", "/usr/lib/shells.d"]
pkgdesc = "Trigger to manage /etc/shells"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
protected_paths = ["-etc/shells.d"]
# no tests
options = ["!check"]
