pkgname = "base-shells"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = ["chimerautils"]
triggers = ["/etc/shells.d"]
pkgdesc = "Trigger to manage /etc/shells"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]

def post_install(self):
    self.install_dir("etc/apk/protected_paths.d")
    # unprotect /etc/shells.d to prevent apk-new files being created
    with open(self.destdir / "etc/apk/protected_paths.d/shells.list", "w") as sf:
        sf.write("-etc/shells.d\n")
