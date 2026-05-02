pkgname = "goop"
pkgver = "0_git20250503"
_commit = "5865759563e115aa1ba75268aa40bb42ecac82dc"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Website git repository dumping tool"
license = "MIT"
url = "https://github.com/nyancrimew/goop"
source = f"{url}/archive/{_commit}.zip"
sha256 = "6fb1d27132d2ebc95c08157844d666723d23f1fc7a27cc646e8f0c22cd179438"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
