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
def _jreh(self):
    self.pkgdesc = f"{pkgdesc} (headless JRE)"
    self.depends = ["alt:java-jre-headless!openjdk17"]
    return []


@subpackage("java-jre")
def _jre(self):
    self.pkgdesc = f"{pkgdesc} (JRE)"
    self.depends = ["alt:java-jre!openjdk17"]
    return []
