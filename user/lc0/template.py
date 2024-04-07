pkgname = "lc0"
pkgver = "0.30.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "eigen",
    "gtest-devel",
    "ocl-icd-devel",
    "protobuf-c-devel",
    "zlib-devel",
]
pkgdesc = "UCI chess engine designed to play via neural network"
maintainer = "shtayerc <david.murko@mailbox.org>"
license = "GPL-3.0-only"
url = "https://github.com/LeelaChessZero/lc0"
_lczero_commit = "fafda0f59c8511b5d933ef758c1e4b10a62da1e0"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    f"https://github.com/LeelaChessZero/lczero-common/archive/{_lczero_commit}.tar.gz",
]
source_paths = [".", "libs/lczero-common"]
sha256 = [
    "c5a11469364d06731b8da09bf9e1989ca6b39695add7d08bd96dd834dd0b5b2a",
    "6de0fd8248369ad1050e6433c6d8d14044e99f53ccf4ffc763ad47c046979237",
]
tool_flags = {"CXXFLAGS": []}

if self.profile().arch == "ppc64":
    tool_flags["CXXFLAGS"] += ["-DEIGEN_DONT_VECTORIZE"]
