pkgname = "libtorrent-rasterbar"
pkgver = "2.0.8"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Dpython-bindings=ON",
    "-Dpython-egg-info=ON",
    "-Dbuild_tests=ON",
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
sha256 = "09dd399b4477638cf140183f5f85d376abffb9c192bc2910002988e27d69e13e"

# loud build
tool_flags = {
    "CXXFLAGS": ["-Wno-unsafe-buffer-usage", "-Wno-deprecated"],
    "LDFLAGS": [],
}

# ld: error: section size decrease is too large
if self.profile().arch == "riscv64":
    tool_flags["CXXFLAGS"] += ["-mno-relax"]
    tool_flags["LDFLAGS"] += ["-mno-relax"]


def do_check(self):
    self.do(
        "ctest",
        f"-j{self.make_jobs}",
        "--output-on-failure",
        "--test-dir",
        "build",
        "--exclude-regex",
        # known broken/flaky/conditionally broken tests
        "test_upnp|test_flags|test_add_torrent|test_create_torrent|test_remove_torrent|test_privacy|test_copy_file|test_web_seed|test_url_seed|test_transfer|test_ssl",
    )


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libtorrent-rasterbar-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libtorrent-rasterbar-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python3*"]
