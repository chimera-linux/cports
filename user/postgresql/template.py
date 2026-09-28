pkgname = "postgresql"
pkgver = "1.0"
pkgrel = 0
build_style = "meta"
depends = ["alt:postgresql!postgresql16"]
pkgdesc = "Shared metapackage for PostgreSQL"
license = "custom:none"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]
