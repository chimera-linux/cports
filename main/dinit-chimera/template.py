pkgname = "dinit-chimera"
_commit = "71553f40d3bffadc28b1d5ba7efa203b1d488957"
pkgver = "0.1"
pkgrel = 0
build_style = "makefile"
depends = ["dinit", "util-linux"]
pkgdesc = "Chimera core services suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/{_commit}.tar.gz"
sha256 = "a90ee19f9757ee98267b514d9935d45805eb5681b8b82cf1f52ea71404ba1fba"
# no tests
options = ["!check", "brokenlinks"]

def post_install(self):
    self.install_file(self.files_path / "hostname", "etc")
    self.install_file(self.files_path / "os-release", "etc")
    self.install_file(self.files_path / "locale.conf", "etc")
    # init symlink
    self.install_link("dinit", "usr/bin/init")
