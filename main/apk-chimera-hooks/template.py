pkgname = "apk-chimera-hooks"
pkgver = "0.1"
pkgrel = 0
pkgdesc = "Chimera Linux apk scriptlets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]

def do_install(self):
    for s in [
        "pycompile"
    ]:
        self.install_file(
            self.files_path / s, "usr/libexec/apk-chimera-hooks", mode = 0o755
        )
