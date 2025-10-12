pkgname = "typescript"
pkgver = "5.9.3"
pkgrel = 1
depends = ["nodejs"]
pkgdesc = "Superset of JavaScript that compiles to JavaScript output"
license = "Apache-2.0"
url = "https://github.com/microsoft/TypeScript"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d371a2430d6305290d1bddaf195fdd629d1a8708cda08f4a72fc923b65d36c4a"


def install(self):
    self.install_license("LICENSE.txt")
    self.install_files(".", "usr/share/node_modules", name="typescript")
    self.uninstall("usr/share/node_modules/typescript/LICENSE.txt")
    self.install_dir("usr/bin")
    self.install_link("usr/bin/tsc", "../share/node_modules/typescript/bin/tsc")
    self.install_link(
        "usr/bin/tsserver", "../share/node_modules/typescript/bin/tsserver"
    )
