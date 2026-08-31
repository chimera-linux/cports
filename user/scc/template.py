pkgname = "scc"
pkgver = "4.0.0"
pkgrel = 0
build_style = "go"
make_check_args = []
hostmakedepends = ["go"]
pkgdesc = "Fast and accurate code counter"
license = "MIT OR Unlicense"
url = "https://github.com/boyter/scc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "7e0418d7b6dfa881b2673e50d32da81e9abc34475a305b612b57600d85801abc"

if self.profile().arch in ["loongarch64"]:
    # These fail with differing sign of 0.0 on loongarch: -0.0 vs. 0.0
    make_check_args += [
        "-skip",
        "TestSparklinePath|TestRenderReport_Golden",
    ]


def post_install(self):
    self.install_license("LICENSE")
