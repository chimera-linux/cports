pkgname = "typescript"
pkgver = "5.7.3"
pkgrel = 0
depends = ["nodejs"]
pkgdesc = "Superset of JavaScript that compiles to JavaScript output"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/microsoft/TypeScript"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f421dc7195ab14d1af7b637d010ec936676f9646723f71663042c53e24433450"


def install(self):
    self.install_license("LICENSE.txt")
    self.install_files(".", "usr/share/node_modules", name="typescript")
    self.uninstall("usr/share/node_modules/typescript/LICENSE.txt")
    self.install_dir("usr/bin")
    self.install_link("usr/bin/tsc", "../share/node_modules/typescript/bin/tsc")
    self.install_link(
        "usr/bin/tsserver", "../share/node_modules/typescript/bin/tsserver"
    )
