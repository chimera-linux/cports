pkgname = "php-common"
pkgver = "1.0"
pkgrel = 0
build_style = "meta"
# technically a cycle, but we don't want this installable without having
# any php provider around, so hack around this a little bit
depends = ["virtual:php-runtime!base-files"]
pkgdesc = "PHP common data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]


def install(self):
    self.install_sysusers(self.files_path / "sysusers.conf", name="php-fpm")
