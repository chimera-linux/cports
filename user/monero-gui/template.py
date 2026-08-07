pkgname = "monero-gui"
pkgver = "0.18.5.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSTACK_TRACE=OFF",
    "-DARCH=default",
    "-DVERSION_IS_RELEASE=true",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "hidapi-devel",
    "libgcrypt-devel",
    "libsodium-devel",
    "libzmq-devel",
    "miniupnpc-devel",
    "openssl3-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "readline-devel",
    "unbound-devel",
    "xz-devel",
]
depends = ["qt6-qtsvg"]
pkgdesc = "GUI wallet for Monero digital currency"
license = "BSD-3-Clause"
url = "https://getmonero.org"
source = [
    f"https://github.com/monero-project/monero-gui/archive/v{pkgver}.tar.gz",
    # these are the revisions for the tag, must be updated
    "https://github.com/dlbeer/quirc/archive/927d680904dc95fdff4cd9d022eb374b438ff8f2.tar.gz",
    "https://github.com/monero-project/monero/archive/4f92268d7c16741cfb41e5bbe2aa46cc260a9ea5.tar.gz",
    # these are monero externals for the revision above
    "https://github.com/tevador/RandomX/archive/6c4340ba4561aec9a3611c1aedf9931239777fb3.tar.gz",
    "https://github.com/Tencent/rapidjson/archive/129d19ba7f496df5e33658527a7158c79b99c21c.tar.gz",
    "https://github.com/monero-project/supercop/archive/633500ad8c8759995049ccd022107d1fa8a1bbc9.tar.gz",
    "https://github.com/trezor/trezor-common/archive/bff7fdfe436c727982cc553bdfb29a9021b423b0.tar.gz",
]
source_paths = [
    ".",
    "external/quirc",
    "monero",
    "monero/external/randomx",
    "monero/external/rapidjson",
    "monero/external/supercop",
    "monero/external/trezor-common",
]
sha256 = [
    "1bbb7c016e334be46d91fe2031f41b190beb8ff3d8b2b6a0d5eef9f9be331a00",
    "a980041c34f8ad9472f57f509ec1c54e1dfd07e843f4419285f5715423410140",
    "4fdd15401af04e1ce84dcae40c8c114320d1cc9b449db25c0d57efa4b4054881",
    "d98a8885968d736b36657fa5264786d4947c3fcf433c873802678527e6db3584",
    "44b007d419ac21b6affec58991e865ee572346ead19b73cf1c3e4e11c7a81273",
    "b973b9d8269ec4d97c3c3443f0dad96d09f72b1b30e616e0947557adbdbb03f7",
    "951f4df9dfb2466698e0b0a1b52ec27e4d6f13538ff22f1d6c0ae87f9d07c1b6",
]
# needs some manual setup
options = ["!cross"]


def install(self):
    # skip installing another copy of monero, we only want the gui wallet
    self.install_bin(f"{self.make_dir}/bin/monero-wallet-gui")
    self.install_license("LICENSE")
