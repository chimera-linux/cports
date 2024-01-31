pkgname = "thunderbird"
pkgver = "123.0_beta2"
pkgrel = 0
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "cargo",
    "cbindgen",
    "clang-devel",
    "gettext",
    "gmake",
    "libtool",
    "llvm-devel",
    "nasm",
    "nodejs",
    "pkgconf",
    "python",
    "rust",
    "wasi-sdk",
    "zip",
]
makedepends = [
    "alsa-lib-devel",
    "dbus-devel",
    "ffmpeg-devel",
    "freetype-devel",
    "glib-devel",
    "gtk+3-devel",
    "icu-devel",
    "libevent-devel",
    "libffi-devel",
    "libjpeg-turbo-devel",
    "libnotify-devel",
    "libogg-devel",
    "libpng-devel",
    "libpulse-devel",
    "libtheora-devel",
    "libvorbis-devel",
    "libvpx-devel",
    "libwebp-devel",
    "libxcomposite-devel",
    "libxscrnsaver-devel",
    "libxt-devel",
    "mesa-devel",
    "nspr-devel",
    "nss-devel",
    "pipewire-jack-devel",
    "pixman-devel",
    "rust-std",
    "zlib-devel",
]
provides = [
    # backwards-compatibility with old subpackages
    f"thunderbird-default={pkgver}-r{pkgrel}",
    f"thunderbird-wayland={pkgver}-r{pkgrel}",
]
pkgdesc = "Thunderbird mail client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND MPL-2.0"
url = "https://www.thunderbird.net"
source = f"$(MOZILLA_SITE)/{pkgname}/releases/{pkgver.replace('_beta', 'b')}/source/{pkgname}-{pkgver.replace('_beta', 'b')}.source.tar.xz"
sha256 = "1cb17b9a6121e8aee7cf2bcc2bfd37d8d0f96ea07b4242388de226668f52e249"
debug_level = 1  # defatten, especially with LTO
tool_flags = {
    "LDFLAGS": ["-Wl,-rpath=/usr/lib/thunderbird", "-Wl,-z,stack-size=2097152"]
}
env = {
    "MAKE": "/usr/bin/gmake",
    "SHELL": "/usr/bin/sh",
    "BUILD_OFFICIAL": "1",
    "MOZILLA_OFFICIAL": "1",
    "USE_SHORT_LIBNAME": "1",
    "MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE": "system",
    "MOZ_APP_REMOTINGNAME": "Thunderbird",
    "MOZBUILD_STATE_PATH": f"/builddir/{pkgname}-{pkgver}/.mozbuild",
    # thunderbird checks for it by calling --help
    "CBUILD_BYPASS_STRIP_WRAPPER": "1",
}
# FIXME: see firefox
hardening = ["!int"]
# XXX: maybe someday
options = ["!cross", "!check"]

if self.profile().endian == "big":
    broken = "broken colors, needs patching, etc."

# crashes compiler in gl.c
if self.profile().arch == "riscv64":
    tool_flags["CXXFLAGS"] = ["-U_FORTIFY_SOURCE"]


def post_extract(self):
    self.cp(
        self.files_path / "stab.h", "toolkit/crashreporter/google-breakpad/src"
    )


def post_patch(self):
    from cbuild.util import cargo

    for crate in ["audio_thread_priority"]:
        cargo.clear_vendor_checksums(self, crate, vendor_dir="third_party/rust")


def init_configure(self):
    from cbuild.util import cargo

    self.env["AS"] = self.get_tool("CC")
    self.env["MOZ_MAKE_FLAGS"] = f"-j{self.make_jobs}"
    self.env["RUST_TARGET"] = self.profile().triplet
    self.env["RUSTFLAGS"] = ""
    # use all the cargo env vars we enforce
    self.env.update(cargo.get_environment(self))


def do_configure(self):
    self.rm("objdir", recursive=True, force=True)
    self.mkdir("objdir")

    extra_opts = []

    match self.profile().arch:
        case "x86_64" | "aarch64":
            extra_opts += ["--enable-rust-simd"]

    if self.has_lto():
        extra_opts += ["--enable-lto=cross"]

    self.do(
        self.chroot_cwd / "mach",
        "configure",
        "--prefix=/usr",
        "--libdir=/usr/lib",
        "--host=" + self.profile().triplet,
        "--target=" + self.profile().triplet,
        "--enable-linker=lld",
        "--enable-release",
        "--enable-optimize",
        "--disable-install-strip",
        "--disable-strip",
        "--with-wasi-sysroot=/usr/wasm32-unknown-wasi",
        # we have our own flags and better
        "--disable-hardening",
        # system libs
        "--with-system-pixman",
        "--with-system-ffi",
        "--with-system-nspr",
        "--with-system-nss",
        "--with-system-jpeg",
        "--with-system-webp",
        "--with-system-zlib",
        "--with-system-libevent",
        "--with-system-libvpx",
        "--with-system-icu",
        # no apng support
        "--without-system-png",
        # features
        "--enable-dbus",
        "--enable-jack",
        "--enable-ffmpeg",
        "--enable-pulseaudio",
        "--enable-necko-wifi",
        "--enable-default-toolkit=cairo-gtk3-wayland",
        "--enable-audio-backends=pulseaudio",
        # disabled features
        "--disable-profiling",
        "--disable-jemalloc",
        "--disable-tests",
        "--disable-updater",
        "--disable-alsa",
        # mail options
        "--enable-official-branding",
        "--enable-application=comm/mail",
        "--allow-addon-sideload",
        # conditional opts
        *extra_opts,
        wrksrc="objdir",
    )


def do_build(self):
    self.do(self.chroot_cwd / "mach", "build", wrksrc="objdir")


def do_install(self):
    self.do(
        self.chroot_cwd / "mach",
        "install",
        wrksrc="objdir",
        env={"DESTDIR": str(self.chroot_destdir)},
    )

    self.install_file(
        self.files_path / "vendor.js",
        "usr/lib/thunderbird/defaults/preferences",
    )
    self.install_file(
        self.files_path / "thunderbird.desktop", "usr/share/applications"
    )

    # icons
    for sz in [16, 22, 24, 32, 48, 128, 256]:
        self.install_file(
            f"comm/mail/branding/thunderbird/default{sz}.png",
            f"usr/share/icons/hicolor/{sz}x{sz}/apps",
            name="thunderbird.png",
        )

    # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
    self.rm(self.destdir / "usr/lib/thunderbird/thunderbird-bin")
    self.install_link("thunderbird", "usr/lib/thunderbird/thunderbird-bin")
