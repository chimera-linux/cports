pkgname = "hx"
pkgver = "1.0.15"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    f"hx_git_hash=chimera-{pkgver}",
    f"hx_version={pkgver}",
]
pkgdesc = "Terminal hex editor"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/krpors/hx"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d4d1f4b65034cd16dd4119f064eae17fe56b39ba4813a958d493e5bfb0a91529"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
