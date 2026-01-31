pkgname = "stockfish"
pkgver = "18"
pkgrel = 0
build_wrksrc = "src"
build_style = "makefile"
make_build_target = "build"
make_build_args = ["optimize=no", "SUPPORTED_ARCH=true", "arch=any"]
pkgdesc = "Free UCI chess engine derived from Glaurung"
license = "GPL-3.0-or-later"
url = "https://stockfishchess.org"
_net_file_big = "nn-c288c895ea92.nnue"
_net_file_small = "nn-37f18f62d772.nnue"
source = [
    f"https://github.com/official-stockfish/Stockfish/archive/sf_{pkgver}.tar.gz",
    f"!https://tests.stockfishchess.org/api/nn/{_net_file_big}",
    f"!https://tests.stockfishchess.org/api/nn/{_net_file_small}",
]
sha256 = [
    "22a195567e3493e7c9ca8bf8fa2339f4ffc876384849ac8a417ff4b919607e7b",
    "c288c895ea924429ea9092e3f36b2b3c1f00f2a3a4c759ff7e57e79e3b43e4a7",
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
