pkgname = "stockfish"
pkgver = "16.1"
pkgrel = 0
build_wrksrc = "src"
build_style = "makefile"
make_build_target = "build"
make_build_args = ["optimize=no", "SUPPORTED_ARCH=true", "arch=any"]
pkgdesc = "Free UCI chess engine derived from Glaurung"
maintainer = "shtayerc <david.murko@mailbox.org>"
license = "GPL-3.0-or-later"
url = "https://stockfishchess.org"
_net_file_big = "nn-b1a57edbea57.nnue"
_net_file_small = "nn-baff1ede1f90.nnue"
source = [
    f"https://github.com/official-stockfish/Stockfish/archive/sf_{pkgver}.tar.gz",
    f"!https://tests.stockfishchess.org/api/nn/{_net_file_big}",
    f"!https://tests.stockfishchess.org/api/nn/{_net_file_small}",
]
sha256 = [
    "a5f94793b5d4155310397ba89e9c4266570ef0f24cd47de41a9103556f811b82",
    "b1a57edbea574ca8b88d6837473845791beb53d885f87f86d5ccdd5659fbf3b2",
    "baff1ede1f90c1dd1b4f772f1eff29848821801e8186345da7f0eb4121bd6f63",
]
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
# no check target
options = ["!check"]


def post_extract(self):
    self.cp(self.sources_path / _net_file_big, self.build_wrksrc)
    self.cp(self.sources_path / _net_file_small, self.build_wrksrc)


def install(self):
    self.install_bin("stockfish")
