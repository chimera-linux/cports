pkgname = "postgresql"
pkgver = "1.1"
pkgrel = 0
build_style = "meta"
depends = ["alt:postgresql!postgresql17"]
pkgdesc = "Shared metapackage for PostgreSQL"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]
