pkgname = "typescript"
pkgver = "5.7.2"
pkgrel = 0
depends = ["nodejs"]
pkgdesc = "Superset of JavaScript that compiles to JavaScript output"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "Apache-2.0"
url = "https://github.com/microsoft/TypeScript"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fa57801450fa6886c6959e24b56b95633baccdc4b03bf285e8aa175ca600fbee"


def install(self):
    self.install_license("LICENSE.txt")
    self.install_files(".", "usr/share/node_modules", name="typescript")
    self.uninstall("usr/share/node_modules/typescript/LICENSE.txt")
    self.install_dir("usr/bin")
    self.install_link("usr/bin/tsc", "../share/node_modules/typescript/bin/tsc")
    self.install_link(
        "usr/bin/tsserver", "../share/node_modules/typescript/bin/tsserver"
    )
