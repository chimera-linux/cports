pkgname = "ledger"
pkgver = "3.3.2"
pkgrel = 5
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
make_dir = "."
# see https://github.com/ledger/ledger/issues/1783
make_check_args = ["-E", "(BaselineTest_cmd-pricedb|BaselineTest_cmd-prices)"]
hostmakedepends = ["cmake", "ninja"]
makedepends = ["boost-devel", "utfcpp", "mpfr-devel", "libedit-devel"]
pkgdesc = "Plain text accounting software"
license = "BSD-3-Clause"
url = "https://ledger-cli.org"
source = f"https://github.com/ledger/ledger/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "555296ee1e870ff04e2356676977dcf55ebab5ad79126667bc56464cb1142035"


def post_install(self):
    self.install_license("LICENSE.md")
