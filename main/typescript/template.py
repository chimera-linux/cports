pkgname = "typescript"
pkgver = "6.0.3"
pkgrel = 0
depends = ["nodejs"]
pkgdesc = "Superset of JavaScript that compiles to JavaScript output"
license = "Apache-2.0"
url = "https://github.com/microsoft/TypeScript"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c26953b79c1197e02f5666a0b612d5b9707339557aa9744097e7d5719de1a117"


def install(self):
    self.install_license("LICENSE.txt")
    self.install_files(".", "usr/share/node_modules", name="typescript")
    self.uninstall("usr/share/node_modules/typescript/LICENSE.txt")
    self.install_dir("usr/bin")
    self.install_link("usr/bin/tsc", "../share/node_modules/typescript/bin/tsc")
    self.install_link(
        "usr/bin/tsserver", "../share/node_modules/typescript/bin/tsserver"
    )
