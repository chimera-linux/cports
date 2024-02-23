pkgname = "hx"
pkgver = "1.0.14"
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
sha256 = "7b7c494df149535f768b3aa449159928aec92b468a17f9eedebcea3dd21343d1"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
