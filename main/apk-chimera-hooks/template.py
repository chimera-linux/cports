pkgname = "apk-chimera-hooks"
pkgver = "0.1"
pkgrel = 0
pkgdesc = "Chimera Linux apk scriptlets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"
# no tests
options = ["bootstrap", "!check"]

# These are taken from Void Linux's xbps-triggers package and modified
# as needed; a lot of things in Chimera are handled through actual real
# triggers, but these are things that all need awareness of individual
# installation stages, and the Void scripts are battle-tested (and we
# use the same tool stack for things like user management)

def do_install(self):
    for s in [
        "pycompile", "system-accounts", "xml-catalog",
    ]:
        self.install_file(
            self.files_path / s, "usr/libexec/apk-chimera-hooks", mode = 0o755
        )
