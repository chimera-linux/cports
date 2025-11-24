pkgname = "golangci-lint-langserver"
pkgver = "0.0.11"
pkgrel = 4
build_style = "go"
hostmakedepends = ["go"]
depends = ["golangci-lint"]
checkdepends = ["golangci-lint"]
pkgdesc = "Language server for golangci-lint"
license = "MIT"
url = "https://github.com/nametake/golangci-lint-langserver"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d9f1fc02861eeb9ce60c89e79be706d7ec636f653d5039a76857b18cb98875fb"


def post_install(self):
    self.install_license("LICENSE")
