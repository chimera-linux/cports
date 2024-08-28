pkgname = "linux-pam-base"
pkgver = "0.111"
pkgrel = 0
pkgdesc = "Pluggable Authentication Modules for Linux"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]


def install(self):
    for f in self.files_path.glob("*"):
        if f.name == "README.md":
            continue
        self.install_file(f, "usr/lib/pam.d", mode=0o644)
