pkgname = "snooze"
pkgver = "0.6"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Run a command at a particular time"
license = "CC0-1.0"
url = "https://github.com/leahneukirchen/snooze"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3a4a2f3f00d42e30647d9af79c8e417990ced6c3f0565474b1ca717938b1e2ab"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    # still left for dinit-chimera
    self.install_file(self.files_path / "dinit-snooze", "usr/lib", mode=0o755)
