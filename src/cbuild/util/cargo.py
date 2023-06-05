import re


def clear_vendor_checksums(pkg, crate, vendor_dir="vendor"):
    p = pkg.cwd / vendor_dir / crate / ".cargo-checksum.json"
    p.write_text(re.sub(r"""("files":{)[^}]*""", r"\1", p.read_text()))


def get_environment(pkg, jobs=None):
    if not jobs:
        jobs = pkg.make_jobs

    sroot = pkg.profile().sysroot
    trip = pkg.profile().triplet
    utrip = trip.replace("-", "_").upper()

    env = {
        "CARGO_BUILD_TARGET": trip,
        f"CARGO_TARGET_{utrip}_LINKER": pkg.get_tool("CC"),
        "CARGO_BUILD_JOBS": str(jobs),
        "CARGO_PROFILE_RELEASE_PANIC": "abort",
        "CARGO_PROFILE_RELEASE_CODEGEN_UNITS": "1",
        "CARGO_REGISTRIES_CRATES_IO_PROTOCOL": "sparse",
        "CARGO_HOME": "/cbuild_cache/cargo",
        # gettext-rs
        "GETTEXT_BIN_DIR": "/usr/bin",
        "GETTEXT_LIB_DIR": str(sroot / "usr/lib/gettext"),
        # libssh2-sys
        "LIBSSH2_SYS_USE_PKG_CONFIG": "1",
        # sodium-sys
        "SODIUM_LIB_DIR": str(sroot / "usr/lib"),
        "SODIUM_INC_DIR": str(sroot / "usr/include"),
        "SODIUM_SHARED": "1",
        # openssl-sys
        "OPENSSL_NO_VENDOR": "1",
        # pcre2-sys
        "PCRE2_SYS_STATIC": "0",
        # rustonig-sys
        "RUSTONIG_SYSTEM_LIBONIG": "1",
        # zstd-sys
        "ZSTD_SYS_USE_PKG_CONFIG": "1",
        # cc-rs: make sure host compiler autoguess behavior is bypassed
        "HOST_CC": "clang",
        "HOST_CFLAGS": "-O2",
    }

    if pkg.profile().cross:
        env["PKG_CONFIG_ALLOW_CROSS"] = "1"

    if pkg.has_lto():
        if pkg.options["ltofull"]:
            env["CARGO_PROFILE_RELEASE_LTO"] = "fat"
        else:
            env["CARGO_PROFILE_RELEASE_LTO"] = "thin"

    return env


# very preliminary, no error checking, etc
def setup_vendor(pkg, vendor_path="vendor", wrksrc=None):
    dirn = pkg.cwd
    if wrksrc is not None:
        dirn = dirn / wrksrc
    pkg.mkdir(dirn / ".cargo")
    with open(dirn / ".cargo/config.toml", "w") as cf:
        cf.write(
            f"""
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "{vendor_path}"
"""
        )


class Cargo:
    def __init__(self, tmpl, jobs=None, env={}, wrksrc=None):
        self.template = tmpl
        self.wrksrc = wrksrc
        self.env = env
        self.jobs = jobs

    def _invoke(
        self,
        command,
        args,
        jobs,
        offline,
        base_env,
        env,
        wrksrc,
        ewrapper,
        wrapper,
    ):
        tmpl = self.template

        if not jobs:
            jobs = self.jobs

        if not jobs:
            jobs = tmpl.make_jobs

        renv = get_environment(tmpl, jobs=jobs)
        renv.update(tmpl.make_env)

        if base_env:
            renv.update(base_env)

        renv.update(self.env)
        renv.update(env)

        if not wrksrc:
            wrksrc = self.wrksrc
        if not wrksrc:
            wrksrc = tmpl.make_dir

        bargs = []
        if command != "vendor":
            bargs += ["--target", tmpl.profile().triplet]

        if offline:
            bargs.append("--offline")

        return self.template.do(
            *wrapper,
            *ewrapper,
            "cargo",
            command,
            *bargs,
            *args,
            env=renv,
            wrksrc=wrksrc,
            allow_network=not offline,
        )

    def invoke(
        self,
        command,
        args=[],
        jobs=None,
        offline=True,
        env={},
        wrksrc=None,
        wrapper=[],
    ):
        return self._invoke(command, args, jobs, None, env, wrksrc, [], wrapper)

    def vendor(self, args=[], env={}, wrksrc=None, wrapper=[]):
        return self._invoke(
            "vendor", args, 1, False, None, env, wrksrc, [], wrapper
        )

    def build(self, args=[], jobs=None, env={}, wrksrc=None, wrapper=[]):
        tmpl = self.template
        return self._invoke(
            "build",
            ["--release"] + tmpl.make_build_args + args,
            jobs,
            True,
            tmpl.make_build_env,
            env,
            wrksrc,
            tmpl.make_build_wrapper,
            wrapper,
        )

    def install(self, args=[], jobs=None, env={}, wrksrc=None, wrapper=[]):
        tmpl = self.template
        iargs = tmpl.make_install_args
        if len(iargs) == 0:
            iargs = ["--path", "."]
        retv = self._invoke(
            "install",
            ["--root", str(tmpl.chroot_destdir / "usr")] + iargs + args,
            jobs,
            True,
            tmpl.make_install_env,
            env,
            wrksrc,
            tmpl.make_install_wrapper,
            wrapper,
        )
        (tmpl.destdir / "usr/.crates.toml").unlink(missing_ok=True)
        (tmpl.destdir / "usr/.crates2.json").unlink(missing_ok=True)
        return retv

    def check(self, args=[], jobs=None, env={}, wrksrc=None, wrapper=[]):
        tmpl = self.template
        return self._invoke(
            "test",
            ["--release"] + tmpl.make_check_args + args,
            jobs,
            True,
            tmpl.make_check_env,
            env,
            wrksrc,
            tmpl.make_check_wrapper,
            wrapper,
        )
