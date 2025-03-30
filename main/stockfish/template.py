pkgname = "stockfish"
pkgver = "17.1"
pkgrel = 0
build_wrksrc = "src"
build_style = "makefile"
make_build_target = "build"
make_build_args = ["optimize=no", "SUPPORTED_ARCH=true", "arch=any"]
pkgdesc = "Free UCI chess engine derived from Glaurung"
license = "GPL-3.0-or-later"
url = "https://stockfishchess.org"
_net_file_big = "nn-1c0000000000.nnue"
_net_file_small = "nn-37f18f62d772.nnue"
source = [
    f"https://github.com/official-stockfish/Stockfish/archive/sf_{pkgver}.tar.gz",
    f"!https://tests.stockfishchess.org/api/nn/{_net_file_big}",
    f"!https://tests.stockfishchess.org/api/nn/{_net_file_small}",
]
sha256 = [
    "0cfd9396438798cc68f5c0d5fa0bb458bb8ffff7de06add841aaeace86bec1f1",
    "1c0000000000a67d629999d932d0c373f7450ce43cd12d0562868f4eaf9ae2ad",
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
