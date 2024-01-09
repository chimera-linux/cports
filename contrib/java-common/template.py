pkgname = "java-common"
pkgver = "1.0"
pkgrel = 1
build_style = "meta"
# technically a cycle, but we don't want this installable without having
# any java provider around, and it gets built as a dep of every openjdk
depends = ["cmd:java!base-files"]
triggers = ["/usr/lib/jvm"]
pkgdesc = "Java common data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]
