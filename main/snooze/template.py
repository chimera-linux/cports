pkgname = "snooze"
pkgver = "0.5.1"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Run a command at a particular time"
license = "CC0-1.0"
url = "https://github.com/leahneukirchen/snooze"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "abb0df288e8fe03ae25453d5f0b723b03a03bcc7afa41b9bec540a7a11a9f93e"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    # still left for dinit-chimera
    self.install_file(self.files_path / "dinit-snooze", "usr/lib", mode=0o755)
