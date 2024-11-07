pkgname = "tea"
pkgver = "0.9.2"
pkgrel = 6
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X main.Version={pkgver}",
]
hostmakedepends = ["go"]
pkgdesc = "CLI tool to interact with Gitea servers"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://gitea.com/gitea/tea"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b5a944de8db7d5af4aa87e9640261c925f094d2b6d26c4faf2701773acab219b"


def post_install(self):
    self.install_license("LICENSE")
