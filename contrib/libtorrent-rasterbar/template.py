pkgname = "libtorrent-rasterbar"
pkgver = "2.0.9"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-Dpython-bindings=ON",
    "-Dpython-egg-info=ON",
    "-Dbuild_tests=ON",
]
# known broken/flaky/conditionally broken tests
make_check_args = [
    "-E",
    "(test_upnp|test_flags|test_add_torrent|test_create_torrent|test_remove_torrent|test_privacy|test_copy_file|test_web_seed|test_url_seed|test_transfer|test_ssl)",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python-devel",
    "python-setuptools",
]
makedepends = ["openssl-devel", "boost-devel", "python-devel", "linux-headers"]
pkgdesc = "C++ BitTorrent library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://libtorrent.org"
source = f"https://github.com/arvidn/libtorrent/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "90cd92b6061c5b664840c3d5e151d43fedb24f5b2b24e14425ffbb884ef1798e"

# loud build
tool_flags = {
    "CXXFLAGS": ["-Wno-unsafe-buffer-usage", "-Wno-deprecated"],
    "LDFLAGS": [],
}


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libtorrent-rasterbar-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libtorrent-rasterbar-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python3*"]
