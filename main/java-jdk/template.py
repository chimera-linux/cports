pkgname = "java-jdk"
pkgver = "1.0"
pkgrel = 0
build_style = "meta"
depends = ["alt:java-jdk!openjdk17"]
pkgdesc = "Shared metapackage for Java"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]


@subpackage("java-jre-headless")
def _(self):
    self.subdesc = "headless JRE"
    self.depends = ["alt:java-jre-headless!openjdk17"]
    return []


@subpackage("java-jre")
def _(self):
    self.subdesc = "JRE"
    self.depends = ["alt:java-jre!openjdk17"]
    return []
