pkgname = "libtorrent-rasterbar"
pkgver = "2.0.9"
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
sha256 = "90cd92b6061c5b664840c3d5e151d43fedb24f5b2b24e14425ffbb884ef1798e"

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
