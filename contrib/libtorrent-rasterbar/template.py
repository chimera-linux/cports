pkgname = "libtorrent-rasterbar"
pkgver = "2.0.10"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Dpython-bindings=ON",
    "-Dpython-egg-info=ON",
    "-Dbuild_tests=ON",
]
# known broken/flaky/conditionally broken tests
make_check_args = [
    "-E",
    "(test_upnp|test_flags|test_add_torrent|test_create_torrent|test_remove_torrent|test_privacy|test_copy_file|test_web_seed|test_url_seed|test_transfer|test_ssl|test_http_connection|test_lsd)",
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
sha256 = "fc935b8c1daca5c0a4d304bff59e64e532be16bb877c012aea4bda73d9ca885d"

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
