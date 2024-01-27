pkgname = "neovide"
pkgver = "0.12.1"
pkgrel = 0
archs = ["aarch64", "ppc64le", "riscv64", "x86_64"]
build_style = "cargo"
hostmakedepends = [
    "cargo",
    "ninja",
    "libcxx-devel-static",
]
makedepends = [
    "fontconfig-devel",
    "freetype-devel",
    "libexpat-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "zlib-devel",
]
checkdepends = ["neovim"]
pkgdesc = "Graphical client for neovim"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "MIT"
url = "https://neovide.dev"
_gn = "2139%5E20240120gitb5adfe5f574d-1.fc40"
_skia = "2196c5b01b984e30bf28038ab861d0a350d4caf4"
_wuffs = "e3f919ccfe3ef542cfc983a82146070258fb57f8"
_spcross = "6e1fb9b09efadee38748e0fd0e6210d329087e89"
_vmalloc = "a6bfc237255a6bac1513f7c1ebde6d8aed6b5191"
_gn0, _gn1 = _gn.split("-")
source = [
    f"https://github.com/neovide/neovide/archive/refs/tags/{pkgver}.tar.gz>{pkgname}-{pkgver}.tar.gz",
    f"https://kojipkgs.fedoraproject.org/packages/gn/{_gn0}/{_gn1}/src/gn-{_gn}.src.rpm>gn-{_gn}.tar.gz",
    f"https://github.com/rust-skia/skia/archive/{_skia}.tar.gz",
    f"https://github.com/google/wuffs-mirror-release-c/archive/{_wuffs}.tar.gz",
    f"https://github.com/KhronosGroup/SPIRV-Cross/archive/{_spcross}.tar.gz",
    f"https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/{_vmalloc}.tar.gz",
]
source_paths = [
    ".",
    "_gn",
    "skia",
    "skia/third_party/externals/wuffs",
    "skia/third_party/externals/spirv-cross",
    "skia/third_party/externals/vulkanmemoryallocator",
]
sha256 = [
    "95df61d51635a981697a6c4b3e63a9feb29bb90bfc69940c02c73273a61cfd10",
    "fff8d73970df98b786270de0ff5e35adc7904037beade6b8f2952ac552c55a4e",
    "e8d08fed6bfc7e61216233b00585a212eace629816b7f1ddb0c0d90eb6df32d4",
    "e849dab1f372f16b782ba7528e7f70281e35425bd2d644c92a36fb95909f98db",
    "e8f175054803997c98df5270fde711b7d6d9d5434194718df5a2b8527f654e7c",
    "7444a78beeb01ee3baca58721b2b7c936521f05df1f6e322bbafe3c2d4114704",
]
env = {
    "SKIA_SOURCE_DIR": f"/builddir/{pkgname}-{pkgver}/skia",
    "SKIA_GN_COMMAND": f"/builddir/{pkgname}-{pkgver}/gn/out/gn",
    "SKIA_NINJA_COMMAND": "ninja",
    "SKIA_USE_SYSTEM_LIBRARIES": "1",
}


def post_extract(self):
    from cbuild.core import chroot

    # see cbuild/hooks/do_extract/000_sources.py
    with self.pushd("_gn"):
        self.mkdir("gn/out", True)
        self.mv("last_commit_position.h", "gn/out")
        ret = chroot.enter(
            "tar",
            "-x",
            "--no-same-owner",
            "--no-same-permissions",
            "-f",
            self.chroot_cwd / f"gn-{_gn[18:30]}.tar.gz",
            "-C",
            self.chroot_cwd / "gn",
            ro_root=True,
            unshare_all=True,
        ).returncode
        if ret != 0:
            self.error(f"Could not extract gn-{_gn[18:30]}.tar.gz (exit {ret})")
    self.mv("_gn/gn", "gn")
    self.rm("_gn", True)


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "skia-bindings")


def do_configure(self):
    with self.pushd("gn"):
        self.do("python", "build/gen.py", "--no-last-commit-position")


def pre_build(self):
    with self.pushd("gn"):
        self.do("ninja", "-C", "out")


def do_install(self):
    self.install_license("LICENSE")
    self.install_bin(f"target/{self.profile().triplet}/release/neovide")
    self.install_file("assets/neovide.desktop", "usr/share/applications")
    self.install_file(
        "assets/neovide.svg",
        "usr/share/icons/hicolor/scalable/apps",
    )
    for f in self.find("assets", "neovide-*.png"):
        dim = str(f).removeprefix("assets/neovide-").removesuffix(".png")
        self.install_file(
            f,
            f"usr/share/icons/hicolor/{dim}/apps",
            name="neovide.png",
        )
