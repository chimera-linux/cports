pkgname = "libtorrent-rasterbar"
pkgver = "2.0.11"
pkgrel = 3
build_style = "cmake"
configure_args = [
    "-Dpython-bindings=ON",
    "-Dpython-egg-info=ON",
    "-Dbuild_tests=ON",
]
# known broken/flaky/conditionally broken tests
make_check_args = [
    "-E",
    "(test_upnp|test_flags|test_add_torrent|test_create_torrent|test_remove_torrent|test_privacy|test_copy_file|test_web_seed|test_url_seed|test_transfer|test_ssl|test_http_connection|test_lsd|test_priority)",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python-devel",
    "python-setuptools",
]
makedepends = ["openssl3-devel", "boost-devel", "python-devel", "linux-headers"]
pkgdesc = "C++ BitTorrent library"
license = "BSD-3-Clause"
url = "https://libtorrent.org"
source = f"https://github.com/arvidn/libtorrent/releases/download/v{pkgver}/libtorrent-rasterbar-{pkgver}.tar.gz"
sha256 = "f0db58580f4f29ade6cc40fa4ba80e2c9a70c90265cd77332d3cdec37ecf1e6d"

# loud build
tool_flags = {
    "CXXFLAGS": ["-Wno-unsafe-buffer-usage", "-Wno-deprecated"],
    "LDFLAGS": [],
}


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libtorrent-rasterbar-devel")
def _(self):
    return self.default_devel()


@subpackage("libtorrent-rasterbar-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python3*"]
