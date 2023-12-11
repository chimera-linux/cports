pkgname = "thunderbird"
pkgver = "115.6.0"
pkgrel = 1
make_cmd = "gmake"
hostmakedepends = [
    "pkgconf",
    "zip",
    "nasm",
    "cargo",
    "rust",
    "python",
    "cbindgen",
    "llvm-devel",
    "clang-devel",
    "nodejs",
    "gettext",
    "automake",
    "libtool",
    "gmake",
]
makedepends = [
    "rust-std",
    "nss-devel",
    "nspr-devel",
    "gtk+3-devel",
    "icu-devel",
    "dbus-devel",
    "glib-devel",
    "libpulse-devel",
    "pixman-devel",
    "freetype-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libwebp-devel",
    "libevent-devel",
    "libnotify-devel",
    "libvpx-devel",
    "libvorbis-devel",
    "libogg-devel",
    "libtheora-devel",
    "libxt-devel",
    "libxcomposite-devel",
    "libxscrnsaver-devel",
    "pipewire-jack-devel",
    "ffmpeg-devel",
    "alsa-lib-devel",
    "mesa-devel",
    "libffi-devel",
    "zlib-devel",
    # XXX: https://bugzilla.mozilla.org/show_bug.cgi?id=1532281
    "dbus-glib-devel",
]
depends = ["virtual:cmd:thunderbird!thunderbird-wayland"]
pkgdesc = "Thunderbird mail client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND MPL-2.0"
url = "https://www.thunderbird.net"
source = f"$(MOZILLA_SITE)/{pkgname}/releases/{pkgver.replace('_beta', 'b')}/source/{pkgname}-{pkgver.replace('_beta', 'b')}.source.tar.xz"
sha256 = "3b1cf976b0d0f48255a603f8ffe8e24390ecd5bd285fc4d10fe48e1ba2513744"
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
options = ["!cross"]

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
            extra_opts += ["--disable-elf-hack", "--enable-rust-simd"]

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
        # wasi currently not ready
        "--without-wasm-sandboxed-libraries",
        # features
        "--enable-dbus",
        "--enable-jack",
        "--enable-ffmpeg",
        "--enable-pulseaudio",
        "--enable-necko-wifi",
        "--enable-default-toolkit=cairo-gtk3-wayland",
        "--enable-audio-backends=pulseaudio",
        # disabled features
        "--disable-crashreporter",
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
    # to be provided
    self.rm(self.destdir / "usr/bin/thunderbird")
    # default launcher
    self.install_link(
        "/usr/lib/thunderbird/thunderbird", "usr/bin/thunderbird-default"
    )
    # wayland launcher
    self.install_file(
        self.files_path / "thunderbird-wayland",
        "usr/lib/thunderbird",
        mode=0o755,
    )
    self.install_link(
        "/usr/lib/thunderbird/thunderbird-wayland",
        "usr/bin/thunderbird-wayland",
    )


def do_check(self):
    # XXX: maybe someday
    pass


@subpackage("thunderbird-wayland")
def _wl(self):
    self.pkgdesc = f"{pkgdesc} (prefer Wayland)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]  # prefer

    def inst():
        self.mkdir(self.destdir / "usr/bin", parents=True)
        self.ln_s("thunderbird-wayland", self.destdir / "usr/bin/thunderbird")

    return inst


@subpackage("thunderbird-default")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (no display server preference)"

    def inst():
        self.mkdir(self.destdir / "usr/bin", parents=True)
        self.ln_s("thunderbird-default", self.destdir / "usr/bin/thunderbird")

    return inst
