pkgname = "stockfish"
pkgver = "17"
pkgrel = 0
build_wrksrc = "src"
build_style = "makefile"
make_build_target = "build"
make_build_args = ["optimize=no", "SUPPORTED_ARCH=true", "arch=any"]
pkgdesc = "Free UCI chess engine derived from Glaurung"
maintainer = "shtayerc <david.murko@mailbox.org>"
license = "GPL-3.0-or-later"
url = "https://stockfishchess.org"
_net_file_big = "nn-1111cefa1111.nnue"
_net_file_small = "nn-37f18f62d772.nnue"
source = [
    f"https://github.com/official-stockfish/Stockfish/archive/sf_{pkgver}.tar.gz",
    f"!https://tests.stockfishchess.org/api/nn/{_net_file_big}",
    f"!https://tests.stockfishchess.org/api/nn/{_net_file_small}",
]
sha256 = [
    "8f9b52285c3348c065b7cb58410626df16d7416a2e60a3b04f3ec7c038e67ad1",
    "1111cefa11116b77161bd4b14dab4c50f26e5920c756f4861592be3dcd6de174",
    "37f18f62d772f3107e1d6aaca3898c130c3c86f2ab63e6555fbbca20635a899d",
]
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
# no check target
options = ["!check"]


def post_extract(self):
    self.cp(self.sources_path / _net_file_big, self.build_wrksrc)
    self.cp(self.sources_path / _net_file_small, self.build_wrksrc)


def install(self):
    self.install_bin("stockfish")
