pkgname = "lc0"
pkgver = "0.31.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "eigen",
    "gtest-devel",
    "ocl-icd-devel",
    "protobuf-c-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "UCI chess engine designed to play via neural network"
maintainer = "shtayerc <david.murko@mailbox.org>"
license = "GPL-3.0-only"
url = "https://github.com/LeelaChessZero/lc0"
_lczero_commit = "55e1b382efadd57903e37f2a2e29caef3ea85799"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    f"https://github.com/LeelaChessZero/lczero-common/archive/{_lczero_commit}.tar.gz",
]
source_paths = [".", "libs/lczero-common"]
sha256 = [
    "6dea1e67e33ec0513853df4fef24d51318e47a6cf0f35c0491cce5c1547dc023",
    "96d82279d1c65ba41ed136977cdbb5c2fab2a30212982f65ab679b425056e9e7",
]
tool_flags = {"CXXFLAGS": []}

if self.profile().arch == "ppc64":
    tool_flags["CXXFLAGS"] += ["-DEIGEN_DONT_VECTORIZE"]
