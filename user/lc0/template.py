pkgname = "lc0"
pkgver = "0.31.0"
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
    "c4ed3f967066f272038ab8f4786680bd8e96287840020fb226f6591b8ed49572",
    "96d82279d1c65ba41ed136977cdbb5c2fab2a30212982f65ab679b425056e9e7",
]
tool_flags = {"CXXFLAGS": []}

if self.profile().arch == "ppc64":
    tool_flags["CXXFLAGS"] += ["-DEIGEN_DONT_VECTORIZE"]
